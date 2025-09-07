# service.py - Business logic and data access for IPFS Control Panel API
import requests
import json
import base64
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import jwt
import bcrypt
from pymongo import MongoClient
from bson.json_util import dumps

# Configuration
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "ipfs_cp")
JWT_SECRET = os.environ.get("JWT_SECRET", "your-secret-key-change-in-production")
JWT_EXPIRATION_HOURS = 8

# Initialize MongoDB connection
db = None
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    # Test connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    db = None


# Authentication functions
def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_token(username: str) -> str:
    """Generate JWT token for user"""
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def verify_token(token: str) -> Optional[Dict]:
    """Verify JWT token and return payload"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# User authentication
def login_user(username: str, password: str) -> Dict:
    """Authenticate user login"""
    # Demo credentials for testing
    if username == "ipfs" and password == "926Ehkry46LY":
        token = generate_token(username)
        return {
            "success": True,
            "token": token,
            "user": {
                "username": username,
                "role": "analyst"
            }
        }
    else:
        return {
            "success": False,
            "error": "Invalid credentials"
        }

def logout_user(token: str) -> Dict:
    """Logout user (in a real app, you'd invalidate the token)"""
    return {"success": True, "message": "Logged out successfully"}

def get_current_user(token: str) -> Dict:
    """Get current user info from token"""
    payload = verify_token(token)
    if payload:
        return {
            "success": True,
            "user": {
                "username": payload['username'],
                "role": "analyst"
            }
        }
    else:
        return {
            "success": False,
            "error": "Invalid or expired token"
        }

def refresh_token(token: str) -> Dict:
    """Refresh user token"""
    payload = verify_token(token)
    if payload:
        new_token = generate_token(payload['username'])
        return {
            "success": True,
            "token": new_token
        }
    else:
        return {
            "success": False,
            "error": "Invalid or expired token"
        }

# CID Management functions
def get_cids(page: int, pagesize: int) -> Dict:
    """Get paginated list of CIDs"""
    if db is not None:
        try:
            collection = db["cp_candidates"]
            skip = (page - 1) * pagesize
            records = list(collection.find({}, {"_id": 0, "html_path": 0, "image_path": 0})
                          .skip(skip).limit(pagesize))
            total = collection.count_documents({})
            return {"cids": records, "total": total, "page": page, "page_size": pagesize}
        except Exception as e:
            print(f"Database error: {e}")
    
    # Return empty result when no database connection
    return {"cids": [], "total": 0, "page": page, "page_size": pagesize}

def get_phishing(page: int, pagesize: int) -> Dict:
    """Get paginated list of confirmed phishing CIDs"""
    if db is not None:
        try:
            collection = db["cp_candidates"]
            skip = (page - 1) * pagesize
            records = list(collection.find({"confirmed": 1}, {"_id": 0, "html_path": 0, "image_path": 0})
                          .skip(skip).limit(pagesize))
            total = collection.count_documents({"confirmed": 1})
            return {"cids": records, "total": total, "page": page, "page_size": pagesize}
        except Exception as e:
            print(f"Database error: {e}")
    
    # Return empty result when no database connection
    return {"cids": [], "total": 0, "page": page, "page_size": pagesize}

def get_image(file_path: str) -> str:
    """Encode a PNG image to Base64 string"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        else:
            # Return a small 1x1 transparent PNG as fallback
            return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
    except Exception as e:
        print(f"Error reading image {file_path}: {e}")
        return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

def get_one_cid(cid: str) -> Dict:
    """Get detailed information for a specific CID"""
    if db is not None:
        try:
            collection = db["cp_candidates"]
            record = collection.find_one({"cid": cid}, {"_id": 0})
            if record:
                record["image64"] = get_image(record.get("image_path", ""))
                record.pop("image_path", None)
                record.pop("html_path", None)
                return record
        except Exception as e:
            print(f"Database error: {e}")
    
    return {"error": "CID not found"}

def get_one_phishing(cid: str) -> Dict:
    """Get detailed information for a specific confirmed phishing CID"""
    if db is not None:
        try:
            collection = db["cp_candidates"]
            record = collection.find_one({"cid": cid, "confirmed": 1}, {"_id": 0})
            if record:
                record["image64"] = get_image(record.get("image_path", ""))
                record.pop("image_path", None)
                record.pop("html_path", None)
                return record
        except Exception as e:
            print(f"Database error: {e}")
    
    return {"error": "Phishing CID not found"}

def process_cid(data: Dict) -> Dict:
    """Process CID confirmation/denial"""
    cid = data.get("cid")
    confirmed = data.get("confirmed")
    
    if db is not None:
        try:
            collection = db["cp_candidates"]
            result = collection.update_many(
                {"cid": cid},
                {"$set": {"confirmed": confirmed}}
            )
            if result.modified_count > 0:
                return {"success": True, "message": "CID status updated successfully"}
            else:
                return {"success": False, "error": "CID not found"}
        except Exception as e:
            print(f"Database error: {e}")
            return {"success": False, "error": "Database error"}
    
    return {"success": False, "error": "Database not available"}

# Campaign Management functions
def get_campaigns() -> Dict:
    """Get list of all campaigns"""
    if db is not None:
        try:
            collection = db["campaigns"]
            campaigns = list(collection.find({}, {"_id": 0}))
            return {"campaigns": campaigns}
        except Exception as e:
            print(f"Database error: {e}")
    
    # Return empty result when no database connection
    return {"campaigns": []}

def get_campaign_cids(campaign_id: str) -> Dict:
    """Get CIDs associated with a specific campaign"""
    if db is not None:
        try:
            collection = db["cp_candidates"]
            cids = list(collection.find({"campaign_id": campaign_id}, {"_id": 0, "html_path": 0, "image_path": 0}))
            return {"cids": cids}
        except Exception as e:
            print(f"Database error: {e}")
    
    # Return empty result when no database connection
    return {"cids": []}

# Analytics functions
def get_analytics_cti_trends(days: int) -> Dict:
    """Get CTI detection trends for the specified number of days"""
    # TODO: Implement real analytics data retrieval from database
    return {"trends": []}

def get_analytics_obfuscation_stats(days: int) -> Dict:
    """Get obfuscation detection statistics"""
    # TODO: Implement real analytics data retrieval from database
    return {
        "total_obfuscated": 0,
        "javascript_heavy": 0,
        "encoded_content": 0,
        "minified_code": 0,
        "confidence_distribution": {
            "high": 0,
            "medium": 0,
            "low": 0
        }
    }

def get_analytics_bitswap_flow(days: int) -> Dict:
    """Get Bitswap network flow analytics"""
    # TODO: Implement real analytics data retrieval from database
    return {"flow_data": []}

def get_analytics_pdns_flow(days: int) -> Dict:
    """Get PDNS flow analytics"""
    # TODO: Implement real analytics data retrieval from database
    return {"flow_data": []}

def get_analytics_simhash_stats(days: int) -> Dict:
    """Get SimHash similarity detection statistics"""
    # TODO: Implement real analytics data retrieval from database
    return {
        "total_hashes": 0,
        "similarity_clusters": 0,
        "new_hashes": 0,
        "collision_rate": 0.0,
        "similarity_threshold": 0.85
    }

# System Health functions
SERVICES = [
    {"name": "cid-notify", "url": "http://localhost:9090/healthz"},
    {"name": "gateway-server", "url": "http://localhost:9191/healthz"},
    {"name": "pdns-processor", "url": "http://localhost:9393/healthz"},
    {"name": "control-panel-api", "url": "http://localhost:6655/healthz"}
]

def get_health() -> List[Dict]:
    """Get health status of all services"""
    health_status = []
    
    for service in SERVICES:
        name = service["name"]
        try:
            response = requests.get(service["url"], timeout=5)
            status = "Healthy" if response.status_code == 200 else "Unhealthy"
        except requests.RequestException:
            status = "Unreachable"
        
        health_status.append({
            "name": name,
            "status": status,
            "url": service["url"]
        })
    
    return health_status

def get_gateways() -> List[str]:
    """Get list of discovered gateways"""
    if db is not None:
        try:
            collection = db["gateways"]
            gateways = list(collection.find({}, {"_id": 0, "name": 1}))
            return [gw["name"] for gw in gateways if "name" in gw]
        except Exception as e:
            print(f"Database error: {e}")
    
    # Return empty result when no database connection
    return []

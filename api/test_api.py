#!/usr/bin/env python3
"""
Test script for IPFS Control Panel API
"""

import requests
import json
import sys

BASE_URL = "http://localhost:6655"

def test_endpoint(method, endpoint, data=None, headers=None, expected_status=200):
    """Test a single API endpoint"""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, headers=headers)
        else:
            print(f"✗ Unsupported method: {method}")
            return False
            
        if response.status_code == expected_status:
            print(f"✓ {method} {endpoint} - Status: {response.status_code}")
            return response.json() if response.content else {}
        else:
            print(f"✗ {method} {endpoint} - Expected: {expected_status}, Got: {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ {method} {endpoint} - Error: {e}")
        return None

def main():
    print("Testing IPFS Control Panel API...")
    print("=" * 50)
    
    # Test health check
    print("\n1. Testing Health Check:")
    test_endpoint("GET", "/healthz")
    
    # Test login
    print("\n2. Testing Authentication:")
    login_data = {"username": "ipfs", "password": "926Ehkry46LY"}
    login_response = test_endpoint("POST", "/api/auth/login", login_data)
    
    if not login_response or not login_response.get("success"):
        print("✗ Login failed - cannot continue with authenticated tests")
        return
    
    token = login_response.get("token")
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test authenticated endpoints
    print("\n3. Testing Authenticated Endpoints:")
    test_endpoint("GET", "/api/auth/me", headers=headers)
    test_endpoint("GET", "/api/cids/get-cids", headers=headers)
    test_endpoint("GET", "/api/cids/get-phishing", headers=headers)
    test_endpoint("GET", "/api/campaigns/", headers=headers)
    test_endpoint("GET", "/api/system/health", headers=headers)
    test_endpoint("GET", "/api/system/gateways", headers=headers)
    
    # Test analytics endpoints
    print("\n4. Testing Analytics Endpoints:")
    test_endpoint("GET", "/api/analytics/cti-trends", headers=headers)
    test_endpoint("GET", "/api/analytics/obfuscation-stats", headers=headers)
    test_endpoint("GET", "/api/analytics/bitswap-flow", headers=headers)
    test_endpoint("GET", "/api/analytics/pdns-flow", headers=headers)
    test_endpoint("GET", "/api/analytics/simhash-stats", headers=headers)
    
    # Test CID detail endpoint (using test CID)
    print("\n5. Testing CID Detail Endpoints:")
    test_cid = "QmTest1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7"
    test_endpoint("GET", f"/api/cids/get-one-cid/{test_cid}", headers=headers)
    test_endpoint("GET", f"/api/cids/get-one-phishing/{test_cid}", headers=headers)
    
    # Test campaign CIDs endpoint
    print("\n6. Testing Campaign Endpoints:")
    test_endpoint("GET", "/api/campaigns/test_campaign/cids", headers=headers)
    
    # Test logout
    print("\n7. Testing Logout:")
    test_endpoint("POST", "/api/auth/logout", headers=headers)
    
    print("\n" + "=" * 50)
    print("API testing completed!")

if __name__ == "__main__":
    main()

# server_auto.py - Automated Swagger generation with Flask-RESTX
from flask import Flask
from flask_restx import Api, Resource, fields, Namespace
from flask_cors import CORS
from service import (
    get_cids, get_phishing, get_one_cid, get_one_phishing, process_cid,
    get_health, get_gateways, get_campaigns, get_campaign_cids,
    get_analytics_cti_trends, get_analytics_obfuscation_stats,
    get_analytics_bitswap_flow, get_analytics_pdns_flow, get_analytics_simhash_stats,
    login_user, logout_user, get_current_user, refresh_token
)
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://localhost:3000"])

# Initialize Flask-RESTX API
api = Api(
    app,
    version='1.0.0',
    title='IPFS Control Panel API',
    description='''
    Backend API for the IPFS Control Panel, providing endpoints for managing phishing CIDs, 
    campaigns, analytics, and system health monitoring.
    
    ## Features
    - JWT-based authentication
    - CID management and phishing detection
    - Campaign organization
    - Comprehensive analytics and reporting
    - System health monitoring
    - Gateway management
    
    ## Demo Credentials
    - **Username**: `ipfs`
    - **Password**: `926Ehkry46LY`
    ''',
    doc='/docs/',  # Swagger UI will be available at /docs/
    prefix='/api'
)

# Define security scheme
authorizations = {
    'bearerAuth': {
        'type': 'http',
        'scheme': 'bearer',
        'bearerFormat': 'JWT',
        'description': 'JWT token obtained from login endpoint'
    }
}

# Create namespaces
auth_ns = Namespace('auth', description='Authentication operations')
cid_ns = Namespace('cids', description='CID management operations')
campaign_ns = Namespace('campaigns', description='Campaign management operations')
analytics_ns = Namespace('analytics', description='Analytics and reporting operations')
system_ns = Namespace('system', description='System health and monitoring operations')

# Add namespaces to API
api.add_namespace(auth_ns)
api.add_namespace(cid_ns)
api.add_namespace(campaign_ns)
api.add_namespace(analytics_ns)
api.add_namespace(system_ns)

# Define models
login_model = api.model('Login', {
    'username': fields.String(required=True, description='Username', example='ipfs'),
    'password': fields.String(required=True, description='Password', example='926Ehkry46LY')
})

user_model = api.model('User', {
    'username': fields.String(description='Username', example='ipfs'),
    'role': fields.String(description='User role', example='analyst')
})

login_response_model = api.model('LoginResponse', {
    'success': fields.Boolean(description='Login success status', example=True),
    'token': fields.String(description='JWT token', example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'),
    'user': fields.Nested(user_model)
})

error_model = api.model('Error', {
    'success': fields.Boolean(description='Success status', example=False),
    'error': fields.String(description='Error message', example='Invalid credentials')
})

cid_model = api.model('CID', {
    'cid': fields.String(description='IPFS Content Identifier', example='QmExample1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7'),
    'detection_date': fields.DateTime(description='Detection timestamp', example='2024-01-15T10:30:00Z'),
    'campaign': fields.String(description='Campaign name', example='Example Campaign'),
    'source': fields.String(description='Detection source', enum=['bitswap', 'pdns', 'both'], example='bitswap'),
    'confirmed': fields.Integer(description='Confirmation status (0=not confirmed, 1=confirmed)', enum=[0, 1], example=1),
    'confidence': fields.Float(description='Detection confidence', example=0.95),
    'simhash': fields.String(description='SimHash value', example='1234567890abcdef'),
    'gateway': fields.String(description='Gateway where CID was discovered', example='gateway.example.com')
})

cid_detail_model = api.inherit('CIDDetail', cid_model, {
    'image64': fields.String(description='Base64-encoded screenshot', example='iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==')
})

cid_list_model = api.model('CIDList', {
    'cids': fields.List(fields.Nested(cid_model)),
    'total': fields.Integer(description='Total number of CIDs', example=150),
    'page': fields.Integer(description='Current page number', example=1),
    'page_size': fields.Integer(description='Items per page', example=10)
})

process_cid_model = api.model('ProcessCID', {
    'cid': fields.String(required=True, description='IPFS Content Identifier', example='QmExample1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7'),
    'confirmed': fields.Integer(required=True, description='Confirmation status', enum=[0, 1], example=1)
})

process_response_model = api.model('ProcessResponse', {
    'success': fields.Boolean(description='Success status', example=True),
    'message': fields.String(description='Response message', example='CID status updated successfully')
})

campaign_model = api.model('Campaign', {
    'id': fields.String(description='Campaign ID', example='example_campaign'),
    'name': fields.String(description='Campaign name', example='Example Campaign'),
    'start_date': fields.DateTime(description='Campaign start date', example='2024-01-10T00:00:00Z'),
    'end_date': fields.DateTime(description='Campaign end date', example='2024-01-20T00:00:00Z'),
    'cid_count': fields.Integer(description='Number of CIDs in campaign', example=15),
    'status': fields.String(description='Campaign status', enum=['active', 'investigating', 'closed'], example='active'),
    'description': fields.String(description='Campaign description', example='Example campaign description')
})

campaign_list_model = api.model('CampaignList', {
    'campaigns': fields.List(fields.Nested(campaign_model))
})

cti_trend_model = api.model('CTITrend', {
    'date': fields.String(description='Date', example='2024-01-15'),
    'cti_detections': fields.Integer(description='CTI detections count', example=12),
    'password_fields': fields.Integer(description='Password fields detected', example=8),
    'suspicious_domains': fields.Integer(description='Suspicious domains found', example=3)
})

cti_trends_model = api.model('CTITrends', {
    'trends': fields.List(fields.Nested(cti_trend_model))
})

obfuscation_stats_model = api.model('ObfuscationStats', {
    'total_obfuscated': fields.Integer(description='Total obfuscated content', example=150),
    'javascript_heavy': fields.Integer(description='JavaScript-heavy content', example=75),
    'encoded_content': fields.Integer(description='Encoded content', example=30),
    'minified_code': fields.Integer(description='Minified code', example=45),
    'confidence_distribution': fields.Raw(description='Confidence distribution', example={'high': 40, 'medium': 60, 'low': 20})
})

bitswap_flow_model = api.model('BitswapFlow', {
    'date': fields.String(description='Date', example='2024-01-15'),
    'requests': fields.Integer(description='Number of requests', example=2500),
    'success_rate': fields.Float(description='Success rate', example=0.95),
    'avg_response_time': fields.Float(description='Average response time', example=1.2)
})

bitswap_flow_list_model = api.model('BitswapFlowList', {
    'flow_data': fields.List(fields.Nested(bitswap_flow_model))
})

pdns_flow_model = api.model('PDNSFlow', {
    'date': fields.String(description='Date', example='2024-01-15'),
    'queries': fields.Integer(description='Number of queries', example=1200),
    'unique_domains': fields.Integer(description='Unique domains', example=300),
    'gateway_discoveries': fields.Integer(description='Gateway discoveries', example=8)
})

pdns_flow_list_model = api.model('PDNSFlowList', {
    'flow_data': fields.List(fields.Nested(pdns_flow_model))
})

simhash_stats_model = api.model('SimHashStats', {
    'total_hashes': fields.Integer(description='Total hashes', example=2500),
    'similarity_clusters': fields.Integer(description='Similarity clusters', example=120),
    'new_hashes': fields.Integer(description='New hashes', example=200),
    'collision_rate': fields.Float(description='Collision rate', example=0.025),
    'similarity_threshold': fields.Float(description='Similarity threshold', example=0.85)
})

service_health_model = api.model('ServiceHealth', {
    'name': fields.String(description='Service name', example='cid-notify'),
    'status': fields.String(description='Service status', enum=['Healthy', 'Unhealthy', 'Unreachable'], example='Healthy'),
    'url': fields.String(description='Service URL', example='http://localhost:9090/healthz')
})

health_response_model = api.model('HealthResponse', {
    'healths': fields.List(fields.Nested(service_health_model))
})

gateways_response_model = api.model('GatewaysResponse', {
    'gateways': fields.List(fields.String, description='List of gateway URLs', example=['gateway.example.com', 'gateway2.example.com'])
})

# Authentication endpoints
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.doc('login')
    @auth_ns.expect(login_model)
    @auth_ns.marshal_with(login_response_model, code=200)
    @auth_ns.marshal_with(error_model, code=401)
    def post(self):
        """User login - Authenticate user and receive JWT token"""
        data = auth_ns.payload
        if not data or 'username' not in data or 'password' not in data:
            return {'success': False, 'error': 'Username and password required'}, 400
        
        result = login_user(data['username'], data['password'])
        if result.get('success'):
            return result, 200
        else:
            return result, 401

@auth_ns.route('/logout')
class Logout(Resource):
    @auth_ns.doc('logout', security='bearerAuth')
    @auth_ns.marshal_with(process_response_model)
    def post(self):
        """User logout - Logout user and invalidate session"""
        token = auth_ns.payload.get('token') if auth_ns.payload else None
        if not token:
            # Try to get from Authorization header
            from flask import request
            auth_header = request.headers.get('Authorization', '')
            token = auth_header.replace('Bearer ', '') if auth_header.startswith('Bearer ') else None
        
        result = logout_user(token) if token else {'success': True, 'message': 'Logged out successfully'}
        return result

@auth_ns.route('/me')
class Me(Resource):
    @auth_ns.doc('get_current_user', security='bearerAuth')
    @auth_ns.marshal_with(api.model('UserResponse', {
        'success': fields.Boolean(example=True),
        'user': fields.Nested(user_model)
    }), code=200)
    @auth_ns.marshal_with(error_model, code=401)
    def get(self):
        """Get current user info - Get information about the currently authenticated user"""
        from flask import request
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        result = get_current_user(token)
        if result.get('success'):
            return result, 200
        else:
            return result, 401

@auth_ns.route('/refresh')
class Refresh(Resource):
    @auth_ns.doc('refresh_token', security='bearerAuth')
    @auth_ns.marshal_with(api.model('RefreshResponse', {
        'success': fields.Boolean(example=True),
        'token': fields.String(example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...')
    }), code=200)
    @auth_ns.marshal_with(error_model, code=401)
    def post(self):
        """Refresh JWT token - Get a new JWT token using the current token"""
        from flask import request
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        result = refresh_token(token)
        if result.get('success'):
            return result, 200
        else:
            return result, 401

# CID Management endpoints
@cid_ns.route('/get-cids')
class GetCIDs(Resource):
    @cid_ns.doc('get_cids')
    @cid_ns.param('page', 'Page number (1-based)', type='integer', default=1)
    @cid_ns.param('page_size', 'Number of items per page', type='integer', default=10)
    @cid_ns.marshal_with(cid_list_model)
    def get(self):
        """Get paginated list of CIDs - Retrieve a paginated list of all CIDs with optional filtering"""
        from flask import request
        page = request.args.get('page', default=1, type=int)
        page_size = request.args.get('page_size', default=10, type=int)
        return get_cids(page, page_size)

@cid_ns.route('/get-phishing')
class GetPhishing(Resource):
    @cid_ns.doc('get_phishing')
    @cid_ns.param('page', 'Page number (1-based)', type='integer', default=1)
    @cid_ns.param('page_size', 'Number of items per page', type='integer', default=10)
    @cid_ns.marshal_with(cid_list_model)
    def get(self):
        """Get confirmed phishing CIDs - Retrieve a paginated list of confirmed phishing CIDs"""
        from flask import request
        page = request.args.get('page', default=1, type=int)
        page_size = request.args.get('page_size', default=10, type=int)
        return get_phishing(page, page_size)

@cid_ns.route('/get-one-cid/<string:cid>')
class GetOneCID(Resource):
    @cid_ns.doc('get_one_cid')
    @cid_ns.param('cid', 'IPFS Content Identifier')
    @cid_ns.marshal_with(cid_detail_model, code=200)
    @cid_ns.marshal_with(error_model, code=404)
    def get(self, cid):
        """Get detailed CID information - Retrieve detailed information for a specific CID including screenshot"""
        result = get_one_cid(cid)
        if 'error' in result:
            return result, 404
        return result

@cid_ns.route('/get-one-phishing/<string:cid>')
class GetOnePhishing(Resource):
    @cid_ns.doc('get_one_phishing')
    @cid_ns.param('cid', 'IPFS Content Identifier')
    @cid_ns.marshal_with(cid_detail_model, code=200)
    @cid_ns.marshal_with(error_model, code=404)
    def get(self, cid):
        """Get detailed phishing CID information - Retrieve detailed information for a specific confirmed phishing CID"""
        result = get_one_phishing(cid)
        if 'error' in result:
            return result, 404
        return result

@cid_ns.route('/process-cid')
class ProcessCID(Resource):
    @cid_ns.doc('process_cid')
    @cid_ns.expect(process_cid_model)
    @cid_ns.marshal_with(process_response_model, code=200)
    @cid_ns.marshal_with(error_model, code=400)
    def post(self):
        """Process CID confirmation - Confirm or deny a CID as phishing"""
        data = cid_ns.payload
        if not data or 'cid' not in data or 'confirmed' not in data:
            return {'success': False, 'error': 'Invalid data'}, 400
        
        result = process_cid(data)
        return result

# Campaign Management endpoints
@campaign_ns.route('/')
class Campaigns(Resource):
    @campaign_ns.doc('get_campaigns')
    @campaign_ns.marshal_with(campaign_list_model)
    def get(self):
        """Get all campaigns - Retrieve a list of all phishing campaigns"""
        return get_campaigns()

@campaign_ns.route('/<string:campaign_id>/cids')
class CampaignCIDs(Resource):
    @campaign_ns.doc('get_campaign_cids')
    @campaign_ns.param('campaign_id', 'Campaign identifier')
    @campaign_ns.marshal_with(cid_list_model)
    def get(self, campaign_id):
        """Get CIDs in campaign - Retrieve all CIDs associated with a specific campaign"""
        return get_campaign_cids(campaign_id)

# Analytics endpoints
@analytics_ns.route('/cti-trends')
class CTITrends(Resource):
    @analytics_ns.doc('get_cti_trends')
    @analytics_ns.param('days', 'Number of days to retrieve data for', type='integer', default=30)
    @analytics_ns.marshal_with(cti_trends_model)
    def get(self):
        """Get CTI detection trends - Retrieve CTI (Cyber Threat Intelligence) detection trends over time"""
        from flask import request
        days = request.args.get('days', default=30, type=int)
        return get_analytics_cti_trends(days)

@analytics_ns.route('/obfuscation-stats')
class ObfuscationStats(Resource):
    @analytics_ns.doc('get_obfuscation_stats')
    @analytics_ns.param('days', 'Number of days to retrieve data for', type='integer', default=30)
    @analytics_ns.marshal_with(obfuscation_stats_model)
    def get(self):
        """Get obfuscation statistics - Retrieve obfuscation detection statistics"""
        from flask import request
        days = request.args.get('days', default=30, type=int)
        return get_analytics_obfuscation_stats(days)

@analytics_ns.route('/bitswap-flow')
class BitswapFlow(Resource):
    @analytics_ns.doc('get_bitswap_flow')
    @analytics_ns.param('days', 'Number of days to retrieve data for', type='integer', default=7)
    @analytics_ns.marshal_with(bitswap_flow_list_model)
    def get(self):
        """Get Bitswap network flow analytics - Retrieve Bitswap network traffic and performance metrics"""
        from flask import request
        days = request.args.get('days', default=7, type=int)
        return get_analytics_bitswap_flow(days)

@analytics_ns.route('/pdns-flow')
class PDNSFlow(Resource):
    @analytics_ns.doc('get_pdns_flow')
    @analytics_ns.param('days', 'Number of days to retrieve data for', type='integer', default=7)
    @analytics_ns.marshal_with(pdns_flow_list_model)
    def get(self):
        """Get PDNS flow analytics - Retrieve PassiveDNS flow analytics and gateway discovery data"""
        from flask import request
        days = request.args.get('days', default=7, type=int)
        return get_analytics_pdns_flow(days)

@analytics_ns.route('/simhash-stats')
class SimHashStats(Resource):
    @analytics_ns.doc('get_simhash_stats')
    @analytics_ns.param('days', 'Number of days to retrieve data for', type='integer', default=30)
    @analytics_ns.marshal_with(simhash_stats_model)
    def get(self):
        """Get SimHash statistics - Retrieve SimHash similarity detection statistics"""
        from flask import request
        days = request.args.get('days', default=30, type=int)
        return get_analytics_simhash_stats(days)

# System Health endpoints
@system_ns.route('/health')
class Health(Resource):
    @system_ns.doc('get_health')
    @system_ns.marshal_with(health_response_model)
    def get(self):
        """Get system health status - Retrieve health status of all monitored services"""
        return {'healths': get_health()}

@system_ns.route('/gateways')
class Gateways(Resource):
    @system_ns.doc('get_gateways')
    @system_ns.marshal_with(gateways_response_model)
    def get(self):
        """Get discovered gateways - Retrieve list of all discovered IPFS gateways"""
        return {'gateways': get_gateways()}

# Health check endpoint (outside of API namespace)
@app.route("/healthz")
def health_check():
    """Health check endpoint"""
    return {'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6655))
    app.run(host="0.0.0.0", port=port, debug=True)

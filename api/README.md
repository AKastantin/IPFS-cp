# IPFS Control Panel API

Backend API for the IPFS Control Panel with **automatic Swagger documentation generation** using Flask-RESTX.

## 🚀 Features

- **Automatic API Documentation** - Generated from code annotations
- **Interactive Swagger UI** - Test endpoints directly in browser
- **JWT Authentication** - Secure token-based authentication
- **CID Management** - Phishing CID detection and management
- **Campaign Organization** - Group CIDs into campaigns
- **Analytics & Reporting** - Comprehensive threat intelligence analytics
- **System Health Monitoring** - Service and gateway monitoring
- **Demo Data** - Built-in demo data for development

## 🛠 Quick Start

### Prerequisites

- Python 3.8+
- MongoDB (optional - falls back to demo data if not available)

### Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set environment variables (optional):**
```bash
export MONGO_URI="mongodb://localhost:27017"
export DB_NAME="ipfs_cp"
export JWT_SECRET="your-secret-key"
```

3. **Start the server:**
```bash
./start.sh
# or
python3 server.py
```

The API will be available at `http://localhost:6655`

## 📖 API Documentation

### Interactive Swagger UI
- **URL**: `http://localhost:6655/docs/`
- **Features**: 
  - Test all endpoints directly from the browser
  - View request/response schemas
  - JWT authentication support
  - Auto-generated from code annotations

### OpenAPI Specification
- **URL**: `http://localhost:6655/api/swagger.json`
- **Usage**: Import into Postman, Insomnia, or other API tools

## 🔐 Authentication

### Demo Credentials
- **Username**: `ipfs`
- **Password**: `926Ehkry46LY`

### How to Authenticate
1. Use the login endpoint to get a JWT token
2. Include the token in the `Authorization` header: `Bearer <token>`
3. Use the Swagger UI "Authorize" button for interactive testing

## 📋 API Endpoints

### Authentication
- `POST /api/auth/login` - Login with username/password
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user info
- `POST /api/auth/refresh` - Refresh JWT token

### CID Management
- `GET /api/cids/get-cids` - Get paginated list of CIDs
- `GET /api/cids/get-phishing` - Get confirmed phishing CIDs
- `GET /api/cids/get-one-cid/{cid}` - Get detailed CID information
- `GET /api/cids/get-one-phishing/{cid}` - Get detailed phishing CID info
- `POST /api/cids/process-cid` - Confirm/deny CID as phishing

### Campaign Management
- `GET /api/campaigns/` - Get all campaigns
- `GET /api/campaigns/{id}/cids` - Get CIDs in a campaign

### Analytics
- `GET /api/analytics/cti-trends` - CTI detection trends
- `GET /api/analytics/obfuscation-stats` - Obfuscation statistics
- `GET /api/analytics/bitswap-flow` - Bitswap network flow
- `GET /api/analytics/pdns-flow` - PDNS flow analytics
- `GET /api/analytics/simhash-stats` - SimHash statistics

### System Health
- `GET /api/system/health` - Service health status
- `GET /api/system/gateways` - List of discovered gateways
- `GET /healthz` - API health check

## 🧪 Testing

### Using the Interactive UI
1. Start the server: `./start.sh`
2. Open: `http://localhost:6655/docs/`
3. Click "Authorize" and login with demo credentials
4. Test any endpoint using "Try it out"

### Using curl
```bash
# Login
curl -X POST http://localhost:6655/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "ipfs", "password": "926Ehkry46LY"}'

# Get CIDs (with token from login response)
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:6655/api/cids/get-cids
```

### Using the test script
```bash
python3 test_api.py
```

## 🔧 Development

### Adding New Endpoints

1. **Define models** in `server.py`:
```python
new_model = api.model('NewModel', {
    'field1': fields.String(required=True, description='Field description'),
    'field2': fields.Integer(description='Optional field')
})
```

2. **Create endpoint** with decorators:
```python
@namespace.route('/new-endpoint')
class NewEndpoint(Resource):
    @namespace.doc('new_endpoint')
    @namespace.expect(new_model)
    @namespace.marshal_with(response_model)
    def post(self):
        """New endpoint description"""
        # Implementation
```

3. **Documentation auto-generates!** - Swagger UI updates automatically

### Key Decorators
- `@api.doc()` - Add endpoint documentation
- `@api.expect()` - Define request model
- `@api.marshal_with()` - Define response model
- `@api.param()` - Define query parameters

## 🗄 Database Integration

The API supports MongoDB integration but gracefully falls back to demo data if MongoDB is not available.

### MongoDB Collections
- `cp_candidates` - Phishing CID data
- `campaigns` - Campaign information
- `gateways` - Gateway discovery data

### Demo Data
Comprehensive demo data is included for development:
- Sample phishing CIDs with various detection states
- Example phishing campaigns
- Demo IPFS gateways
- Generated trend data and statistics

## 🚀 Production Deployment

### Security Notes
- Change the JWT_SECRET in production
- Implement proper user management
- Add rate limiting and input validation
- Use HTTPS in production
- Implement proper session management

### Environment Variables
```bash
export MONGO_URI="mongodb://your-mongo-host:27017"
export DB_NAME="ipfs_cp_prod"
export JWT_SECRET="your-production-secret-key"
export PORT="6655"
```

## 📁 File Structure

```
api/
├── server.py              # Main Flask-RESTX server with auto-generated docs
├── service.py             # Business logic and data access
├── requirements.txt       # Python dependencies
├── start.sh              # Startup script
├── test_api.py           # API testing script
├── README.md             # This file
├── sample.html           # Demo phishing page
└── sample.png            # Demo image
```

## 🎯 Benefits of Automated Documentation

- ✅ **Always up-to-date** - Documentation reflects code changes automatically
- ✅ **Type-safe** - Request/response validation built-in
- ✅ **Interactive testing** - Test endpoints directly in browser
- ✅ **IDE support** - Full autocomplete and type checking
- ✅ **Zero maintenance** - No manual YAML files to maintain
- ✅ **Professional** - Production-ready API documentation

## 📚 Resources

- **Flask-RESTX Documentation**: https://flask-restx.readthedocs.io/
- **OpenAPI Specification**: https://swagger.io/specification/
- **Interactive Documentation**: `http://localhost:6655/docs/`

---

**Built with Flask-RESTX for automatic, always-up-to-date API documentation!** 🚀
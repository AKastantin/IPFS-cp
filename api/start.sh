#!/bin/bash

# IPFS Control Panel API Startup Script

echo "Starting IPFS Control Panel API with Automated Swagger Generation..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Check if requirements are installed
if ! python3 -c "import flask_restx" &> /dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Set environment variables (optional)
export MONGO_URI=${MONGO_URI:-"mongodb://localhost:27017"}
export DB_NAME=${DB_NAME:-"ipfs_cp"}
export JWT_SECRET=${JWT_SECRET:-"your-secret-key-change-in-production"}

# Start the server
echo "Starting server on http://localhost:6655"
echo "📖 Interactive API Documentation: http://localhost:6655/docs/"
echo "📋 OpenAPI Specification: http://localhost:6655/api/swagger.json"
echo "Press Ctrl+C to stop"
python3 server.py

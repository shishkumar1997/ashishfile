# Quick Start Guide

## Running the Server from ashishfile directory

### Option 1: Using the startup script
```bash
cd /home/admin2/user_management/ashishfile
./start_server.sh
```

### Option 2: Manual command
```bash
cd /home/admin2/user_management/ashishfile
source ../venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Access the API

- **API Base URL**: `http://localhost:8000`
- **Interactive API Docs (Swagger)**: `http://localhost:8000/docs`
- **Alternative API Docs (ReDoc)**: `http://localhost:8000/redoc`

## API Endpoints

- **POST** `/api/register` - Register a new user
- **POST** `/api/login` - Login and get JWT token
- **GET** `/api/me` - Get current user profile (requires authentication)
- **GET** `/api/user_data` - Get all users (requires authentication)

## Fixed Issues

✅ Favicon 404 error has been fixed - no more 404 errors in logs
✅ Server can now run from ashishfile directory
✅ All dependencies are properly configured

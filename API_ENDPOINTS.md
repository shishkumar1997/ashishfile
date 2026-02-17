# FastAPI User Management System - API Endpoints

## Base URL
`http://localhost:8000`

## Authentication
Most endpoints require JWT token in Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

---

## User Management Endpoints

### 1. Register User
**POST** `/api/register`
- Register a new user
- **Request Body:**
  ```json
  {
    "full_name": "John Doe",
    "email": "john@example.com",
    "password": "password123",
    "role": "Admin"
  }
  ```

### 2. Login
**POST** `/api/login`
- User login and get JWT token
- **Request Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```

### 3. Get Current User Profile
**GET** `/api/me`
- Get authenticated user's profile
- Requires authentication

### 4. Get All Users (with Search & Pagination)
**GET** `/api/user_data`
- Get all users with search and pagination
- **Query Parameters:**
  - `search` (optional): Search by full_name or email
  - `page` (default: 1): Page number
  - `page_size` (default: 5): Items per page (max 100)
- **Response includes pagination links:**
  - `next`: URL for next page
  - `pre`: URL for previous page

---

## Accounts Endpoints (`/api/accounts/v1`)

### 1. Web Login
**POST** `/api/accounts/v1/web_login`
- Web login with remember_me option
- **Request Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "password123",
    "remember_me": true
  }
  ```

### 2. Forgot Password
**POST** `/api/accounts/v1/forgot_password`
- Request password reset
- **Request Body:**
  ```json
  {
    "email": "john@example.com"
  }
  ```

### 3. Change Password
**POST** `/api/accounts/v1/change_password`
- Change password using reset token
- **Request Body:**
  ```json
  {
    "token": "reset_token_here",
    "new_password": "newpassword123",
    "confirm_password": "newpassword123"
  }
  ```

### 4. Refresh Token
**POST** `/api/accounts/v1/refresh_token`
- Refresh access token
- **Request Body:**
  ```json
  {
    "access_token": "current_token_here"
  }
  ```

---

## Profile Endpoints (`/api/accounts/v1`)

### 1. Get Profile
**GET** `/api/accounts/v1/profile`
- Get current user profile
- Requires authentication

### 2. Update Profile
**PUT** `/api/accounts/v1/profile`
- Update current user profile
- **Request Body:**
  ```json
  {
    "full_name": "Updated Name",
    "email": "newemail@example.com"
  }
  ```

---

## Dashboard Endpoints (`/api`)

### 1. Get Dashboard Count
**GET** `/api/dashboard/count`
- Get dashboard counts based on user role
- Returns different data for:
  - Admin (role_id: 1)
  - SubAdmin (role_id: 2)
  - Business Head (role_id: 3)
  - Regional Manager (role_id: 4)
  - Key Account Manager (role_id: 9)
  - Sales Team/Teacher (role_id: 5)

---

## Role Access Endpoints (`/api`)

### 1. Get Role Access List
**GET** `/api/role_access`
- Get all role accesses with search
- **Query Parameters:**
  - `search` (optional): Search by access name

### 2. Get Role Access List by Role Type
**GET** `/api/role_access_list`
- Get role access list filtered by role type
- **Query Parameters:**
  - `role_type` (optional): Filter by role type (1,2,3,4,5,9)

### 3. Get User Role Access Status
**GET** `/api/user_role_access_status`
- Get user role access status with nested structure
- **Query Parameters:**
  - `user_id` (required): User ID to get access for
  - `role_type` (optional): Filter by role type

### 4. Get User Role Access (Dashboard)
**GET** `/api/user_role_access`
- Get current user's role access for dashboard
- Returns nested structure: role_access → submodule → submodule_crud
- Includes hardcoded Dashboard entry (id: 20)
- Requires authentication

---

## Response Format

All endpoints return responses in this format:
```json
{
  "status": 200,
  "message": "Success message",
  "data": { ... }
}
```

For paginated responses:
```json
{
  "pagination": {
    "total": 100,
    "page": 1,
    "page_size": 10,
    "total_pages": 10,
    "next": "http://localhost:8000/api/user_data?page=2&page_size=10",
    "pre": null
  },
  "status": 200,
  "message": "Data found Successfully",
  "data": [ ... ]
}
```

---

## User Roles

- `Admin` (role_id: 1)
- `SubAdmin` (role_id: 2)
- `Business Head` (role_id: 3)
- `Regional Manager` (role_id: 4)
- `Sales Team` (role_id: 5)
- `Key Account Manager` (role_id: 9)
- `Teacher` (role_id: 6)

---

## Interactive API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## Notes

1. All passwords are hashed using Argon2
2. JWT tokens expire after 8 hours (configurable in .env)
3. CORS is enabled for all origins (configure in production)
4. Database is SQLite by default (change in .env for production)

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import Optional
from urllib.parse import urlencode
from app.dependencies import get_current_user
from app.models import User, UserRole
from app.schemas import (
    UserRegister, UserLogin, UserResponse, TokenResponse
)
from app.auth import hash_password, verify_password, create_access_token
from app.database import get_db


router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserRegister, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ==============================
# LOGIN
# ==============================

@router.post("/login", response_model=TokenResponse)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.email).first()

    if not user or not verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "status": 200,
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "Bearer"
    }


# ==============================
# PROTECTED ROUTE
# ==============================

@router.get("/me")
def get_my_profile(current_user: User = Depends(get_current_user)):

    data={
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role
    }
    return {
        "status": 200,
        "message": "Data found Successfully",
        "data": data,
    }



@router.get("/user_data")
def get_all_users(
    request: Request,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
    search: Optional[str] = Query(None, description="Search by full_name or email"),
    page: int = Query(1, ge=1, description="Page number (starts from 1)"),
    page_size: int = Query(5, ge=1, le=100, description="Number of items per page (max 100)")
):
  
    # Start with base query
    query = db.query(User)
    
    # Apply search filter if provided
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                User.full_name.ilike(search_term),
                User.email.ilike(search_term)
            )
        )
    
    # Get total count before pagination
    total = query.count()
    
    # Calculate pagination
    total_pages = (total + page_size - 1) // page_size if total > 0 else 0
    skip = (page - 1) * page_size
    
    
    # Build base URL
    base_url = str(request.url).split('?')[0]  # Get URL without query parameters
    
    # Build query parameters for links
    def build_query_params(page_num: int) -> str:
        params = {"page": page_num, "page_size": page_size}
        if search:
            params["search"] = search
        return urlencode(params)

    # Apply pagination
    users = query.offset(skip).limit(page_size).all()
    
    # Generate next and previous page links
    next_link = None
    previous_link = None
    
    if page < total_pages:
        next_link = f"{base_url}?{build_query_params(page + 1)}"
    
    if page > 1:
        previous_link = f"{base_url}?{build_query_params(page - 1)}"
    
    return {
        "pagination": {
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "next": next_link,
            "pre": previous_link
        },
        "status": 200,
        "message": "Data found Successfully",
        "data": users,
        
    }
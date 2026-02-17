from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_current_user
from app.models import User
from app.schemas import (
    UserLogin, WebLoginResponse, ForgetPasswordRequest, 
    ForgetPasswordResponse, ChangePasswordRequest, ChangePasswordResponse,
    RefreshTokenRequest, RefreshTokenResponse
)
from app.auth import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from app.database import get_db
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()


@router.post("/web_login", response_model=WebLoginResponse)
def web_login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Optimized Web Login API - Fast response
    """
    try:
        email = user_credentials.email
        password = user_credentials.password
        remember_me = user_credentials.remember_me
        
        # Get user by email
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email or password"
            )
        
        # Verify password
        if not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email or password"
            )
        
        # Update last active on
        # Note: Add last_active_on field to User model if needed
        # user.last_active_on = datetime.utcnow()
        # db.commit()
        
        # Create access token
        access_token = create_access_token(data={"sub": user.email, "user_id": user.id})
        
        # Prepare user data
        user_data = {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role.value,
            "access_token": access_token,
            "token_type": "Bearer",
            "remember_me": remember_me
        }
        
        return {
            "status": 200,
            "message": "User login successful",
            "data": user_data
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.post("/forgot_password", response_model=ForgetPasswordResponse)
def forgot_password(request: ForgetPasswordRequest, db: Session = Depends(get_db)):
    """
    Forgot Password API - Sends password reset link via email
    """
    try:
        email = request.email
        
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            return {
                "status": 400,
                "message": "This email address is not registered with us.",
                "data": None
            }
        
        
        allowed_roles = ["Admin", "SubAdmin", "Business Head", "Regional Manager", "Key Account Manager"]
        if user.role.value not in allowed_roles:
            return {
                "status": 400,
                "message": "This email address is not registered with us.",
                "data": None
            }
        
        # Generate reset token
        reset_token = create_access_token(data={"sub": email, "type": "password_reset"})
        
        
        reset_link = f"http://localhost:3000/change_password_confirmation/{reset_token}"
        
        
        
        return {
            "status": 200,
            "message": "Password reset link sent successfully",
            "data": reset_link
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.post("/change_password", response_model=ChangePasswordResponse)
def change_password(request: ChangePasswordRequest, db: Session = Depends(get_db)):
    """
    Change Password API - Changes password using reset token
    """
    try:
        token = request.token
        new_password = request.new_password
        confirm_password = request.confirm_password
        
        # Validate passwords match
        if new_password != confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )
        
        # Decode token
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email = payload.get("sub")
            token_type = payload.get("type")
            
            if token_type != "password_reset":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid token type"
                )
                
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired token"
            )
        
        # Get user
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Update password
        user.password = hash_password(new_password)
        db.commit()
        
        return {
            "status": 200,
            "message": "Password changed successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.post("/refresh_token", response_model=RefreshTokenResponse)
def refresh_token(request: RefreshTokenRequest, db: Session = Depends(get_db)):
    """
    Refresh Token API - Refreshes access token
    """
    try:
        access_token = request.access_token
        
        # Decode token
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
            email = payload.get("sub")
            
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Expired access token, please login again."
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token"
            )
        
        # Get user
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Create new token
        new_token = create_access_token(data={"sub": user.email, "user_id": user.id})
        
        # Prepare user data
        user_data = {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role.value,
            "access_token": new_token,
            "token_type": "Bearer"
        }
        
        return {
            "status": 200,
            "message": "Token refreshed successfully",
            "data": user_data
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

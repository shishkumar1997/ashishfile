from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_current_user
from app.models import User
from app.schemas import ProfileGetResponse, ProfileUpdateRequest, ProfileUpdateResponse
from app.database import get_db

router = APIRouter()


@router.get("/profile", response_model=ProfileGetResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    """
    Get current user profile
    """
    try:
        user_data = {
            "id": current_user.id,
            "full_name": current_user.full_name,
            "email": current_user.email,
            "role": current_user.role.value
        }
        
        return {
            "status": 200,
            "message": "Profile found successfully",
            "data": user_data
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.put("/profile", response_model=ProfileUpdateResponse)
def update_profile(
    request: ProfileUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
 
    try:
        # Get user from database
        user = db.query(User).filter(User.id == current_user.id).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        if request.full_name is not None:
            user.full_name = request.full_name
        
        if request.email is not None:
            existing_user = db.query(User).filter(
                User.email == request.email,
                User.id != user.id
            ).first()
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
            user.email = request.email
        
        db.commit()
        db.refresh(user)
        
        user_data = {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role.value
        }
        
        return {
            "status": 200,
            "message": "Profile updated successfully",
            "data": user_data
        }
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

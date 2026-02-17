from fastapi import APIRouter, Depends, HTTPException, Query, Request
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import Optional
from urllib.parse import urlencode
from app.dependencies import get_current_user
from app.models import User, UserRole
from app.schemas import ChangePasswordRequest, ChangePasswordResponse, DashboardCountResponse, ForgetPasswordRequest, ForgetPasswordResponse, RefreshTokenRequest, RefreshTokenResponse, UserRegister, UserLogin, UserResponse, TokenResponse
from app.auth import ALGORITHM, SECRET_KEY, hash_password, verify_password, create_access_token
from app.database import get_db
from fastapi import status
import jwt


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



@router.get("/dashboard/count", response_model=DashboardCountResponse)
def get_dashboard_count(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
 
    try:
        user_role = current_user.role
        
        # Admin Dashboard
        if user_role == UserRole.admin:
            data = _get_admin_dashboard_data(db)
        
        # SubAdmin Dashboard
        elif user_role == UserRole.subadmin:
            data = _get_subadmin_dashboard_data(db)
        
        # Business Head Dashboard
        elif user_role == UserRole.business_head:
            data = _get_business_head_dashboard_data(db, current_user)
        
        # Regional Manager Dashboard
        elif user_role == UserRole.regional_manager:
            data = _get_regional_manager_dashboard_data(db, current_user)
        
        # Key Account Manager Dashboard
        elif user_role == UserRole.key_account_manager:
            data = _get_kam_dashboard_data(db, current_user)
        
        # Teacher/Sales Team Dashboard
        elif user_role == UserRole.teacher or user_role == UserRole.sales_team:
            data = _get_teacher_dashboard_data(db, current_user)
        
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not logged in or invalid role"
            )
        
        return {
            "status": 200,
            "message": "Dashboard data retrieved successfully",
            "data": data
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


def _get_admin_dashboard_data(db: Session):

    role_counts = db.query(
        User.role,
        func.count(User.id).label('count')
    ).group_by(User.role).all()
    
    counts_dict = {role.value: count for role, count in role_counts}
    
    # Total teachers (leads)
    teacher_count = db.query(User).filter(
        User.role == UserRole.teacher
    ).count()
    
    
    
    return {
        'Total_numbers_of_leads': teacher_count,
        'Total_numbers_of_subject': 0,  # Update when SubjectMaster model is added
        'Total_Business_head': counts_dict.get(UserRole.business_head.value, 0),
        'Total_Regional_Managers': counts_dict.get(UserRole.regional_manager.value, 0),
        'Total_Key_Account_Managers': counts_dict.get(UserRole.key_account_manager.value, 0),
        'Sales_managers': counts_dict.get(UserRole.sales_team.value, 0),
        'Total_numbers_of_books': 0,  # Update when BookMaster model is added
        'total_spent_time': "00:00:00",  # Update when watch_time tracking is added
        'total_subadmin_count': counts_dict.get(UserRole.subadmin.value, 0),
        'open_leads': 0,  # Update when leads calculation is implemented
        'closed_leads': 0  # Update when leads calculation is implemented
    }


def _get_subadmin_dashboard_data(db: Session):

    role_counts = db.query(
        User.role,
        func.count(User.id).label('count')
    ).group_by(User.role).all()
    
    counts_dict = {role.value: count for role, count in role_counts}
    teacher_count = db.query(User).filter(User.role == UserRole.teacher).count()
    
    return {
        'Total_numbers_of_leads': teacher_count,
        'Total_numbers_of_subject': 0,
        'Total_Business_head': counts_dict.get(UserRole.business_head.value, 0),
        'Total_Regional_Managers': counts_dict.get(UserRole.regional_manager.value, 0),
        'Total_Key_Account_Managers': counts_dict.get(UserRole.key_account_manager.value, 0),
        'Sales_managers': counts_dict.get(UserRole.sales_team.value, 0),
        'Total_numbers_of_books': 0,
        'total_spent_time': "00:00:00",
        'total_subadmin_count': counts_dict.get(UserRole.subadmin.value, 0),
        'open_leads': 0,
        'closed_leads': 0
    }


def _get_business_head_dashboard_data(db: Session, user: User):
    
    
    business_head_count = db.query(User).filter(
        User.role == UserRole.business_head
    ).count()
    
    rm_count = db.query(User).filter(
        User.role == UserRole.regional_manager
    ).count()
    
    kam_count = db.query(User).filter(
        User.role == UserRole.key_account_manager
    ).count()
    
    sales_count = db.query(User).filter(
        User.role == UserRole.sales_team
    ).count()
    
    teacher_count = db.query(User).filter(
        User.role == UserRole.teacher
    ).count()
    
    return {
        'Total_numbers_of_leads': teacher_count,
        'Total_numbers_of_subject': 0,
        'Total_Business_head': business_head_count,
        'Total_Regional_Managers': rm_count,
        'Total_Key_Account_Managers': kam_count,
        'Sales_managers': sales_count,
        'Total_numbers_of_books': 0,
        'total_spent_time': "00:00:00",
        'open_leads': 0,
        'closed_leads': 0
    }


def _get_regional_manager_dashboard_data(db: Session, user: User):

    rm_count = db.query(User).filter(
        User.role == UserRole.regional_manager
    ).count()
    
    kam_count = db.query(User).filter(
        User.role == UserRole.key_account_manager
    ).count()
    
    sales_count = db.query(User).filter(
        User.role == UserRole.sales_team
    ).count()
    
    teacher_count = db.query(User).filter(
        User.role == UserRole.teacher
    ).count()
    
    business_head_count = db.query(User).filter(
        User.role == UserRole.business_head
    ).count()
    
    return {
        'Total_numbers_of_leads': teacher_count,
        'Total_numbers_of_subject': 0,
        'Total_numbers_of_books': 0,
        'total_spent_time': "00:00:00",
        'Sales_managers': sales_count,
        'Total_Business_head': business_head_count,
        'Total_Regional_Managers': rm_count,
        'Total_Key_Account_Managers': kam_count,
        'Total_Reportees': sales_count + kam_count,
        'open_leads': 0,
        'closed_leads': 0
    }


def _get_kam_dashboard_data(db: Session, user: User):

    teacher_count = db.query(User).filter(
        User.role == UserRole.teacher
    ).count()
    
    return {
        'Total_numbers_of_leads': teacher_count,
        'Total_numbers_of_subject': 0,
        'Total_numbers_of_books': 0,
        'total_spent_time': "00:00:00",
        'open_leads': 0,
        'closed_leads': 0
    }


def _get_teacher_dashboard_data(db: Session, user: User):

    teacher_count = db.query(User).filter(
        User.role == UserRole.teacher
    ).count()
    
    return {
        'Total_numbers_of_leads': teacher_count,
        'Total_numbers_of_subject': 0,
        'Total_numbers_of_books': 0,
        'total_spent_time': "00:00:00",
        'open_leads': 0,
        'closed_leads': 0
    }



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

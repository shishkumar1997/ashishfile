from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.dependencies import get_current_user
from app.models import User, UserRole
from app.schemas import DashboardCountResponse
from app.database import get_db

router = APIRouter()


@router.get("/dashboard/count", response_model=DashboardCountResponse)
def get_dashboard_count(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get dashboard count based on user role
    Optimized with bulk queries and aggregations
    """
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
    """Admin dashboard - aggregated counts"""
    # Count users by role
    role_counts = db.query(
        User.role,
        func.count(User.id).label('count')
    ).group_by(User.role).all()
    
    counts_dict = {role.value: count for role, count in role_counts}
    
    # Total teachers (leads)
    teacher_count = db.query(User).filter(
        User.role == UserRole.teacher
    ).count()
    
    # Note: Add SubjectMaster and BookMaster models if needed
    # subject_count = db.query(SubjectMaster).filter(...).count()
    # book_count = db.query(BookMaster).filter(...).count()
    
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
    """SubAdmin dashboard"""
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
    """Business Head dashboard"""
    # Note: Add created_by_id, assigned_by_id fields to User model if needed
    # For now, using basic counts
    
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
    """Regional Manager dashboard"""
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
    """Key Account Manager dashboard"""
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
    """Teacher/Sales Team dashboard"""
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

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import or_, func, not_
from typing import Optional, List, Dict, Any
from app.dependencies import get_current_user
from app.models import (
    RoleAccessMaster, SubModuleMaster, SubModuleCRUDMaster, 
    MapRolesAccessToSubAdmin, User, UserRole
)
from app.schemas import RoleAccessResponse
from app.database import get_db
import re

router = APIRouter()


@router.get("/role_access", response_model=RoleAccessResponse)
def get_role_access_list(
    search: Optional[str] = Query(None, description="Search by access name"),
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get role access list with search functionality
    Returns list of role accesses ordered by created_on descending
    """
    try:
        # Start with base query
        query = db.query(RoleAccessMaster).order_by(RoleAccessMaster.created_on.desc())
        
        # Apply search filter if provided
        if search:
            search_term = search.strip()
            search_pattern = f"%{search_term}%"
            query = query.filter(
                RoleAccessMaster.access.ilike(search_pattern)
            )
        
        # Get all results
        queryset = query.all()
        
        # Convert to dictionary format
        data = [
            {
                "id": item.id,
                "access": item.access,
                "status1": item.status1,
                "status2": item.status2,
                "status3": item.status3,
                "status4": item.status4,
                "status5": item.status5,
                "status9": item.status9,
                "created_on": item.created_on.isoformat() if item.created_on else None,
                "updated_on": item.updated_on.isoformat() if item.updated_on else None
            }
            for item in queryset
        ]
        
        if not data:
            return {
                "status": 200,
                "message": "No data found",
                "data": []
            }
        
        return {
            "status": 200,
            "message": "Data found successfully",
            "data": data
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.get("/role_access_list", response_model=RoleAccessResponse)
def get_role_access_list_by_role_type(
    role_type: Optional[int] = Query(None, description="Role type filter (1=admin, 2=subadmin, 3=business_head, 4=regional_manager, 5=sales_team, 9=key_account_manager)"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get role access list based on current user role and role_type filter
    """
    try:
        # Get current user's role_id (map from UserRole enum to numeric ID)
        role_id_map = {
            UserRole.admin: 1,
            UserRole.subadmin: 2,
            UserRole.business_head: 3,
            UserRole.regional_manager: 4,
            UserRole.sales_team: 5,
            UserRole.key_account_manager: 9,
            UserRole.teacher: 6
        }
        role_id = role_id_map.get(current_user.role, 1)
        
        # Base query
        query = db.query(RoleAccessMaster).order_by(RoleAccessMaster.id)
        
        # Role-based filtering logic
        if role_id == 1:  # Admin
            if role_type:
                if role_type == 5:
                    query = query.filter(RoleAccessMaster.id != 1)
                # Other role_types return all
        elif role_id == 2:  # SubAdmin
            if role_type:
                if role_type == 5:
                    query = query.filter(RoleAccessMaster.id != 1)
        elif role_id == 3:  # Business Head
            if role_type:
                if role_type == 1:
                    query = query.filter(RoleAccessMaster.id != 1)
                elif role_type == 5:
                    query = query.filter(RoleAccessMaster.id != 1)
        elif role_id == 4:  # Regional Manager
            if role_type:
                if role_type == 1:
                    query = query.filter(RoleAccessMaster.id != 1)
                elif role_type == 5:
                    query = query.filter(RoleAccessMaster.id != 1)
        elif role_id == 9:  # Key Account Manager
            if role_type:
                if role_type == 1:
                    query = query.filter(RoleAccessMaster.id != 1)
                elif role_type == 5:
                    query = query.filter(RoleAccessMaster.id != 1)
        elif role_id == 5:  # Sales Team
            query = query.filter(RoleAccessMaster.id != 1)
        
        # Get results
        role_access_list = query.all()
        
        # Serialize data
        data = [
            {
                "id": item.id,
                "access": item.access,
                "status1": item.status1,
                "status2": item.status2,
                "status3": item.status3,
                "status4": item.status4,
                "status5": item.status5,
                "status9": item.status9
            }
            for item in role_access_list
        ]
        
        return {
            "status": 200,
            "message": "Data found successfully",
            "data": data
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.get("/user_role_access_status", response_model=RoleAccessResponse)
def get_user_role_access_status(
    user_id: int = Query(..., description="User ID to get access status for"),
    role_type: Optional[int] = Query(None, description="Role type filter"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get user role access status with nested structure (role_access -> submodule -> submodule_crud)
    """
    try:
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Please provide valid user id"
            )
        
        # Get target user
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Get current user's role_id
        role_id_map = {
            UserRole.admin: 1,
            UserRole.subadmin: 2,
            UserRole.business_head: 3,
            UserRole.regional_manager: 4,
            UserRole.sales_team: 5,
            UserRole.key_account_manager: 9,
            UserRole.teacher: 6
        }
        current_role_id = role_id_map.get(current_user.role, 1)
        target_role_id = role_id_map.get(user.role, 1)
        
        # Get role access based on current user role and role_type
        role_access_query = db.query(RoleAccessMaster).order_by(RoleAccessMaster.id)
        submodule_query = db.query(SubModuleMaster)
        
        # Apply role-based filtering
        if current_role_id == 1:  # Admin
            if role_type == 2:
                submodule_query = submodule_query.filter(SubModuleMaster.id != 1)
            elif role_type == 3:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2]))
            elif role_type == 4:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            elif role_type == 9:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 15]))
            elif role_type == 5:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 4, 15]))
        elif current_role_id == 2:  # SubAdmin
            submodule_query = submodule_query.filter(SubModuleMaster.id != 1)
            if role_type == 2:
                submodule_query = submodule_query.filter(SubModuleMaster.id != 1)
            elif role_type == 3:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2]))
            elif role_type == 4:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            elif role_type == 9:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 15]))
            elif role_type == 5:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 4, 15]))
        elif current_role_id == 3:  # Business Head
            submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2]))
            if role_type == 1:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
            elif role_type == 3:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2]))
            elif role_type == 4:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            elif role_type == 9:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 15]))
            elif role_type == 5:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 4, 15]))
        elif current_role_id == 4:  # Regional Manager
            submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            if role_type == 1:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
            elif role_type == 2:
                submodule_query = submodule_query.filter(SubModuleMaster.id != 1)
            elif role_type == 3:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2]))
            elif role_type == 4:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            elif role_type == 9:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 15]))
            elif role_type == 5:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 4, 15]))
        elif current_role_id == 9:  # Key Account Manager
            submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            if role_type == 1:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
            elif role_type == 2:
                submodule_query = submodule_query.filter(SubModuleMaster.id != 1)
            elif role_type == 3:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2]))
            elif role_type == 4:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3]))
            elif role_type == 9:
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 15]))
            elif role_type == 5:
                role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
                submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 4, 15]))
        elif current_role_id == 5:  # Sales Team
            role_access_query = role_access_query.filter(RoleAccessMaster.id != 1)
            submodule_query = submodule_query.filter(~SubModuleMaster.id.in_([1, 2, 3, 4, 15]))
        
        # Get all data
        role_access_list = role_access_query.all()
        submodule_list = submodule_query.all()
        submodule_crud_list = db.query(SubModuleCRUDMaster).all()
        user_access_list = db.query(MapRolesAccessToSubAdmin).filter(
            MapRolesAccessToSubAdmin.user_id == user.id
        ).all()
        
        # Create lookup dictionaries for faster access
        user_access_dict = {
            (ua.access_id, ua.submodule_access_id, ua.submodule_crud_access_id): True
            for ua in user_access_list
        }
        
        # Build nested structure
        result = []
        for role_access in role_access_list:
            role_access_data = {
                "id": role_access.id,
                "access": role_access.access,
                "status": True if target_role_id == 1 else (
                    any(ua.access_id == role_access.id for ua in user_access_list)
                ),
                "sub_module": [],
                "sub_module_crud": None
            }
            
            # Get submodules for this role_access
            submodules = [sm for sm in submodule_list if sm.role_access_id == role_access.id]
            
            if submodules:
                submodule_result = []
                for submodule in submodules:
                    submodule_data = {
                        "id": submodule.id,
                        "name": submodule.name,
                        "status": True if target_role_id == 1 else (
                            any(ua.submodule_access_id == submodule.id for ua in user_access_list)
                        ),
                        "sub_module_crud": []
                    }
                    
                    # Get submodule CRUDs
                    submodule_cruds = [
                        sc for sc in submodule_crud_list 
                        if sc.submodule_access_id == submodule.id
                    ]
                    
                    for submodule_crud in submodule_cruds:
                        crud_data = {
                            "id": submodule_crud.id,
                            "name": submodule_crud.name,
                            "status": True if target_role_id == 1 else (
                                any(ua.submodule_crud_access_id == submodule_crud.id for ua in user_access_list)
                            )
                        }
                        submodule_data["sub_module_crud"].append(crud_data)
                    
                    submodule_result.append(submodule_data)
                
                role_access_data["sub_module"] = submodule_result
            else:
                # If no submodules, check for direct submodule_crud
                direct_cruds = [
                    sc for sc in submodule_crud_list 
                    if sc.role_access_id == role_access.id
                ]
                
                if direct_cruds:
                    crud_result = []
                    for crud in direct_cruds:
                        crud_data = {
                            "id": crud.id,
                            "name": crud.name,
                            "status": True if target_role_id == 1 else (
                                any(ua.submodule_crud_access_id == crud.id for ua in user_access_list)
                            )
                        }
                        crud_result.append(crud_data)
                    role_access_data["sub_module_crud"] = crud_result
            
            result.append(role_access_data)
        
        return {
            "status": 200,
            "message": "Data found successfully.",
            "data": result
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.get("/user_role_access", response_model=RoleAccessResponse)
def get_user_role_access_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get current user's role access for dashboard
    Returns nested structure: role_access -> submodule -> submodule_crud
    Includes hardcoded Dashboard entry with id: 20
    """
    try:
        user = current_user
        
        # Get role_id mapping
        role_id_map = {
            UserRole.admin: 1,
            UserRole.subadmin: 2,
            UserRole.business_head: 3,
            UserRole.regional_manager: 4,
            UserRole.sales_team: 5,
            UserRole.key_account_manager: 9,
            UserRole.teacher: 6
        }
        role_id = role_id_map.get(user.role, 1)
        
        # Get role access based on user role
        role_access_query = db.query(RoleAccessMaster).order_by(RoleAccessMaster.id)
        submodule_query = db.query(SubModuleMaster)
        
        # Apply role-based filtering
        if role_id in [1, 2]:  # Admin or SubAdmin
            # No filtering for role_access, get all submodules
            pass
        elif role_id == 2:  # SubAdmin
            # Get all role access, all submodules
            pass
        elif role_id == 3:  # Business Head
            # Get all role access, all submodules
            pass
        elif role_id == 4:  # Regional Manager
            # Get all role access, all submodules
            pass
        elif role_id == 9:  # Key Account Manager
            # Get all role access, all submodules
            pass
        elif role_id == 5:  # Sales Team
            # Get all role access, all submodules
            pass
        
        # Get all data
        role_access_list = role_access_query.all()
        submodule_list = submodule_query.all()
        submodule_crud_list = db.query(SubModuleCRUDMaster).all()
        user_access_list = db.query(MapRolesAccessToSubAdmin).filter(
            MapRolesAccessToSubAdmin.user_id == user.id
        ).all()
        
        # Build result list - start with Dashboard entry
        result = [{
            "id": 20,
            "title": "Dashboard",
            "sub_module": [],
            "status": True
        }]
        
        # Process each role access
        for role_access in role_access_list:
            role_access_data = {
                "id": role_access.id,
                "title": role_access.access,
                "sub_module": [],
                "sub_module_crud": None
            }
            
            # Get submodules for this role_access
            submodules = [sm for sm in submodule_list if sm.role_access_id == role_access.id]
            
            if submodules:
                submodule_result = []
                for submodule in submodules:
                    submodule_data = {
                        "id": submodule.id,
                        "name": submodule.name,
                        "sub_module_crud": []
                    }
                    
                    # Get submodule CRUDs
                    submodule_cruds = [
                        sc for sc in submodule_crud_list 
                        if sc.submodule_access_id == submodule.id
                    ]
                    
                    for submodule_crud in submodule_cruds:
                        crud_data = {
                            "id": submodule_crud.id,
                            "name": submodule_crud.name,
                            "status": True if role_id == 1 else (
                                any(ua.submodule_crud_access_id == submodule_crud.id for ua in user_access_list)
                            )
                        }
                        submodule_data["sub_module_crud"].append(crud_data)
                    
                    # Set submodule status
                    if role_id in [2, 3, 4, 5, 9]:
                        submodule_data["status"] = any(
                            ua.submodule_access_id == submodule.id for ua in user_access_list
                        )
                    else:
                        submodule_data["status"] = True
                    
                    submodule_result.append(submodule_data)
                
                role_access_data["sub_module"] = submodule_result
            else:
                # If no submodules, check for direct submodule_crud
                direct_cruds = [
                    sc for sc in submodule_crud_list 
                    if sc.role_access_id == role_access.id
                ]
                
                if direct_cruds:
                    crud_result = []
                    for crud in direct_cruds:
                        crud_data = {
                            "id": crud.id,
                            "name": crud.name,
                            "status": True if role_id == 1 else (
                                any(ua.submodule_crud_access_id == crud.id for ua in user_access_list)
                            )
                        }
                        crud_result.append(crud_data)
                    role_access_data["sub_module_crud"] = crud_result
            
            # Set role access status
            if role_id in [2, 3, 4, 5, 9]:
                role_access_data["status"] = any(
                    ua.access_id == role_access.id for ua in user_access_list
                )
            else:
                role_access_data["status"] = True
            
            result.append(role_access_data)
        
        return {
            "status": 200,
            "message": "Data found successfully.",
            "data": result
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional, List, Dict, Any
from app.dependencies import get_current_user
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
   
    try:
        # Placeholder data - Replace with actual RoleAccessMaster model query
        # For now, returning sample data structure
        
        # Example query (uncomment when RoleAccessMaster model is created):
        # queryset = db.query(RoleAccessMaster).all()
        # data = [{"id": item.id, "access": item.access} for item in queryset]
        
        # Sample data structure
        data = [
            {"id": 1, "access": "User Management"},
            {"id": 2, "access": "Dashboard Access"},
            {"id": 3, "access": "Reports Access"},
            {"id": 4, "access": "Settings Access"}
        ]
        
        # Apply search filter if provided
        if search:
            search_term = search.strip()
            search_pattern = re.escape(search_term)
            data = [
                item for item in data
                if re.search(search_pattern, item.get("access", ""), re.IGNORECASE)
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

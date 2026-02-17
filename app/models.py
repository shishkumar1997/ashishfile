from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum
from datetime import datetime


class UserRole(str, enum.Enum):
    admin = "Admin"
    subadmin = "SubAdmin"
    business_head = "Business Head"
    regional_manager = "Regional Manager"
    key_account_manager = "Key Account Manager"
    sales_team = "Sales Team"
    teacher = "Teacher"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)


class RoleAccessMaster(Base):
    __tablename__ = "roles_access_master"

    id = Column(Integer, primary_key=True, index=True)
    access = Column(String(50), nullable=False)
    status1 = Column(Boolean, default=True)
    status2 = Column(Boolean, default=True)
    status3 = Column(Boolean, default=True)
    status4 = Column(Boolean, default=True)
    status5 = Column(Boolean, default=True)
    status9 = Column(Boolean, default=True)
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, server_default=func.now())

    # Relationships
    created_by = relationship("User", foreign_keys=[created_by_id], backref="role_access_registered_by")
    updated_by = relationship("User", foreign_keys=[updated_by_id], backref="role_access_modified_by")


class SubModuleMaster(Base):
    __tablename__ = "submodule_master"

    id = Column(Integer, primary_key=True, index=True)
    role_access_id = Column(Integer, ForeignKey("roles_access_master.id"), nullable=True)
    name = Column(String(50), nullable=False)
    status1 = Column(Boolean, default=True)
    status2 = Column(Boolean, default=True)
    status3 = Column(Boolean, default=True)
    status4 = Column(Boolean, default=True)
    status5 = Column(Boolean, default=True)
    status9 = Column(Boolean, default=True)
    created_on = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, server_default=func.now())

    # Relationships
    role_access = relationship("RoleAccessMaster", backref="submodules")


class SubModuleCRUDMaster(Base):
    __tablename__ = "submodule_crud_master"

    id = Column(Integer, primary_key=True, index=True)
    role_access_id = Column(Integer, ForeignKey("roles_access_master.id"), nullable=True)
    submodule_access_id = Column(Integer, ForeignKey("submodule_master.id"), nullable=True)
    name = Column(String(50), nullable=False)
    status1 = Column(Boolean, default=True)
    status2 = Column(Boolean, default=True)
    status3 = Column(Boolean, default=True)
    status4 = Column(Boolean, default=True)
    status5 = Column(Boolean, default=True)
    status9 = Column(Boolean, default=True)
    created_on = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, server_default=func.now())

    # Relationships
    role_access = relationship("RoleAccessMaster", backref="submodule_cruds")
    submodule_access = relationship("SubModuleMaster", backref="crud_accesses")


class MapRolesAccessToSubAdmin(Base):
    __tablename__ = "map_role_access_to_subadmin"
    __table_args__ = (
        Index('idx_access_user', 'access_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, index=True)
    access_id = Column(Integer, ForeignKey("roles_access_master.id"), nullable=True)
    submodule_access_id = Column(Integer, ForeignKey("submodule_master.id"), nullable=True)
    submodule_crud_access_id = Column(Integer, ForeignKey("submodule_crud_master.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow, server_default=func.now(), nullable=True)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, server_default=func.now())

    # Relationships
    access = relationship("RoleAccessMaster", backref="mapped_subadmins")
    submodule_access = relationship("SubModuleMaster", backref="mapped_subadmins")
    submodule_crud_access = relationship("SubModuleCRUDMaster", backref="mapped_subadmins")
    user = relationship("User", backref="role_access_mappings")

from sqlalchemy import Column, Integer, String, Enum
# from database import Base
from app.database import Base
# from app.models import User


import enum


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

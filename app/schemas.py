from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import Optional, List, Dict, Any
from app.models import UserRole


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    remember_me: Optional[bool] = False


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    status: int
    message: str
    access_token: str
    token_type: str


class WebLoginResponse(BaseModel):
    status: int
    message: str
    data: Dict[str, Any]


class ForgetPasswordRequest(BaseModel):
    email: EmailStr


class ForgetPasswordResponse(BaseModel):
    status: int
    message: str
    data: Optional[str] = None


class ChangePasswordRequest(BaseModel):
    token: str
    new_password: str
    confirm_password: str


class ChangePasswordResponse(BaseModel):
    status: int
    message: str


class ProfileGetResponse(BaseModel):
    status: int
    message: str
    data: Dict[str, Any]


class ProfileUpdateRequest(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None


class ProfileUpdateResponse(BaseModel):
    status: int
    message: str
    data: Dict[str, Any]


class RoleAccessResponse(BaseModel):
    status: int
    message: str
    data: List[Dict[str, Any]]


class DashboardCountResponse(BaseModel):
    status: int
    message: str
    data: Dict[str, Any]


class RefreshTokenRequest(BaseModel):
    access_token: str


class RefreshTokenResponse(BaseModel):
    status: int
    message: str
    data: Dict[str, Any]

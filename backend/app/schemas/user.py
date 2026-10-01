from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str


class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: str
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    is_active: bool | None = None
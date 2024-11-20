from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from jose import jwt

from app.core.config import get_settings
from app.core.auth import get_password_hash, verify_password
from app.models.user import User
from app.models.enums import UserRole, ROLE_HIERARCHY
from app.schemas.auth import TokenData

settings = get_settings()

def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(user: User) -> str:
    token_data = TokenData(
        user_id=user.id,
        tenant_id=user.tenant_id,
        role=user.role
    )
    
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        "exp": expire,
        "sub": str(token_data.user_id),
        "tenant_id": token_data.tenant_id,
        "role": token_data.role
    }
    
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_user(
    db: Session,
    *,
    email: str,
    username: str,
    password: str,
    role: UserRole,
    tenant_id: int,
    created_by_role: UserRole
) -> User:
    # Check if the creating user has sufficient privileges
    if ROLE_HIERARCHY[created_by_role] <= ROLE_HIERARCHY[role]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient privileges to create user with this role"
        )
    
    # Check if email already exists
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Check if username already exists
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    user = User(
        email=email,
        username=username,
        hashed_password=get_password_hash(password),
        role=role,
        tenant_id=tenant_id
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def check_permission(required_role: UserRole, user_role: UserRole) -> bool:
    return ROLE_HIERARCHY[user_role] >= ROLE_HIERARCHY[required_role]
from typing import Optional, Callable
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.api.deps import get_db
from app.models.user import User
from app.models.enums import UserRole, ROLE_HIERARCHY
from app.services.auth import check_permission

settings = get_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    return user

def require_role(required_role: UserRole) -> Callable:
    async def role_checker(
        current_user: User = Depends(get_current_user)
    ) -> User:
        if not check_permission(required_role, current_user.role):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role {required_role} or higher required"
            )
        return current_user
    return role_checker

# Convenience dependencies for common role checks
require_super_admin = require_role(UserRole.SUPER_ADMIN)
require_school_admin = require_role(UserRole.SCHOOL_ADMIN)
require_teacher = require_role(UserRole.TEACHER)
require_student = require_role(UserRole.STUDENT)
require_parent = require_role(UserRole.PARENT)
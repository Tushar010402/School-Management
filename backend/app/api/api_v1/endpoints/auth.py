from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.security import get_current_user, require_school_admin
from app.schemas.auth import Token, RegisterUser
from app.services.auth import authenticate_user, create_access_token, create_user
from app.models.user import User

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(user)
    return Token(access_token=access_token)

@router.post("/register", response_model=None)
async def register(
    user_data: RegisterUser,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_school_admin)
) -> dict:
    """
    Register a new user (requires school_admin or higher role)
    """
    user = create_user(
        db,
        email=user_data.email,
        username=user_data.username,
        password=user_data.password,
        role=user_data.role,
        tenant_id=user_data.tenant_id,
        created_by_role=current_user.role
    )
    
    return {"message": "User created successfully", "user_id": user.id}

@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user)) -> dict:
    """
    Logout endpoint (client should discard the token)
    """
    return {"message": "Successfully logged out"}
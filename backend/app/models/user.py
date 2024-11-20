from sqlalchemy import Column, String, Integer, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
from app.models.enums import UserRole

class User(BaseModel):
    __tablename__ = "users"

    tenant_id = Column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False)
    is_active = Column(SQLAlchemyEnum(bool), default=True, nullable=False)
    
    # Relationships
    tenant = relationship("Tenant", back_populates="users")
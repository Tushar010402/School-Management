from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum as SQLAlchemyEnum, Date
from sqlalchemy.orm import relationship
from datetime import date
from enum import Enum
from app.models.base import BaseModel

class FeeType(str, Enum):
    TUITION = "tuition"
    LIBRARY = "library"
    LABORATORY = "laboratory"
    SPORTS = "sports"
    TRANSPORT = "transport"
    OTHER = "other"

class PaymentInterval(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    PARTIALLY_PAID = "partially_paid"

class FeeStructure(BaseModel):
    __tablename__ = "fee_structures"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    fee_type = Column(SQLAlchemyEnum(FeeType), nullable=False)
    amount = Column(Float, nullable=False)
    interval = Column(SQLAlchemyEnum(PaymentInterval), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    academic_year = Column(String, nullable=False)
    
    # Relationships
    school = relationship("School", back_populates="fee_structures")
    fee_discounts = relationship("FeeDiscount", back_populates="fee_structure")
    fee_transactions = relationship("FeeTransaction", back_populates="fee_structure")

class FeeDiscount(BaseModel):
    __tablename__ = "fee_discounts"

    fee_structure_id = Column(Integer, ForeignKey("fee_structures.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Float, nullable=False)
    reason = Column(String, nullable=False)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    approved_at = Column(Date, nullable=False, default=date.today)
    
    # Relationships
    fee_structure = relationship("FeeStructure", back_populates="fee_discounts")
    student = relationship("User", foreign_keys=[student_id])
    approver = relationship("User", foreign_keys=[approved_by])

class FeeTransaction(BaseModel):
    __tablename__ = "fee_transactions"

    fee_structure_id = Column(Integer, ForeignKey("fee_structures.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False, default=date.today)
    transaction_id = Column(String, unique=True, nullable=False)
    payment_method = Column(String, nullable=False)
    status = Column(SQLAlchemyEnum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    remarks = Column(String, nullable=True)
    
    # Relationships
    fee_structure = relationship("FeeStructure", back_populates="fee_transactions")
    student = relationship("User")
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Date, Enum as SQLAlchemyEnum, JSON
from sqlalchemy.orm import relationship
from enum import Enum
from app.models.base import BaseModel

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class BloodGroup(str, Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"

class StudentProfile(BaseModel):
    __tablename__ = "student_profiles"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    admission_number = Column(String(50), nullable=False)
    admission_date = Column(Date, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(SQLAlchemyEnum(Gender), nullable=False)
    blood_group = Column(SQLAlchemyEnum(BloodGroup), nullable=True)
    address = Column(String(500), nullable=False)
    phone = Column(String(20), nullable=True)
    emergency_contact = Column(String(20), nullable=False)
    medical_conditions = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Additional fields
    previous_school = Column(String(200), nullable=True)
    transfer_certificate = Column(String(200), nullable=True)  # Document URL
    documents = Column(JSON, nullable=True)  # Store document URLs and metadata
    
    # Relationships
    user = relationship("User", back_populates="student_profile")
    guardians = relationship("Guardian", back_populates="student")
    attendance = relationship("StudentAttendance", back_populates="student")
    fees = relationship("StudentFee", back_populates="student")

class Guardian(BaseModel):
    __tablename__ = "guardians"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    relationship = Column(String(50), nullable=False)  # father, mother, guardian
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    occupation = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)
    address = Column(String(500), nullable=True)
    is_emergency_contact = Column(Boolean, default=False)
    is_authorized_pickup = Column(Boolean, default=False)
    
    # Relationships
    student = relationship("StudentProfile", back_populates="guardians")
    user = relationship("User", back_populates="guardian")

class StudentAttendance(BaseModel):
    __tablename__ = "student_attendance"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)  # present, absent, late, excused
    remarks = Column(String(200), nullable=True)
    marked_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    student = relationship("StudentProfile", back_populates="attendance")
    section = relationship("Section")
    teacher = relationship("User")

class StudentDocument(BaseModel):
    __tablename__ = "student_documents"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False)
    document_type = Column(String(50), nullable=False)  # birth_certificate, transfer_certificate, etc.
    document_url = Column(String(500), nullable=False)
    file_name = Column(String(200), nullable=False)
    file_size = Column(Integer, nullable=False)  # in bytes
    mime_type = Column(String(100), nullable=False)
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_verified = Column(Boolean, default=False)
    verified_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    verification_date = Column(Date, nullable=True)
    
    # Relationships
    student = relationship("StudentProfile")
    uploader = relationship("User", foreign_keys=[uploaded_by])
    verifier = relationship("User", foreign_keys=[verified_by])

class StudentNote(BaseModel):
    __tablename__ = "student_notes"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False)
    note_type = Column(String(50), nullable=False)  # academic, behavioral, medical, etc.
    title = Column(String(200), nullable=False)
    content = Column(String(1000), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_confidential = Column(Boolean, default=False)
    
    # Relationships
    student = relationship("StudentProfile")
    author = relationship("User")

# Add relationships to User model
from app.models.user import User
User.student_profile = relationship("StudentProfile", back_populates="user", uselist=False)
User.guardian = relationship("Guardian", back_populates="user", uselist=False)

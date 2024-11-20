from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum, DateTime, Boolean
from sqlalchemy.orm import relationship
from enum import Enum
from datetime import datetime
from app.models.base import BaseModel

class AssignmentStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CLOSED = "closed"

class SubmissionStatus(str, Enum):
    PENDING = "pending"
    SUBMITTED = "submitted"
    LATE = "late"
    GRADED = "graded"
    RESUBMIT = "resubmit"

class Assignment(BaseModel):
    __tablename__ = "assignments"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    due_date = Column(DateTime, nullable=False)
    max_score = Column(Integer, nullable=False)
    file_url = Column(String, nullable=True)
    status = Column(SQLAlchemyEnum(AssignmentStatus), nullable=False, default=AssignmentStatus.DRAFT)
    allow_late_submission = Column(Boolean, default=False)
    
    # Relationships
    school = relationship("School")
    teacher = relationship("User", foreign_keys=[teacher_id])
    submissions = relationship("AssignmentSubmission", back_populates="assignment")

class AssignmentSubmission(BaseModel):
    __tablename__ = "assignment_submissions"

    assignment_id = Column(Integer, ForeignKey("assignments.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    submission_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    file_url = Column(String, nullable=True)
    comments = Column(String, nullable=True)
    score = Column(Integer, nullable=True)
    status = Column(SQLAlchemyEnum(SubmissionStatus), nullable=False, default=SubmissionStatus.PENDING)
    feedback = Column(String, nullable=True)
    
    # Relationships
    assignment = relationship("Assignment", back_populates="submissions")
    student = relationship("User")
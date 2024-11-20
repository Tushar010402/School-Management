from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum, Date, Time, Boolean
from sqlalchemy.orm import relationship
from enum import Enum
from datetime import date, time
from app.models.base import BaseModel

class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    EXCUSED = "excused"
    HALF_DAY = "half_day"

class AttendanceSession(BaseModel):
    __tablename__ = "attendance_sessions"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=True)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    session_start = Column(Time, nullable=False)
    session_end = Column(Time, nullable=False)
    is_completed = Column(Boolean, default=False)
    
    # Relationships
    school = relationship("School")
    teacher = relationship("User")
    attendance_records = relationship("AttendanceRecord", back_populates="session")

class AttendanceRecord(BaseModel):
    __tablename__ = "attendance_records"

    session_id = Column(Integer, ForeignKey("attendance_sessions.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status = Column(SQLAlchemyEnum(AttendanceStatus), nullable=False)
    remarks = Column(String, nullable=True)
    late_minutes = Column(Integer, nullable=True)
    
    # Relationships
    session = relationship("AttendanceSession", back_populates="attendance_records")
    student = relationship("User")
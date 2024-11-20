from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum as SQLAlchemyEnum, Time, JSON
from sqlalchemy.orm import relationship
from enum import Enum
from datetime import time
from app.models.base import BaseModel

class WeekDay(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

class GradeSystem(str, Enum):
    PERCENTAGE = "percentage"
    LETTER = "letter"
    GPA = "gpa"
    CUSTOM = "custom"

class AssessmentType(str, Enum):
    TEST = "test"
    ASSIGNMENT = "assignment"
    PROJECT = "project"
    EXAM = "exam"
    QUIZ = "quiz"
    PRACTICAL = "practical"

class Timetable(BaseModel):
    __tablename__ = "timetables"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    day = Column(SQLAlchemyEnum(WeekDay), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    room = Column(String, nullable=True)
    is_active = Column(SQLAlchemyEnum(bool), default=True, nullable=False)
    
    # Relationships
    school = relationship("School", back_populates="timetables")
    teacher = relationship("User")
    subject = relationship("Subject")

class GradingSystem(BaseModel):
    __tablename__ = "grading_systems"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    type = Column(SQLAlchemyEnum(GradeSystem), nullable=False)
    scale = Column(JSON, nullable=False)  # Store grading scale as JSON
    passing_grade = Column(Float, nullable=False)
    
    # Relationships
    school = relationship("School", back_populates="grading_systems")
    assessments = relationship("Assessment", back_populates="grading_system")

class Assessment(BaseModel):
    __tablename__ = "assessments"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    grading_system_id = Column(Integer, ForeignKey("grading_systems.id"), nullable=False)
    name = Column(String, nullable=False)
    type = Column(SQLAlchemyEnum(AssessmentType), nullable=False)
    total_marks = Column(Float, nullable=False)
    weightage = Column(Float, nullable=False)  # Percentage weightage in final result
    description = Column(String, nullable=True)
    
    # Relationships
    school = relationship("School", back_populates="assessments")
    teacher = relationship("User")
    subject = relationship("Subject")
    grading_system = relationship("GradingSystem", back_populates="assessments")
    results = relationship("Result", back_populates="assessment")

class Result(BaseModel):
    __tablename__ = "results"

    assessment_id = Column(Integer, ForeignKey("assessments.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    marks_obtained = Column(Float, nullable=False)
    remarks = Column(String, nullable=True)
    
    # Relationships
    assessment = relationship("Assessment", back_populates="results")
    student = relationship("User")

class TeacherNote(BaseModel):
    __tablename__ = "teacher_notes"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    file_url = Column(String, nullable=True)
    
    # Relationships
    school = relationship("School")
    teacher = relationship("User")
    subject = relationship("Subject")
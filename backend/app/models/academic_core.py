from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class AcademicYear(BaseModel):
    __tablename__ = "academic_years"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    school = relationship("School", back_populates="academic_years")
    classes = relationship("Class", back_populates="academic_year")

    __table_args__ = (
        CheckConstraint('end_date > start_date', name='check_academic_year_dates'),
    )

class Class(BaseModel):
    __tablename__ = "classes"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    academic_year_id = Column(Integer, ForeignKey("academic_years.id"), nullable=False)
    name = Column(String, nullable=False)
    grade_level = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    school = relationship("School", back_populates="classes")
    academic_year = relationship("AcademicYear", back_populates="classes")
    sections = relationship("Section", back_populates="class_")

class Section(BaseModel):
    __tablename__ = "sections"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    school = relationship("School", back_populates="sections")
    class_ = relationship("Class", back_populates="sections")
    student_sections = relationship("StudentSection", back_populates="section")
    teacher_sections = relationship("TeacherSection", back_populates="section")

class Subject(BaseModel):
    __tablename__ = "subjects"

    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    description = Column(String, nullable=True)
    credits = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    school = relationship("School", back_populates="subjects")
    teacher_sections = relationship("TeacherSection", back_populates="subject")

class StudentSection(BaseModel):
    __tablename__ = "student_sections"

    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="CASCADE"), nullable=False)
    roll_number = Column(String, nullable=True)

    # Relationships
    student = relationship("User", foreign_keys=[student_id])
    section = relationship("Section", back_populates="student_sections")

class TeacherSection(BaseModel):
    __tablename__ = "teacher_sections"

    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="CASCADE"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    is_class_teacher = Column(Boolean, default=False, nullable=False)

    # Relationships
    teacher = relationship("User", foreign_keys=[teacher_id])
    section = relationship("Section", back_populates="teacher_sections")
    subject = relationship("Subject", back_populates="teacher_sections")
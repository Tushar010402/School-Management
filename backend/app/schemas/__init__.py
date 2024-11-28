from app.schemas.tenant import TenantCreate, TenantUpdate, TenantInDB
from app.schemas.school import SchoolCreate, SchoolUpdate, SchoolInDB
from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.schemas.academic import (
    AcademicYear, AcademicYearCreate, AcademicYearUpdate,
    Class, ClassCreate, ClassUpdate,
    Section, SectionCreate, SectionUpdate,
    Subject, SubjectCreate, SubjectUpdate,
    StudentSection, StudentSectionCreate,
    TeacherSection, TeacherSectionCreate,
    TimetableBase, TimetableCreate, TimetableUpdate, TimetableInDB,
    GradingSystemBase, GradingSystemCreate, GradingSystemUpdate, GradingSystemInDB,
    AssessmentBase, AssessmentCreate, AssessmentUpdate, AssessmentInDB,
    ResultBase, ResultCreate, ResultUpdate, ResultInDB,
    TeacherNoteBase, TeacherNoteCreate, TeacherNoteUpdate, TeacherNoteInDB,
    StudentResult
)

__all__ = [
    # Tenant
    "TenantCreate", "TenantUpdate", "TenantInDB",
    # School
    "SchoolCreate", "SchoolUpdate", "SchoolInDB",
    # User
    "UserCreate", "UserUpdate", "UserInDB",
    # Academic
    "AcademicYear", "AcademicYearCreate", "AcademicYearUpdate",
    "Class", "ClassCreate", "ClassUpdate",
    "Section", "SectionCreate", "SectionUpdate",
    "Subject", "SubjectCreate", "SubjectUpdate",
    "StudentSection", "StudentSectionCreate",
    "TeacherSection", "TeacherSectionCreate",
    # Timetable
    "TimetableBase", "TimetableCreate", "TimetableUpdate", "TimetableInDB",
    # Grading
    "GradingSystemBase", "GradingSystemCreate", "GradingSystemUpdate", "GradingSystemInDB",
    # Assessment
    "AssessmentBase", "AssessmentCreate", "AssessmentUpdate", "AssessmentInDB",
    # Result
    "ResultBase", "ResultCreate", "ResultUpdate", "ResultInDB",
    # Teacher Notes
    "TeacherNoteBase", "TeacherNoteCreate", "TeacherNoteUpdate", "TeacherNoteInDB",
    # Student Results
    "StudentResult"
]
from pydantic import BaseModel, Field, validator
from datetime import time
from typing import Optional, List, Dict, Union
from app.models.academic import WeekDay, GradeSystem, AssessmentType
from app.schemas.base import TimestampSchema

class TimetableBase(BaseModel):
    class_id: int
    section_id: Optional[int] = None
    subject_id: int
    teacher_id: int
    day: WeekDay
    start_time: time
    end_time: time
    room: Optional[str] = None

    @validator('end_time')
    def end_time_must_be_after_start_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError('end_time must be after start_time')
        return v

class TimetableCreate(TimetableBase):
    school_id: int

class TimetableUpdate(TimetableBase):
    is_active: Optional[bool] = None

class TimetableInDB(TimetableBase, TimestampSchema):
    id: int
    school_id: int
    is_active: bool

class GradingSystemBase(BaseModel):
    name: str
    type: GradeSystem
    scale: Dict[str, Union[float, str]]  # Example: {"A": 90, "B": 80} or {"4.0": "Excellent"}
    passing_grade: float

class GradingSystemCreate(GradingSystemBase):
    school_id: int

class GradingSystemUpdate(GradingSystemBase):
    pass

class GradingSystemInDB(GradingSystemBase, TimestampSchema):
    id: int
    school_id: int

class AssessmentBase(BaseModel):
    class_id: int
    section_id: Optional[int] = None
    subject_id: int
    teacher_id: int
    grading_system_id: int
    name: str
    type: AssessmentType
    total_marks: float = Field(gt=0)
    weightage: float = Field(gt=0, le=100)
    description: Optional[str] = None

class AssessmentCreate(AssessmentBase):
    school_id: int

class AssessmentUpdate(AssessmentBase):
    pass

class AssessmentInDB(AssessmentBase, TimestampSchema):
    id: int
    school_id: int

class ResultBase(BaseModel):
    marks_obtained: float
    remarks: Optional[str] = None

    @validator('marks_obtained')
    def validate_marks(cls, v, values):
        if v < 0:
            raise ValueError('marks_obtained cannot be negative')
        return v

class ResultCreate(ResultBase):
    assessment_id: int
    student_id: int

class ResultUpdate(ResultBase):
    pass

class ResultInDB(ResultBase, TimestampSchema):
    id: int
    assessment_id: int
    student_id: int

class TeacherNoteBase(BaseModel):
    class_id: int
    section_id: Optional[int] = None
    subject_id: int
    title: str
    content: str
    file_url: Optional[str] = None

class TeacherNoteCreate(TeacherNoteBase):
    school_id: int
    teacher_id: int

class TeacherNoteUpdate(TeacherNoteBase):
    pass

class TeacherNoteInDB(TeacherNoteBase, TimestampSchema):
    id: int
    school_id: int
    teacher_id: int

class StudentResult(BaseModel):
    student_id: int
    assessment_results: List[ResultInDB]
    total_percentage: float
    grade: str
    remarks: Optional[str] = None
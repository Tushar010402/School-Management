from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.security import require_teacher, get_current_user
from app.models.user import User
from app.schemas.academic import (
    TimetableCreate,
    TimetableInDB,
    GradingSystemCreate,
    GradingSystemInDB,
    AssessmentCreate,
    AssessmentInDB,
    ResultCreate,
    ResultInDB,
    TeacherNoteCreate,
    TeacherNoteInDB,
    StudentResult
)
from app.services import academic as academic_service

router = APIRouter()

# Timetable endpoints
@router.post("/timetable", response_model=TimetableInDB)
async def create_timetable(
    timetable_data: TimetableCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
) -> TimetableInDB:
    """
    Create a new timetable entry (Teacher or higher role)
    """
    if current_user.school_id != timetable_data.school_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create timetable for different school"
        )
    return academic_service.create_timetable(db, timetable_data)

@router.get("/timetable", response_model=List[TimetableInDB])
async def get_timetable(
    class_id: int | None = Query(None, description="Filter by class ID"),
    section_id: int | None = Query(None, description="Filter by section ID"),
    teacher_id: int | None = Query(None, description="Filter by teacher ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> List[TimetableInDB]:
    """
    Get timetable with optional filters
    """
    return academic_service.get_timetable(
        db,
        school_id=current_user.school_id,
        class_id=class_id,
        section_id=section_id,
        teacher_id=teacher_id
    )

# Assessment endpoints
@router.post("/assessments", response_model=AssessmentInDB)
async def create_assessment(
    assessment_data: AssessmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
) -> AssessmentInDB:
    """
    Create a new assessment (Teacher or higher role)
    """
    if current_user.school_id != assessment_data.school_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create assessment for different school"
        )
    return academic_service.create_assessment(db, assessment_data)

# Results endpoints
@router.post("/results", response_model=ResultInDB)
async def create_result(
    result_data: ResultCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
) -> ResultInDB:
    """
    Create a new result entry (Teacher only)
    """
    # Verify assessment belongs to teacher's school
    assessment = db.query(Assessment).filter(
        Assessment.id == result_data.assessment_id
    ).first()
    
    if not assessment or assessment.school_id != current_user.school_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create result for different school"
        )
    
    return academic_service.create_result(db, result_data)

@router.get("/results/student/{student_id}", response_model=List[StudentResult])
async def get_student_results(
    student_id: int,
    class_id: int | None = Query(None, description="Filter by class ID"),
    subject_id: int | None = Query(None, description="Filter by subject ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> List[StudentResult]:
    """
    Get student results with optional filters
    """
    results = academic_service.get_student_results(
        db,
        school_id=current_user.school_id,
        student_id=student_id,
        class_id=class_id,
        subject_id=subject_id
    )
    
    # Group results by subject and calculate final grades
    subject_results = {}
    for result in results:
        subject_id = result.assessment.subject_id
        if subject_id not in subject_results:
            subject_results[subject_id] = []
        subject_results[subject_id].append(result)
    
    final_results = []
    for subject_id, results in subject_results.items():
        final_percentage = academic_service.calculate_final_result(
            db,
            school_id=current_user.school_id,
            student_id=student_id,
            class_id=results[0].assessment.class_id,
            subject_id=subject_id
        )
        
        # Get grade based on grading system
        grading_system = results[0].assessment.grading_system
        grade = "N/A"
        for grade_key, min_percentage in grading_system.scale.items():
            if isinstance(min_percentage, (int, float)) and final_percentage >= min_percentage:
                grade = grade_key
                break
        
        final_results.append(
            StudentResult(
                student_id=student_id,
                assessment_results=results,
                total_percentage=final_percentage,
                grade=grade,
                remarks=f"Final grade for subject {subject_id}"
            )
        )
    
    return final_results

# Teacher notes endpoints
@router.post("/notes", response_model=TeacherNoteInDB)
async def create_teacher_note(
    note_data: TeacherNoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
) -> TeacherNoteInDB:
    """
    Create a teacher note (Teacher only)
    """
    if current_user.school_id != note_data.school_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create note for different school"
        )
    
    if current_user.id != note_data.teacher_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create note for different teacher"
        )
    
    return academic_service.create_teacher_note(db, note_data)

@router.get("/notes", response_model=List[TeacherNoteInDB])
async def get_teacher_notes(
    teacher_id: int | None = Query(None, description="Filter by teacher ID"),
    class_id: int | None = Query(None, description="Filter by class ID"),
    subject_id: int | None = Query(None, description="Filter by subject ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> List[TeacherNoteInDB]:
    """
    Get teacher notes with optional filters
    """
    return academic_service.get_teacher_notes(
        db,
        school_id=current_user.school_id,
        teacher_id=teacher_id,
        class_id=class_id,
        subject_id=subject_id
    )
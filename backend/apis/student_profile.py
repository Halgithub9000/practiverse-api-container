from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from slowapi.util import get_remote_address
from slowapi.extension import Limiter as SlowAPILimiter

from backend.services.document_operations_service import GcsDocumentOperations
from backend.services.student_profile_service import AnthropicHaikuStudentProfiler

router = APIRouter()
limiter = SlowAPILimiter(key_func=get_remote_address)


class StudentProfileRequest(BaseModel):
    blob: str


@router.post("/create")
@limiter.limit("5/minute")  # 5 solicitudes por minuto por IP
async def student_profile_endpoint(request: Request, data: StudentProfileRequest):
    try:
        gcsDocumentOperations = GcsDocumentOperations()
        pdf_text = gcsDocumentOperations.download_file(data.blob)
        print("Descarga OK")
        profiler = AnthropicHaikuStudentProfiler()
        perfil_json = profiler.generate_student_profile(pdf_text)
        return perfil_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
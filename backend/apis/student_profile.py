from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from slowapi.extension import Limiter as SlowAPILimiter
from slowapi.util import get_remote_address

from services.document_operations_service import GcsDocumentOperations, GcsDocumentOutputOperations
from services.student_profile_service import AnthropicHaikuStudentProfiler

router = APIRouter()
limiter = SlowAPILimiter(key_func=get_remote_address)


class StudentProfileRequest(BaseModel):
    blob: str


class ProfileSuggestionsRequest(BaseModel):
    interests: str
    profile: str


@router.post("/create")
@limiter.limit("5/minute")  # 5 solicitudes por minuto por IP
async def student_profile_endpoint(request: Request, data: StudentProfileRequest):
    try:
        gcsDocumentOperations = GcsDocumentOperations()
        pdf_text = gcsDocumentOperations.download_file(data.blob)
        print("Descarga OK")
        profiler = AnthropicHaikuStudentProfiler()
        perfil_json = profiler.generate_student_profile(pdf_text)

        gcsDocumentOutputOperations = GcsDocumentOutputOperations()
        gcsDocumentOutputOperations.upload_file(data=perfil_json, destination_blob_name="profile.json")
        return perfil_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/suggest")
@limiter.limit("5/minute")  # 5 solicitudes por minuto por IP
async def profile_suggestions_endpoint(request: Request, data: ProfileSuggestionsRequest):
    try:
        gcsDocumentOperations = GcsDocumentOutputOperations()
        pdf_text = gcsDocumentOperations.download_file(data.profile)
        print("Descarga OK")
        profiler = AnthropicHaikuStudentProfiler()
        perfil_json = profiler.suggest_improvements(pdf_text, data.interests)
        return perfil_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

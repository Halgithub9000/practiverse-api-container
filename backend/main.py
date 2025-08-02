from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from .apis.document_operations import router as document_operations_router
from .apis.student_profile import router as student_profile_router

app = FastAPI()

# Configuración de CORS (ajusta los orígenes según tus necesidades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# Importa y registra los routers de tus APIs

app.include_router(student_profile_router, prefix="/api/student-profile")
app.include_router(document_operations_router, prefix="/api/documents")

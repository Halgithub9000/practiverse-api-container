from fastapi import APIRouter, HTTPException
from fastapi import UploadFile, File, Form
from dotenv import load_dotenv
from backend.services.document_operations_service import GcsDocumentOperations

import os

router = APIRouter()


@router.get("/list-all-documents")
async def list_all_documents():
    try:
        gcs_service = GcsDocumentOperations()
        documents = gcs_service.list_all_documents()
        return {"documents": documents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload-document")
async def upload_document(
    file: UploadFile = File(...),
    destination_blob_name: str = Form("cv.pdf")
):
    try:
        gcs_service = GcsDocumentOperations()
        gcs_service.upload_file(
            file, destination_blob_name)
        return {"message": f"Archivo '{destination_blob_name}' subido correctamente a GCS."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
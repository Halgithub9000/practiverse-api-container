import os
from typing import Protocol

import fitz  # PyMuPDF
from dotenv import load_dotenv
from google.cloud import storage


class DocumentOperationsService(Protocol):

    def list_all_documents(self) -> list[str]: ...

    def download_file(self, blob_name: str) -> str: ...

    def upload_file(self, file, destination_blob_name: str) -> None: ...


class GcsDocumentOperations(DocumentOperationsService):
    def __init__(self):
        load_dotenv()
        self.bucket_name = os.getenv("GCS_BUCKET_NAME")
        self.client = storage.Client()

    def list_all_documents(self) -> list[str]:
        if not self.bucket_name:
            raise EnvironmentError("GCS_BUCKET_NAME no está configurado en las variables de entorno.")
        try:
            bucket = self.client.bucket(self.bucket_name)
            blobs = bucket.list_blobs()
            return [blob.name for blob in blobs]
        except Exception as e:
            raise RuntimeError(f"Error al listar los documentos en GCS: {e}")

    def download_file(self, blob_name: str) -> str:
        if not self.bucket_name:
            raise EnvironmentError("No se encontró la variable de entorno GCS_BUCKET_NAME.")

        print(f"Nombre del bucket cargado desde .env: {self.bucket_name}")

        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(blob_name)
            pdf_bytes = blob.download_as_bytes()
            print(f"Archivo '{blob_name}' descargado exitosamente de GCS.")
            return self.extract_text_from_pdf_bytes(pdf_bytes)
        except Exception as e:
            raise RuntimeError(f"Error al descargar el archivo: {e}")

    def extract_text_from_pdf_bytes(self, pdf_bytes: bytes) -> str:
        if not pdf_bytes:
            raise ValueError("No se proporcionaron bytes para el archivo.")
        try:
            with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
            return text
        except Exception as e:
            raise RuntimeError(f"Error al extraer el texto del PDF: {e}")

    def upload_file(self, file, destination_blob_name: str = "cv.pdf") -> None:
        if not self.bucket_name:
            raise EnvironmentError("GCS_BUCKET_NAME no está configurado en las variables de entorno.")

        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_file(file.file, content_type=file.content_type)
        except Exception as e:
            raise RuntimeError(f"Error al subir el archivo a GCS: {e}")


class GcsDocumentOutputOperations(GcsDocumentOperations):
    def __init__(self):
        load_dotenv()
        self.bucket_name = os.getenv("GCS_BUCKET_OUTPUT_NAME")
        self.client = storage.Client()

    def download_file(self, blob_name: str) -> str:
        if not self.bucket_name:
            raise EnvironmentError("No se encontró la variable de entorno GCS_BUCKET_NAME.")

        print(f"Nombre del bucket cargado desde .env: {self.bucket_name}")

        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(blob_name)
            pdf_text = blob.download_as_text()
            print(f"Archivo '{blob_name}' descargado exitosamente de GCS.")
            return pdf_text
        except Exception as e:
            raise RuntimeError(f"Error al descargar el archivo: {e}")

    def upload_file(self, data, destination_blob_name: str = "profile.json") -> None:
        """
        Sube un JSON serializado (dict o str) como archivo a GCS.
        """
        import json

        if not self.bucket_name:
            raise EnvironmentError("GCS_BUCKET_OUTPUT_NAME no está configurado en las variables de entorno.")

        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(destination_blob_name)
            # Si es dict, serializa a string
            if isinstance(data, dict):
                data_str = json.dumps(data, ensure_ascii=False)
            else:
                data_str = str(data)
            blob.upload_from_string(data_str, content_type="application/json")
            print(f"Archivo JSON '{destination_blob_name}' subido exitosamente a GCS.")
        except Exception as e:
            raise RuntimeError(f"Error al subir el archivo JSON a GCS: {e}")

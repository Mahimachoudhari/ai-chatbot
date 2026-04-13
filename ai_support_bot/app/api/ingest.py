from fastapi import APIRouter, UploadFile, File
from app.utils import load_pdf, split_text
from app.vector_store import create_vectorstore
import app.state

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    text = load_pdf(file.file)
    chunks = split_text(text)

    vector_db = create_vectorstore(chunks)

    # 🔥 SAVE PROPERLY (IMPORTANT FIX)
    app.state.db = vector_db

    return {"message": "PDF uploaded successfully"}
from fastapi import APIRouter, UploadFile, File
from app.utils import load_pdf, split_text
from app.vector_store import create_vectorstore
import app.state as state

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        # read pdf
        text = load_pdf(file.file)

        if not text:
            return {"error": "PDF empty or unreadable"}

        # split
        chunks = split_text(text)

        # create vector store
        db = create_vectorstore(chunks)

        if db is None:
            return {"error": "Vector store creation failed"}

        state.vector_store = db

        return {"message": "PDF uploaded successfully"}

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return {"error": str(e)}
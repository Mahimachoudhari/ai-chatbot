from fastapi import APIRouter
import app.state as state
from app.rag import generate_answer

router = APIRouter()

@router.get("/ask")
def ask(query: str):

    print("VECTOR STORE:", state.vector_store)  

    if state.vector_store is None:
        return {"answer": "⚠️ Please upload PDF first"}

    return {
        "answer": generate_answer(query, state.vector_store)
    }
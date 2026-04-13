from fastapi import APIRouter
from app.rag import generate_answer
import app.state

router = APIRouter()

@router.get("/ask")
def ask(query: str):

    if app.state.db is None:
        return {"answer": "⚠️ Please upload PDF first"}

    docs = app.state.db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    return {"answer": generate_answer(context, query)}
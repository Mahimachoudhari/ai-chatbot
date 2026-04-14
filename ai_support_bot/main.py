from fastapi import FastAPI
from app.api import chat, ingest
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/ui")
def ui():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except Exception as e:
        return {"error": str(e)}

# Register routes
app.include_router(chat.router)
app.include_router(ingest.router)


@app.get("/")
def home():
    return {
        "message": "AI Chatbot is running successfully 🚀"
    }
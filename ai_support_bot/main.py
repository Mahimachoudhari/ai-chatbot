from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# routers
from app.api import chat, ingest

app = FastAPI(title="AI Customer Support Bot 🚀")

# ---------------- CORS (important for UI) ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROUTERS ----------------
app.include_router(chat.router)
app.include_router(ingest.router)

# ---------------- HOME ----------------
@app.get("/")
def home():
    return {
        "message": "AI Customer Support Bot Running 🚀",
        "status": "active"
    }

# ---------------- UI ROUTE ----------------
@app.get("/ui")
def ui():
    return FileResponse("app/index.html")
# AI Chatbot Pro (RAG + FastAPI)

A simple and powerful AI chatbot built using FastAPI, LangChain, FAISS, and HuggingFace embeddings.  
It allows users to upload PDFs and ask questions based on the document content.

---

## Features

- PDF upload and text extraction
- AI-based question answering (RAG system)
- FAISS vector database for fast retrieval
- FastAPI backend
- Simple Chat UI
- Chat history support (browser local storage)
- Typing animation in UI

---

## Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- HuggingFace Embeddings
- HTML, CSS, JavaScript

---

## Project Structure


ai-chatbot/
│
├── main.py
├── index.html
├── requirements.txt
├── app/
│ ├── api/
│ ├── rag.py
│ ├── utils.py
│ ├── vector_store.py


---

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/Mahimachoudhari/ai-chatbot.git
cd ai-chatbot
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   (Windows)
3. Install Dependencies
pip install -r requirements.txt
4. Run Server
uvicorn main:app --reload
Important Links

Backend:
http://127.0.0.1:8000/

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

Custom UI:
http://127.0.0.1:8000/ui

API Endpoints

Upload PDF:
POST /upload

Ask Question:
GET /ask?query=your_question

How It Works
User uploads PDF
Text is extracted and split into chunks
FAISS vector database is created
User asks a question
Relevant content is retrieved and AI generates answer
Example

User: What is AI automation?
Bot: AI automation refers to the use of artificial intelligence to perform tasks automatically without human intervention.

Developer

Mahima Choudhari
GitHub: https://github.com/Mahimachoudhari





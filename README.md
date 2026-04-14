# 🤖 AI Customer Support Chatbot (RAG + FastAPI + Ollama)

A powerful AI-powered customer support chatbot built using **FastAPI, LangChain, Ollama, and Vector Database (RAG system)** with a modern ChatGPT-style UI

## 🚀 Features

- 📄 Upload PDF and extract knowledge
- 🧠 AI-powered Q&A (RAG system)
- 💬 ChatGPT-like chatbot UI (Dark animated theme)
- ⚡ FastAPI backend API
- 🔍 Semantic search using embeddings
- 🤖 Ollama local LLM integration (Mistral / LLaMA3)
- 🧾 Context-based answers from documents

---

## 🖥️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Chat UI)
- **Backend:** FastAPI (Python)
- **AI Model:** Ollama (Mistral / LLaMA3)
- **Frameworks:** LangChain
- **Vector DB:** FAISS / ChromaDB (depending on setup)
- **PDF Processing:** PyPDF / LangChain loaders

---

## 📂 Project Structure

ai_support_bot/
│
├── app/
│ ├── api/
│ ├── models/
│ ├── rag.py
│ ├── vector_store.py
│ ├── ingestion.py
│ ├── memory.py
│ └── config.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

💬 How it Works
Upload PDF document
Text is converted into embeddings
Stored in vector database
User asks question
AI retrieves relevant context
LLM generates final answer
🔥 Example Queries
What is AI?


👨‍💻 Author - Mahima Choudhari





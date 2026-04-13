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


---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot


### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment
venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Run Server
uvicorn main:app --reload
🌐 Open Application
Feature	URL
Home	http://127.0.0.1:8000/

API Docs	http://127.0.0.1:8000/docs

Chat UI	http://127.0.0.1:8000/ui
💬 How it Works
Upload PDF document
Text is converted into embeddings
Stored in vector database
User asks question
AI retrieves relevant context
LLM generates final answer
🔥 Example Queries
What is AI?
Summarize my resume
What are my skills?
Explain education section
🎯 Future Improvements
🔥 Chat memory support
⚡ Streaming responses
🎤 Voice input system
🌍 Deploy on cloud
📱 Mobile responsive UI
👨‍💻 Author - Mahima Choudhari

AI Enthusiast
Full Stack Developer
Passionate about AI + Web Development
⭐ Show Your Support




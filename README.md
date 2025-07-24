
# 🧠 Agentic RAG Chatbot with Multi-format Document QA

This project is a lightweight agent-based Retrieval-Augmented Generation (RAG) chatbot that can handle document-based queries across multiple file formats (.pdf, .docx, .pptx, .csv, .txt). It utilizes an agentic architecture and integrates the **Model Context Protocol (MCP)** for structured task delegation among agents.

---

## 🚀 Features

- 📄 Multi-format document parsing (.pdf, .docx, .pptx, .csv, .txt)
- 🧠 RAG-based QA over user-uploaded documents
- 🔁 Modular agent architecture with Ingestion & Retrieval Agents
- 📜 Streamlit-based interactive UI
- 🔌 Plug-and-play integration with sentence-transformers and FAISS

---

## 🛠️ Tech Stack

| Layer            | Technology Used                   |
|------------------|-----------------------------------|
| Frontend         | Streamlit                         |
| Backend          | Python                            |
| Document Parsing | PyMuPDF (fitz), python-docx, python-pptx, pandas |
| Embeddings       | SentenceTransformers              |
| Vector DB        | FAISS                             |
| Agent Protocol   | Model Context Protocol (MCP)      |

---

## 🧩 Agent-based Architecture

- `IngestionAgent`: Parses and indexes documents into a vector database.
- `RetrievalAgent`: Handles natural language questions and retrieves relevant answers using embeddings + FAISS.

---

## 🔄 System Flow

1. User uploads documents.
2. `IngestionAgent` parses and embeds the data.
3. User asks a question.
4. `RetrievalAgent` fetches relevant chunks and generates a response.
5. UI displays the answer.

---

## 💻 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`) in your browser.

---

## 🧪 Sample Files

You can test the system by uploading any of these file types:
- `.pdf`, `.docx`, `.pptx`, `.csv`, `.txt`

---

## ❗ Challenges Faced

- Managing document parsing edge cases (like tables in PDFs)
- Ensuring sentence transformer compatibility across OS
- Streamlit upload file type handling and memory usage

---

## 🚀 Future Scope

- Integration with LangChain or LlamaIndex
- Multi-agent collaboration over task trees
- Better UI/UX with file previews and chat memory
- Support for scanned image documents via OCR

---

## 📸 UI Screenshots

(Add screenshots of your Streamlit UI here manually before submission.)

---

## 📬 Contact

For any queries, reach out at: yourname@email.com

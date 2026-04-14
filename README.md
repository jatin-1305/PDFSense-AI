# PDFSense AI: RAG-Based Multi-Document QA System using LangChain, Groq & Streamlit

## 📌 Overview
**PDFSense AI** is an AI-powered Streamlit web application that allows you to **upload multiple PDF documents and interact with them using natural language**.

The app leverages **Retrieval-Augmented Generation (RAG)** to extract, process, and retrieve relevant information from documents, and uses a **Groq-hosted LLM** to generate fast, accurate, and context-aware answers. It also includes **chat history memory**, enabling conversational interactions with your documents.

---

## 🚀 Features

- 📂 Upload **multiple PDF documents**
- 📄 Extract text from uploaded PDFs
- ✂️ Split document text into manageable chunks
- 🧠 Generate embeddings using Hugging Face models
- ⚡ Store and retrieve vectors using **FAISS**
- 💬 Ask natural-language questions about your PDFs
- 🔄 Chat interface with **latest Q&A at the top**
- 🤖 Conversational responses powered by **Groq LLM**
- 🧠 Maintains **chat history memory** for context-aware conversations

---

## 🛠️ Tech Stack

- 🐍 **Python**
- 🌐 **Streamlit** (UI)
- 🔗 **LangChain** (RAG pipeline)
- ⚡ **FAISS** (vector database)
- 📄 **PyPDF2** (PDF text extraction)
- 🤗 **Hugging Face Embeddings** (`all-MiniLM-L6-v2`)
- 🚀 **Groq LLM API** (primary LLM)
- 🔄 Optional: **OpenAI / Ollama**

---

## ⚙️ How It Works

1. 📂 Upload PDFs through the Streamlit interface  
2. 📄 Extract text using PyPDF2  
3. ✂️ Split text into smaller chunks using LangChain  
4. 🧠 Convert chunks into embeddings (Hugging Face)  
5. ⚡ Store embeddings in FAISS vector database  
6. 🔍 Retrieve relevant chunks via similarity search  
7. 🤖 Generate answers using Groq LLM  
8. 💬 Maintain chat history for follow-up questions  

---

## 📂 Project Structure

```text
PDFSense-AI/
|- app.py
|- htmlTemplates.py
|- .env
|- .gitignore
```
---
## Environment Variables

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_groq_api_key
```

Optional variables if you later switch providers:

```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACEHUB_API_KEY=your_huggingface_api_key
```

## How To Run

From the project folder:

```bash
streamlit run app.py
```

If `streamlit` is not recognized, use:

```bash
python3 -m streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

`http://localhost:8501`

## How To Use

1. Start the app.
2. Upload one or more PDF files in the sidebar.
3. Click `Process`.
4. Wait until the success message appears.
5. Ask questions about your uploaded documents.

## Current Workflow

1. PDF files are uploaded through the Streamlit sidebar.
2. `PyPDF2` extracts text from each page.
3. LangChain splits the text into chunks.
4. `HuggingFaceEmbeddings` converts chunks into vectors.
5. FAISS stores the vectors for similarity search.
6. `ConversationalRetrievalChain` uses `ChatGroq` to answer user questions with chat memory.

## Input Validation

The app currently handles a few common edge cases:

- Empty or whitespace-only questions are ignored
- Asking a question before processing PDFs shows a warning
- Clicking `Process` without uploading a PDF shows a warning
- PDFs with no extractable text show a warning
- Empty chunk generation is handled with a warning

## Notes

- The app currently uses `ChatGroq(model="llama-3.1-8b-instant", temperature=0)`.
- Scanned/image-only PDFs may not work well unless OCR is added.

## Future Improvements

- Add a `requirements.txt`
- Add OCR support for scanned PDFs
- Persist the FAISS index locally
- Show source chunks used for answers
- Add automated tests
- Clean up unused imports and older LangChain imports

## Security

- Do not commit your `.env` file.
- Keep API keys private.
- If any real API keys were exposed or shared accidentally, rotate them immediately.
  

Screenshot-
<img width="1716" height="675" alt="image" src="https://github.com/user-attachments/assets/f8e9cf04-082c-4194-9d3a-2c0900973f65" />


# PDFSense AI: RAG-Based Multi-Document QA System using LangChain, Groq & Streamlit

## 📌 Overview
**PDFSense-AI** is an AI-powered document intelligence system that enables users to interact with multiple PDF documents through a simple and intuitive web interface.

Built using **Retrieval-Augmented Generation (RAG)**, **LangChain**, and **Groq LLMs**, the system retrieves relevant information from uploaded PDFs and generates accurate, context-aware answers. It also leverages **chat history memory** to support conversational interactions.

The application is deployed with a **Streamlit UI**, making it easy to upload documents and ask questions in real time.

---

## 🚀 Features
- 📄 Upload and query **multiple PDF documents**
- 🌐 Interactive **Streamlit web interface**
- 🔍 **Semantic search** using embeddings
- 🤖 **Accurate answers using RAG architecture**
- ⚡ High-speed inference using **Groq LLMs**
- 🧠 **Chat history memory** for conversational context
- 📚 Reduced hallucination via document-grounded responses

---

## ⚙️ System Architecture

The application follows a **RAG pipeline**:

1. **Document Loading**  
   PDFs are uploaded via Streamlit and parsed  

2. **Text Chunking**  
   Documents are split into smaller chunks  

3. **Embeddings Generation**  
   Text chunks are converted into vector embeddings  

4. **Vector Store**  
   Stored in FAISS/Chroma for fast retrieval  

5. **Query Processing**  
   User queries are embedded  

6. **Similarity Search**  
   Relevant chunks are retrieved  

7. **LLM Response Generation (Groq)**  
   Context + chat history → LLM → final answer  

8. **Memory Integration**  
   Maintains conversation continuity  

---

## 🛠️ Tech Stack

- **LangChain** – LLM orchestration framework  
- **RAG (Retrieval-Augmented Generation)** – Core architecture  
- **Groq LLMs** – Fast inference engine  
- **Streamlit** – Interactive UI  
- **FAISS / Chroma** – Vector database  
- **Python** – Backend  
- **PyPDFLoader** – PDF processing  

---


Screenshot-
<img width="1716" height="675" alt="image" src="https://github.com/user-attachments/assets/f8e9cf04-082c-4194-9d3a-2c0900973f65" />


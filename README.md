# PDFSense AI (RAG-Based Multi-Document QA System using LangChain & Groq)

## 📌 Overview
**PDFSense-AI** is an AI-powered document intelligence system that enables users to interact with multiple PDF documents using natural language.

Built using **Retrieval-Augmented Generation (RAG)**, **LangChain**, and **Groq LLMs**, the system retrieves relevant context from uploaded PDFs and generates accurate, context-aware answers. It also incorporates **chat history memory**, allowing for more conversational and context-aware interactions.

---

## 🚀 Features
- 📄 Upload and query **multiple PDF documents**
- 🔍 **Semantic search** using embeddings (not keyword-based)
- 🤖 **Accurate answers using RAG architecture**
- ⚡ High-speed inference using **Groq LLMs**
- 🧠 **Chat history memory** for contextual conversations
- 📚 Reduced hallucination via document-grounded responses

---

## ⚙️ System Architecture

The application follows a **RAG pipeline**:

1. **Document Loading**  
   PDFs are ingested and parsed into raw text  

2. **Text Chunking**  
   Documents are split into smaller chunks for better retrieval  

3. **Embeddings Generation**  
   Text chunks are converted into vector embeddings  

4. **Vector Store**  
   Embeddings are stored in a vector database (FAISS/Chroma)  

5. **Query Processing**  
   User queries are embedded and matched against stored vectors  

6. **Context Retrieval**  
   Most relevant chunks are retrieved using similarity search  

7. **LLM Response Generation (Groq)**  
   Retrieved context + chat history is passed to the LLM to generate answers  

8. **Memory Integration**  
   Chat history is maintained to support follow-up questions  

---

## 🛠️ Tech Stack

- **LangChain** – LLM orchestration framework  
- **RAG (Retrieval-Augmented Generation)** – Core architecture  
- **Groq LLMs** – Fast inference for response generation  
- **FAISS** – Vector database  
- **Python** – Backend implementation  
- **PyPDFLoader** – PDF processing  

---

## 📂 Project Structure


---


Screenshot-
<img width="1718" height="981" alt="image" src="https://github.com/user-attachments/assets/14674558-237c-4808-adb8-c581d5c2b7c7" />

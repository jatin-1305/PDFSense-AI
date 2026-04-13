# PDFSense AI (LangChain)

## 📌 Overview
This project is an **AI-powered document question answering system** built using **Retrieval-Augmented Generation (RAG)** and **LangChain**. It enables users to upload multiple PDF documents and ask questions in natural language.

The system retrieves relevant information from the documents and generates **accurate, context-aware answers**, reducing hallucinations typically seen in standalone LLMs.

---

## 🚀 Features
- 📄 Supports **multiple PDF documents**
- 🔍 **Semantic search** (context-based, not keyword-based)
- 🤖 **Accurate answers using RAG pipeline**
- ⚡ Fast retrieval with **vector databases (FAISS/Chroma)**
- 🧠 Context-grounded responses using LLMs

---

## ⚙️ How It Works

1. **Document Ingestion**  
   Load and parse multiple PDF files  

2. **Text Chunking**  
   Split large documents into smaller chunks  

3. **Embeddings Generation**  
   Convert text chunks into vector embeddings  

4. **Vector Storage**  
   Store embeddings in a vector database (FAISS/Chroma)  

5. **User Query Processing**  
   Convert user query into embeddings  

6. **Similarity Search**  
   Retrieve relevant chunks based on semantic similarity  

7. **Answer Generation**  
   Use an LLM to generate answers based on retrieved context  

---

## 🛠️ Tech Stack

- **LangChain** – LLM application framework  
- **RAG (Retrieval-Augmented Generation)** – Core architecture  
- **OpenAI / LLMs** – Response generation  
- **FAISS / Chroma** – Vector database  
- **PyPDF / PDF Loaders** – Document processing  

---

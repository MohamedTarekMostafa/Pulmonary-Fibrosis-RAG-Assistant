# Pulmonary Fibrosis Research RAG Assistant 
![WhatsApp Image 2025-12-29 at 4 58 50 PM](https://github.com/user-attachments/assets/ebbb3548-55c5-4e9c-b55c-b65876131fba)))

This project is a **Retrieval-Augmented Generation (RAG)** application designed to act as an expert Biomedical Research Assistant. It focuses on technical inquiries regarding **Human Lung Organoids (hLOs)** and **Radiation-induced Pulmonary Fibrosis (RIPF)** based on specific research papers.

## 🚀 Features
* **PDF Processing:** Extracts and splits research papers into manageable chunks using LangChain.
* **Vector Database:** Uses **ChromaDB** with HuggingFace embeddings (`BAAI/bge-small-en-v1.5`) for efficient semantic search.
* **LLM Integration:** Powered by **Llama-3.3-70b** (via Groq) for high-speed and accurate medical reasoning.
* **FastAPI Backend:** A robust API to handle question-answering requests.
* **Streamlit UI:** A clean, user-friendly web interface for researchers to interact with the model.

---

## 🛠️ Tech Stack
- **Framework:** LangChain
- **LLM:** Groq (Llama-3.3-70b-versatile)
- **Embeddings:** HuggingFace (BGE model)
- **Vector Store:** ChromaDB
- **API:** FastAPI
- **Frontend:** Streamlit

---

## 📋 Prerequisites
Ensure you have a `.env` file in the root directory containing your API keys:
```env

GROQ_API_KEY=your_groq_api_key_here



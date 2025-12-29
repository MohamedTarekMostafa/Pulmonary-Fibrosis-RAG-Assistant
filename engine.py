from chromadb import EmbeddingFunction
from torch import embedding
import processor as poc
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv(".env")
def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(model_name = 'BAAI/bge-small-en-v1.5')
    presist_dir = './chroma_db'
    split = poc.get_split()
    llm  = ChatGroq(
        model = 'llama-3.3-70b-versatile',
        max_tokens = 512,
        temperature=0
    )
    vector_store = Chroma(
        embedding_function = embeddings,
        persist_directory=presist_dir,
    )
    retriever = vector_store.as_retriever(search_kwargs ={"k":5})
    template = """ 
You are an expert Biomedical Research Assistant. Your task is to provide accurate, 
technical, and concise answers based strictly on the provided research context 
regarding Human Lung Organoids (hLOs) and Radiation-induced Pulmonary Fibrosis (RIPF).

Guidelines:
1. Use technical terminology (e.g., hESC-derived, epithelial-mesenchymal transition, profibrotic cytokines).
2. If the answer involves data or findings (like the effect of Pirfenidone), cite them clearly from the context.
3. If the user asks a question that cannot be answered using the provided research paper, 
   state that the information is not available in the current document.
4. Maintain a formal, academic tone.

Context:
{Context}

Question: 
{Question}

Answer:

    """
    prompt = PromptTemplate.from_template(template)

    chain = ({"Context":retriever,"Question":RunnablePassthrough()}|prompt|llm|StrOutputParser())
    return chain
    

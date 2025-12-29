#splitting pdf ->loader
import langchain 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def get_split():
    loader = PyPDFLoader(file_path='research.pdf')
    pages= loader.load()
    splits = RecursiveCharacterTextSplitter(
        chunk_size = 1200,
        chunk_overlap = 200,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splits.split_documents(pages)
    return chunks

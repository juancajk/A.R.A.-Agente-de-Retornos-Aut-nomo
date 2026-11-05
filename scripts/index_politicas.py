"""Script para indexar políticas en ChromaDB con Sentence Transformers (Local)."""
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def crear_vectorstore():
    os.makedirs('data/chroma_db', exist_ok=True)
    
    loader = TextLoader("data/politicas.md", encoding="utf-8")
    docs = loader.load()
    
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    Chroma.from_documents(chunks, embeddings, persist_directory="data/chroma_db")
    print("Base vectorial ChromaDB generada exitosamente con sentence-transformers.")

if __name__ == "__main__":
    crear_vectorstore()
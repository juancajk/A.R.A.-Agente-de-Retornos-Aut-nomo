"""Tool: búsqueda de políticas mediante RAG (ChromaDB) local."""
from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

@tool
def buscar_casos_similares(consulta: str) -> dict:
    """Busca en las políticas de la empresa cómo resolver un caso dudoso o complejo."""
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="data/chroma_db", embedding_function=embeddings)
    
    docs = db.similarity_search(consulta, k=1)
    
    if docs:
        return {"encontrado": True, "politica": docs[0].page_content}
    return {"encontrado": False, "politica": "No se encontraron políticas relevantes."}
"""Memoria a corto plazo para Streamlit."""
from langchain.memory import ConversationBufferMemory

def obtener_memoria_sesion():
    """Devuelve el buffer de conversación para la UI."""
    return ConversationBufferMemory(return_messages=True, memory_key="chat_history")
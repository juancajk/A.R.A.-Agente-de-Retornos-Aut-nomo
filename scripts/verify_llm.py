"""Script de verificación de conexión con Gemini."""
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GOOGLE_API_KEY, LLM_MODEL

if __name__ == "__main__":
    llm = ChatGoogleGenerativeAI(model=LLM_MODEL, google_api_key=GOOGLE_API_KEY)
    response = llm.invoke("Di exactamente: Hola desde Gemini")
    print(response.content)
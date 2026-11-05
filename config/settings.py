import os
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash")
DB_PATH = "data/techstore.db"
DIAS_PLAZO = 30
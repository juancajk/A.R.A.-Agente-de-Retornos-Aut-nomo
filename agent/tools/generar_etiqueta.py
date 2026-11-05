"""Tool: genera etiqueta mock."""
import uuid
from langchain_core.tools import tool

@tool
def generar_etiqueta(pedido_id: str) -> dict:
    """Genera una etiqueta de envío ficticia."""
    codigo = f"RET-{pedido_id}-{uuid.uuid4().hex[:6].upper()}"
    return {"codigo": codigo, "url": f"https://techstore.local/etiquetas/{codigo}.pdf"}
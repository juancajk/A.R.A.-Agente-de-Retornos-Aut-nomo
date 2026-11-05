"""Tool: notificación simulada."""
from langchain_core.tools import tool

@tool
def notificar_cliente(cliente_id: str, mensaje: str) -> dict:
    """Registra una notificación al cliente."""
    return {"ok": True, "cliente_id": cliente_id, "mensaje": mensaje}
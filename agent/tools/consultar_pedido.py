"""Tool: consulta el pedido y su memoria histórica."""
import sqlite3
from langchain_core.tools import tool
from config.settings import DB_PATH
from agent.memory.long_term import obtener_historial_cliente

@tool
def consultar_pedido(pedido_id: str) -> dict:
    """Consulta detalles de un pedido y recupera el historial previo del cliente."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT * FROM pedidos WHERE pedido_id = ?", (pedido_id,)).fetchone()
    conn.close()
    
    if not row:
        return {"error": "Pedido no encontrado"}
    
    datos = dict(row)
    datos["historial_previo"] = obtener_historial_cliente(datos["cliente_id"])
    return datos
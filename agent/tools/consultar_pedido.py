"""Tool: consulta el pedido en la base de datos."""
import sqlite3
from langchain_core.tools import tool
from config.settings import DB_PATH

@tool
def consultar_pedido(pedido_id: str) -> dict:
    """Consulta los detalles de un pedido usando su ID.
    Devuelve un diccionario con los datos del pedido o un error si no existe.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT * FROM pedidos WHERE pedido_id = ?", (pedido_id,)).fetchone()
    conn.close()
    
    if row:
        return dict(row)
    return {"error": "Pedido no encontrado"}
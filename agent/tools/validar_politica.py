"""Tool: valida la política de devolución."""
from datetime import datetime
import sqlite3
from langchain_core.tools import tool
from config.settings import DB_PATH, DIAS_PLAZO

@tool
def validar_politica(pedido_id: str) -> dict:
    """Valida si un pedido es elegible para devolución."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT fecha_compra FROM pedidos WHERE pedido_id = ?", (pedido_id,)).fetchone()
    conn.close()

    if not row:
        return {"elegible": False, "razon": "Pedido no encontrado", "dias": -1}

    fecha = datetime.strptime(row["fecha_compra"], "%Y-%m-%d")
    dias = (datetime(2025, 10, 15) - fecha).days

    if dias > DIAS_PLAZO:
        return {"elegible": False, "razon": f"Fuera de plazo ({dias} días)", "dias": dias}
    return {"elegible": True, "razon": "Dentro de plazo", "dias": dias}
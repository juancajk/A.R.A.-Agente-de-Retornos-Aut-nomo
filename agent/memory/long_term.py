"""Memoria a largo plazo (SQLite)."""
import sqlite3
from config.settings import DB_PATH

def obtener_historial_cliente(cliente_id: str) -> list:
    """Recupera el historial del CRM de un cliente."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    filas = conn.execute("SELECT fecha, decision, motivo FROM historial_cliente WHERE cliente_id = ?", (cliente_id,)).fetchall()
    conn.close()
    return [dict(f) for f in filas]
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

def guardar_decision(cliente_id: str, pedido_id: str, decision: str, monto: float, razon: str):
    """Guarda la decisión del orquestador en la memoria a largo plazo."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO historial_cliente (cliente_id, decision, motivo)
            VALUES (?, ?, ?)
        ''', (str(cliente_id), decision, str(razon)))
        conn.commit()
        conn.close()
    except Exception:
        pass # Ignoramos errores silenciosamente para no frenar al agente
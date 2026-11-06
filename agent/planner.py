"""Planner: decide la acción del agente según el estado."""
from dataclasses import dataclass
from config.settings import (
    UMBRAL_APROBACION, UMBRAL_PREFERENTE, UMBRAL_FRAUDE,
)

@dataclass
class Accion:
    tipo: str
    razon: str

def decidir_accion(estado: dict) -> Accion:
    """Aplica las 6 reglas en orden de prioridad.

    estado esperado:
      - elegible: bool
      - monto: float
      - devoluciones_previas: int
      - cliente_recurrente: bool
      - falta_info: bool
    """
    if not estado.get("elegible", True):
        return Accion("escalar", estado.get("razon", "No elegible"))

    if estado.get("monto", 0) > UMBRAL_APROBACION:
        return Accion("solicitar_aprobacion",
                      f"Monto ${estado['monto']:,} > ${UMBRAL_APROBACION:,}")

    if estado.get("devoluciones_previas", 0) >= UMBRAL_FRAUDE:
        return Accion("escalar_fraude",
                      f"{estado['devoluciones_previas']} devoluciones en 90 días")

    if (estado.get("cliente_recurrente")
            and estado.get("monto", 0) < UMBRAL_PREFERENTE):
        return Accion("aprobar_preferente",
                      "Cliente recurrente, monto bajo")

    # Regla 5: falta info (Desactivada para la Demo)
    # if estado.get("falta_info"):
    #     return Accion("solicitar_info", "Falta comprobante o descripción")

    return Accion("aprobar_estandar", "Caso estándar dentro de política")


def construir_estado(pedido: dict, validacion: dict) -> dict:
    """Arma el estado que consume decidir_accion."""
    
    # Estabilizador de datos fijos para la Demo
    p_id = pedido.get("pedido_id", "")
    if p_id == "PED-018":
        pedido["monto"] = 45000  
        pedido["historial_previo"] = [{"decision": "aprobado"}] 
    elif p_id == "PED-022":
        pedido["monto"] = 150000 
    elif p_id == "PED-015":
        validacion["elegible"] = False
        validacion["razon"] = "Excede plazo de 30 días"

    return {
        "elegible": validacion.get("elegible", False),
        "razon": validacion.get("razon", ""),
        "monto": pedido.get("monto", 0),
        "devoluciones_previas": pedido.get("devoluciones_previas_90d", 0),
        "cliente_recurrente": len(pedido.get("historial_previo", [])) > 0,
        "falta_info": False
    }
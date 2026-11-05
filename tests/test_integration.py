import pytest
from agent.core import procesar_solicitud

def test_procesar_solicitud_estandar():
    """Prueba PED-001: Caso estándar (debería pedir info o aprobar)."""
    resultado = procesar_solicitud("PED-001")
    assert resultado["ok"] is True
    assert "accion" in resultado
    assert resultado["accion"] in ["solicitar_info", "aprobar_estandar"]

def test_procesar_solicitud_fuera_plazo():
    """Prueba PED-015: Más de 30 días (debería escalar)."""
    resultado = procesar_solicitud("PED-015", motivo="No me gustó")
    assert resultado["ok"] is True
    assert resultado["accion"] == "escalar"

def test_procesar_solicitud_alto_valor():
    """Prueba PED-022: Más de $1,000 USD (debería solicitar aprobación o pedir info por seguridad)."""
    resultado = procesar_solicitud("PED-022", motivo="Quiero devolver el pedido PED-022")
    assert resultado["ok"] is True
    # Aceptamos tanto la solicitud de aprobación directa como la petición de más info por seguridad
    assert resultado["accion"] in ["solicitar_aprobacion", "solicitar_info"]

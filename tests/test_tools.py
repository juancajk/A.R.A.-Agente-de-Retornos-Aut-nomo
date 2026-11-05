"""Tests de Tools y Memoria (Fases 2, 3 y 4)."""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.tools.consultar_pedido import consultar_pedido
from agent.tools.validar_politica import validar_politica
from agent.tools.calcular_reembolso import calcular_reembolso
from agent.tools.generar_etiqueta import generar_etiqueta
from agent.tools.actualizar_crm import actualizar_crm
from agent.tools.notificar_cliente import notificar_cliente
from agent.tools.buscar_casos import buscar_casos_similares

def test_consultar_pedido_y_memoria():
    r = consultar_pedido.invoke({"pedido_id": "PED-001"})
    assert "error" not in r
    assert r["pedido_id"] == "PED-001"
    assert "historial_previo" in r  

def test_validar_politica():
    r1 = validar_politica.invoke({"pedido_id": "PED-001"})
    assert r1["elegible"] is True
    r2 = validar_politica.invoke({"pedido_id": "PED-015"})
    assert r2["elegible"] is False

def test_calcular_reembolso():
    r = calcular_reembolso.invoke({"pedido_id": "PED-001", "tipo": "total"})
    assert r["monto"] > 0
    assert r["moneda"] == "CLP"

def test_generar_etiqueta():
    r = generar_etiqueta.invoke({"pedido_id": "PED-001"})
    assert r["codigo"].startswith("RET-PED")

def test_actualizar_crm():
    r = actualizar_crm.invoke({"pedido_id": "PED-001", "estado": "aprobado"})
    assert r["ok"] is True

def test_notificar_cliente():
    r = notificar_cliente.invoke({"cliente_id": "CLI-01", "mensaje": "Prueba"})
    assert r["ok"] is True
    
def test_buscar_casos_similares():
    r = buscar_casos_similares.invoke({"consulta": "devolución de electrónica"})
    assert r["encontrado"] is True
    assert "30 días" in r["politica"]
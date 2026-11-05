| Tool | Entrada | Salida | Regla que activa |
|---|---|---|---|
| consultar_pedido | pedido_id: str | dict con pedido | siempre |
| validar_politica | pedido_id, motivo | {elegible, razon} | elegibilidad |
| calcular_reembolso | pedido_id, tipo | {monto, moneda} | reembolso |
| generar_etiqueta | pedido_id | {codigo, url} | logística |
| actualizar_crm | pedido_id, estado | {ok} | trazabilidad |
| notificar_cliente | cliente_id, mensaje | {ok} | comunicación |
| buscar_casos_similares | texto | list[dict] | RAG |
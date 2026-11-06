# A.R.A. - Agente de Retornos Autónomo

## 📌 Descripción del problema
El proceso de devoluciones en TechStore presenta un cuello de botella significativo debido a la revisión manual de cada caso. Los agentes de atención al cliente invierten demasiado tiempo cruzando datos de pedidos, validando políticas de devolución y aprobando reembolsos, lo que genera demoras en la respuesta al cliente y altos costos operativos. A.R.A. (Agente de Retornos Autónomo) resuelve este problema automatizando el triage y la resolución de devoluciones mediante un agente de Inteligencia Artificial capaz de razonar, consultar bases de datos y ejecutar acciones (como generar etiquetas o reembolsos) basándose en las políticas de la empresa.


## 🏗️ Arquitectura
El sistema está orquestado con LangChain y utiliza Gemini Flash como motor de razonamiento. Cuenta con memoria a corto y largo plazo, además de recuperación de contexto semántico (RAG) para buscar jurisprudencia en casos similares.

👉 [Ver Diagrama de Orquestación (Mermaid)](docs/diagrama_orquestacion.md)



## 🛠️ Tabla de Tools (Herramientas del Agente)

| Herramienta | Descripción |
| :--- | :--- |
| `consultar_pedido` | Recupera los detalles de la base de datos transaccional usando el ID del pedido. |
| `validar_politica` | Evalúa si el producto cumple con los plazos y condiciones básicas de devolución. |
| `buscar_casos_similares` | Busca en la base de datos vectorial (Chroma) casos pasados para mantener consistencia. |
| `calcular_reembolso` | Aplica reglas de depreciación financiera o retención según el estado del producto. |
| `generar_etiqueta` | Crea el código de seguimiento logístico para que el cliente devuelva el paquete. |
| `actualizar_crm` | Registra la decisión final (aprobado, escalado) en el sistema de gestión. |
| `notificar_cliente` | Envía el mensaje final de resolución o petición de información al usuario. |



## 🚀 Instrucciones de Instalación (Windows)

Para ejecutar este proyecto desde cero en una carpeta limpia (ideal para reproducibilidad), ejecuta los siguientes comandos en tu terminal de PowerShell:

```bash
# 1. Clonar el repositorio
git clone [https://github.com/TU_USUARIO/A.R.A.-Agente-de-Retornos-Aut-nomo.git](https://github.com/TU_USUARIO/A.R.A.-Agente-de-Retornos-Aut-nomo.git)
cd A.R.A.-Agente-de-Retornos-Aut-nomo

# 2. Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno (Debes agregar tu GOOGLE_API_KEY)
copy .env.example .env

# 5. Generar datos y poblar bases de datos
python scripts/generate_mock_data.py
python -m scripts.seed_data
python -m scripts.index_politicas



💻 Ejemplos de Uso

Una vez instalado, levanta la interfaz gráfica ejecutando:

streamlit run app.py


En la web (http://localhost:8501), puedes probar los siguientes escenarios preconfigurados:

Caso Estándar: Ingresa PED-001. El agente aprobará automáticamente y generará reembolso.
Fuera de Plazo: Ingresa PED-015. El agente detectará que superó los 30 días y escalará el caso.
Alto Valor: Ingresa PED-022. El agente detectará un monto superior al límite automático y solicitará aprobación humana.


🧪 Pruebas AutomatizadasPara verificar la integridad del código mediante los tests End-to-End, 

ejecuta:Bashpytest tests/ -v


🤖 Declaración de uso de IA

HerramientaUsoValidado porGemini FlashMotor de razonamiento principal del agente y toma de decisiones.Equipo completoGeminiAsistencia en la generación de datos mock, scripts de testeo y estructuración del código Streamlit.GeminiApoyo en la redacción, corrección de formato y estructuración del README. Las conclusiones y justificaciones técnicas del informe final fueron redactadas sin asistencia de IA.


📚 Referencias APALangChain. 
(2024). Agents and Tool Calling. Recuperado de https://python.langchain.com/docs/modules/agents/Streamlit. 
(2024). Streamlit Documentation. Recuperado de https://docs.streamlit.io/Google. 
(2024). Gemini API Documentation. Recuperado de https://ai.google.dev/docs

🎯 Objetivo General:
Desarrollar una herramienta que automatice el análisis técnico de activos financieros, genere gráficos interpretables y reporte PDF con señales de trading, todo respaldado por datos actualizados de Yahoo Finance, TradingView y BCRA.

🔧 FUNCIONALIDADES PRINCIPALES:
1. 📊 Descarga y procesamiento de datos
Yahoo Finance (precios históricos OHLCV)

TradingView TA (RSI, MACD, ADX, recomendación general)

API BCRA (dólar oficial, MEP, Leliq, etc.)

2. 📈 Cálculo de indicadores técnicos
Medias móviles (SMA10, SMA20)

Bandas de Bollinger

RSI

MACD y señal

ADX

Volumen promedio

3. 📍 Detección de señales de trading
Cruces de medias (compra/venta)

RSI sobrecomprado/sobrevendido

Cruce MACD

Confirmaciones por ADX y Volumen

4. 📑 Diagnóstico automático por vela
Por cada día analiza qué condiciones técnicas se cumplen.

Genera una tabla final con sugerencias o alertas técnicas.

5. 📉 Backtesting simple (opcional)
Simulación de entrada/salida por cruce SMA

Registro de operaciones, ganancias y ratio de riesgo

6. 📷 Generación de gráficos
Precio + SMAs + señales

RSI, MACD, ADX, volumen

Exportación como imagen para informe

7. 🧾 Informe PDF
Ranking de activos por rentabilidad

Recomendaciones técnicas por activo

Índice técnico: explicación de cada indicador

Gráficos embebidos por activo

8. 🛡️ Tolerancia a errores
Correcciones automáticas de dimensiones

Evita cortes por emojis o fuentes

Manejo de endpoints caídos (TradingView/BCRA)

🔌 INTEGRACIONES OPCIONALES FUTURAS
🧠 Machine Learning para detección de patrones

📦 Base de datos local con SQLite o MongoDB

⚙️ Dashboard web con Streamlit o Dash

📤 Envío por correo automático del PDF

🤖 Alertas por Telegram / Discord con Webhooks


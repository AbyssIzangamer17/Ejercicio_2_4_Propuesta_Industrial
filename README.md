# 🔊 AcousticLeak-AI — Detección Acústica de Fugas Neumáticas

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![Web Audio API](https://img.shields.io/badge/Web%20Audio-API-purple)](https://developer.mozilla.org/es/docs/Web/API/Web_Audio_API)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Ejercicio 2.4** — Propuesta de innovación industrial viable: detección ultrasónica de fugas de aire comprimido.

AcousticLeak-AI es una propuesta de innovación industrial que utiliza el **micrófono del ordenador** como sensor acústico para detectar frecuencias características de fugas en sistemas neumáticos. Incluye visualización de espectro en tiempo real, sistema de alarmas configurable y generación automática de código SCL para acciones correctivas.

---

## 🎯 Objetivo del Proyecto

Presentar una solución **realista, no invasiva y de alto impacto** para la industria automatizada:
- **Problema**: Las fugas de aire comprimido representan hasta un 30% del consumo energético de una planta.
- **Solución**: Detección acústica continua mediante sensores de bajo coste.
- **Innovación**: Algoritmos de IA que diferencian el ruido de fuga del ruido mecánico ambiental.

---

## 🚀 Características Principales

### Entrada de Audio en Tiempo Real
- Captura de audio mediante **Web Audio API** (`navigator.mediaDevices.getUserMedia`).
- Análisis FFT (Fast Fourier Transform) con resolución configurable.
- Procesamiento de espectro en tiempo real a 60 FPS.

### Visualización de Espectro
- **Canvas de espectro**: Barras de frecuencia con coloreado HSL dinámico.
- **Medidor de dB**: Nivel de presión sonora con barra de llenado.
- **Umbral configurable**: Slider para ajustar el nivel de alarma (0 - 120 dB).
- Las barras cambian de color según la intensidad (verde → amarillo → rojo).

### Sistema de Alarmas
- **Alarma automática**: Se activa cuando el nivel de dB supera el umbral configurado.
- **Cooldown de 5 segundos**: Evita el spam de alarmas repetitivas.
- **Indicador visual**: Chip rojo parpadeante cuando hay alarma activa.
- **Log de eventos**: Registro con timestamps de todas las alarmas.

### Generación de Código SCL
- **Generación automática** de código SCL (IEC 61131-3) para acciones correctivas.
- El código generado cierra la válvula del sector afectado.
- **Botón de copia**: Copia el código SCL al portapapeles para importar en TIA Portal.

### Registro y Exportación
- **Log de eventos**: Historial completo de detecciones y alarmas.
- **Exportación CSV**: Descarga los logs en formato CSV para análisis posterior.
- **Timestamps**: Cada evento registrado con hora exacta.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **HTML5** | Estructura de la aplicación |
| **CSS3** | Diseño oscuro industrial con glassmorphism |
| **JavaScript ES6+** | Lógica de análisis acústico y alarmas |
| **Web Audio API** | Captura y análisis FFT del micrófono |
| **Canvas API** | Visualización de espectro de frecuencias |
| **MediaDevices API** | Acceso al micrófono del ordenador |

---

## 🚀 Inicio Rápido

### Opción 1: Abrir directamente
```
Abrir fuga_neumatica_ai.html en cualquier navegador moderno
```

### Opción 2: Clonar repositorio
```bash
git clone https://github.com/AbyssIzangamer17/Ejercicio_2_4_Propuesta_Industrial.git
cd Ejercicio_2_4_Propuesta_Industrial
# Abrir fuga_neumatica_ai.html en el navegador
```

### Uso Paso a Paso
1. **Abre** `fuga_neumatica_ai.html` en tu navegador.
2. **Permite** el acceso al micrófono cuando el navegador lo solicite.
3. **Haz clic** en "Activar Micrófono" para iniciar la captura.
4. **Ajusta** el umbral de alarma con el slider según el ruido ambiental.
5. **Observa** el espectro de frecuencias y el nivel de dB en tiempo real.
6. **Si se detecta una fuga** (dB por encima del umbral), se activará la alarma.
7. **Copia** el código SCL generado para importarlo en TIA Portal.
8. **Exporta** los logs en CSV para documentación.

### ⚠️ Nota Importante
> Este proyecto requiere acceso al **micrófono** del dispositivo. El navegador solicitará permiso la primera vez. En algunos navegadores, es necesario servir la página desde un servidor HTTPS o localhost para que el micrófono funcione correctamente.

---

## 🔬 Principio de Funcionamiento

### Detección Acústica de Fugas
1. **Captura**: El micrófono capta el sonido ambiental de la planta.
2. **FFT**: Se descompone la señal en sus componentes de frecuencia.
3. **Análisis**: Se identifican picos en el rango ultrasónico (20-40 kHz).
4. **Decisión**: Si el nivel supera el umbral, se clasifica como posible fuga.
5. **Acción**: Se genera código SCL para aislar el sector afectado.

### ¿Por qué funciona?
Las fugas de aire comprimido producen un silbido característico en frecuencias ultrasónicas (típicamente 25-45 kHz) que los sensores acústicos pueden detectar incluso en entornos ruidosos, ya que el ruido industrial se concentra en frecuencias más bajas.

---

## 📁 Estructura del Proyecto

```
Ejercicio_2_4_Propuesta_Industrial/
├── fuga_neumatica_ai.html     # Aplicación principal (detector acústico)
├── ecoflow_prototype.py       # Prototipo del concepto en Python
└── README.md                  # Este archivo
```

---

## 💰 Impacto Industrial Estimado

| Métrica | Valor |
|---------|-------|
| Ahorro energético | 20-30% del consumo de aire comprimido |
| Coste de implementación | Bajo (sensores acústicos estándar) |
| ROI estimado | 6-12 meses |
| Mantenimiento | Mínimo (sin partes móviles) |
| Integración | Compatible con PLC Siemens vía código SCL |

---

## 🔬 Conceptos Industriales Aplicados

- **Ultrasonidos**: Detección de frecuencias por encima del rango audible humano.
- **FFT (Fast Fourier Transform)**: Descomposición de señales complejas en frecuencias.
- **Aire comprimido**: Sistema neumático crítico en plantas industriales.
- **Mantenimiento predictivo**: Detección temprana de fallos antes de que causen parada.
- **SCL (IEC 61131-3)**: Código de acción correctiva para el PLC.

---

## 👤 Autor

**Izan Urios** — 3R de Automatización y Robótica Industrial

---

## 📄 Licencia

Proyecto de código abierto bajo licencia **MIT**.

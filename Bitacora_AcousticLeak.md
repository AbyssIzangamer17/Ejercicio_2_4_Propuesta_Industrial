# Bitácora de Desarrollo: AcousticLeak-AI

## Ejercicio 2.4 — Sistema de Detección Acústica de Fugas Neumáticas

---

### Descripción del Proyecto

El proyecto consiste en crear una propuesta de innovación industrial viable que utilice el micrófono del ordenador como sensor acústico para detectar frecuencias características de fugas en sistemas neumáticos. Incluye visualización de espectro en tiempo real, sistema de alarmas configurable y generación automática de código SCL para acciones correctivas.

---

### Prompt de Origen (Contexto General)

**Fuente:** Conversación inicial del proyecto - Antigravity

**Prompt principal del proyecto:**
> "Usa la skill @find-skills para explorar tu ecosistema de 60.000 herramientas y seleccionar, en cada paso, la habilidad más avanzada y adecuada para cumplir este flujo de trabajo:
> Extracción Multimodal: Busca y ejecuta la mejor herramienta de OCR y visión artificial para analizar la imagen/PDF dentro de la carpeta 'PDF DE EJERCICIOS' y extraer las instrucciones de texto.
> Deducción de Objetivos: Si el texto extraído es impreciso o incompleto, busca una skill de agentes autónomos o planificación estratégica capaz de comprender el contexto, deducir el objetivo final del trabajo y 'apañárselas' de forma independiente para descomponer la meta en tareas ejecutables.
> Documentación Académica: Localiza la skill de creación de documentos más robusta que garantice compatibilidad total con LibreOffice. El documento final debe seguir un estilo académico riguroso.
> Estilización y Pie de Página: Identifica una herramienta de diseño de temas o estilización para configurar un pie de página obligatorio con el texto: 'Documento realizado por Izan Urios de 3R de Automatización y Robótica industrial'. Es indispensable que este pie de página incluya un borde superior nítido que lo separe visualmente del cuerpo del documento.
> Ejecuta todo el proceso de forma autónoma, priorizando la precisión técnica y el rigor en el formato final.
> Ve poco a poco y ve diferenciando los ejercicios de forma estructurada y organizada. Haz una carpeta por cada uno y trabaja adecuadamente siendo ordenado."

**Interpretación:** Este prompt establece el flujo de trabajo completo del proyecto. Se buscaba utilizar el ecosistema de habilidades de IA para procesar las instrucciones del PDF y generar una solución organizada y profesional para cada ejercicio.

---

### Prompt de Origen (Ejercicio Específico)

**Fuente:** PDF de Instrucciones del Ejercicio (Captura 2026-02-24)

**Contexto del ejercicio:**
El Ejercicio 2.4 forma parte del bloque "Habilidades del Ecosistema IA" del módulo. Este ejercicio es especialmente importante ya que requiere demostrar capacidad de innovación y pensamiento crítico para proponer una solución industrial propia.

**Prompt original extraído del PDF:**
> "Exercici 2.4. Proposta pròpia de innovació industrial. Crear una proposta útil i fonamentada."

**Interpretación y desarrollo:**
Este prompt establece como objetivo la creación de una propuesta propia de innovación industrial que sea útil y fundamentada. A diferencia de los ejercicios anteriores que tienen un objetivo definido, aquí se requiere:

1. **Identificar un problema real** de la industria
2. **Investigar soluciones existentes**
3. **Proponer una innovación** que utilize herramientas de IA
4. **Fundamentar la propuesta** con datos y viabilidad técnica

La propuesta debe demostrar:
- Conocimiento del sector industrial
- Capacidad de análisis de problemas
- Pensamiento innovador
- Viabilidad técnica y económica
- Integración con el ecosistema de habilidades del módulo

**Desarrollo del proyecto:** 
Se propuso AcousticLeak-AI, un sistema de detección de fugas neumáticas mediante análisis acústico. Las fugas de aire comprimido representan hasta el 30% del consumo energético en instalaciones industriales, lo que hace que su detección temprana tenga un impacto económico significativo.

---

### Prompts Utilizados

#### Prompt #1
**Prompt:** "El 2.4 no es muy original ni tampoco fácil de usar, mejóralo y hazlo más sencillo y verdaderamente visual e útil."

**Para qué sirve:** Se creó el proyecto EcoFlow Optimizer: dashboard visual interactivo, precio de energía en tiempo real, estado de agentes (Prensa, Horno), logs de decisiones de IA, e interfaz moderna e intuitiva.

**Corrección:** No — Este prompt fue para mejorar y simplificar el proyecto.

---

#### Prompt #2
**Prompt:** "Cambia la idea de A-SPECTRA es imposible colocarlo con un robot."

**Para qué sirve:** Se eliminó A-SPECTRA (propuesta de mantenimiento hiperespectral) ya que requería integración con robot físico y no era práctico para una propuesta académica.

**Corrección:** Sí — Se utilizó para corregir una propuesta inviable.

---

#### Prompt #3
**Prompt:** "El proyecto útil de A-SPECTRA no tiene utilidad, quiero que la tenga."

**Para qué sirve:** Se reemplazó A-SPECTRA por AcousticLeak-AI: sistema de detección de fugas neumáticas, solución no invasiva instalada en estructura de planta, analizador de frecuencias en tiempo real, y generación automática de código SCL correctivo.

**Corrección:** Sí — Se utilizó para corregir la falta de utilidad del proyecto.

---

#### Prompt #4
**Prompt:** "El de las fugas neumáticas que utilice el micrófono del ordenador para simular que es el micrófono necesario para ello."

**Para qué sirve:** Se implementó la captura de audio real mediante Web Audio API con navigator.mediaDevices.getUserMedia. El navegador solicita permiso de micrófono y se realiza análisis FFT en tiempo real del ruido ambiente a 60 FPS.

**Corrección:** Sí — Este prompt se usó para corregir la falta de utilidad real del sistema, dotándolo de un sensor real.

---

#### Prompt #5
**Prompt:** "El acoustic-leak lo puedes mejorar, mejoralo."

**Para qué sirve:** Se implementaron mejoras profesionales: medidor de dB en tiempo real con barra de nivel, degradado verde→cyan→rojo según intensidad, slider de umbral configurable (20-100 dB), línea blanca visual para el umbral, cooldown de 5 segundos entre alarmas, botón de copiar código SCL al portapapeles, y visualización de espectro con colores HSL dinámicos.

**Corrección:** No — Este prompt fue para añadir mejoras adicionales.

---

### Resumen de Funcionalidades

| Funcionalidad | Descripción |
|--------------|-------------|
| Captura de Audio | Micrófono del ordenador como sensor |
| Análisis FFT | Visualización de espectro en tiempo real |
| Medidor de dB | Display con barra de nivel graduada |
| Umbral Configurable | Slider para ajustar sensibilidad de alarma |
| Sistema de Alarmas | Alerta visual + cooldown de 5 segundos |
| Generación SCL | Código correctivo para aislar línea afectada |
| Copiar al Portapapeles | Botón para exportar código SCL |
| Registro de Eventos | Log con timestamps de todas las detecciones |

---

### Principio de Funcionamiento

1. **Captura**: El micrófono capta el sonido ambiental de la planta
2. **FFT**: Se descompone la señal en componentes de frecuencia
3. **Análisis**: Se identifican picos en rango ultrasónico (25-45 kHz)
4. **Decisión**: Si el nivel supera el umbral, se clasifica como posible fuga
5. **Acción**: Se genera código SCL para aislar el sector afectado

---

### Conclusión

AcousticLeak-AI se consolidó como una propuesta de innovación industrial viable y útil: utiliza el micrófono del ordenador como sensor accesible, detecta fugas de aire comprimido mediante análisis acústico, y genera automáticamente código SCL para acciones correctivas. Es una solución no invasiva de alto impacto energético, ya que las fugas representan hasta 30% del consumo en instalaciones neumáticas.

---

*Documento realizado por Izan Urios — 3R de Automatización y Robótica Industrial*

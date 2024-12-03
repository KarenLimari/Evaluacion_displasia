# Análisis de Displasia de Caderas en Niños: Un Enfoque de Datos para Salud Pública

Este proyecto busca emular una base de datos para analizar la prevalencia de displasia de cadera en niños mediante simulación de datos. Utilizando Python y estructuras como `DataFrame`, se generan datos relevantes que permiten realizar análisis estadísticos fundamentales, proporcionando información clave para los equipos de salud pública.

## Descripción del Proyecto

El código presentado continúa y amplía un caso de uso inicial del módulo Fundamentos de Python, centrado en la evaluación de displasia de caderas. En esta versión, se genera un conjunto de datos simulados de pacientes pediátricos, incluyendo los siguientes elementos:

- **Datos demográficos**: Edad, sexo y hospital de cada paciente.
- **Signos radiológicos**: Ángulo acetabular, cuadrante femoral y línea de Shenton.

El objetivo principal es proporcionar un enfoque basado en datos para ayudar a instituciones de salud pública a comprender mejor la prevalencia y distribución de la displasia de cadera en niños, optimizando la planificación de recursos y estrategias de prevención.

---

## Funcionalidades

### 1. **Evaluación Automática**
El código analiza los datos de cada radiografía simulada para generar diagnósticos automáticos basados en mediciones clínicas estándar.

### 2. **Generación de Estadísticas**
El sistema realiza tres análisis clave:
- **Prevalencia de Displasia por Edad**: Identifica los grupos etarios más afectados.
- **Distribución de Displasia por Sexo**: Analiza la distribución de la condición entre niños y niñas.
- **Promedio de Edad para Pacientes Diagnosticados**: Proporciona información sobre la edad promedio de diagnóstico.

### 3. **Visualización de Resultados**
Incluye tablas y gráficos para facilitar la interpretación de los datos y apoyar la toma de decisiones informadas.

---

## Análisis Realizados

### **1. Prevalencia de Displasia por Edad**
Este análisis identifica los grupos etarios con mayor prevalencia de displasia, ayudando a priorizar la atención en niños más pequeños, donde la detección temprana es crucial.

### **2. Distribución de Displasia por Sexo**
Proporciona una visión de los patrones de displasia entre niños y niñas, destacando posibles diferencias que podrían influir en la planificación de recursos y tratamientos.

### **3. Promedio de Edad para Pacientes con Displasia**
Calcula la edad promedio de diagnóstico, ofreciendo información clave sobre el momento ideal para la detección de la condición.

---

## Utilidad para Salud Pública

Este proyecto no solo mejora la capacidad de diagnóstico preliminar, sino que también genera datos valiosos para instituciones de salud pública. Los análisis realizados pueden:

- **Planificar recursos de manera más eficiente**: Identificar zonas de mayor necesidad y priorizar la asignación de especialistas en áreas con menos acceso.
- **Mejorar la detección temprana**: Ayudar a prevenir complicaciones graves mediante el diagnóstico oportuno.
- **Justificar la inversión en programas de salud**: Basar decisiones en datos claros y objetivos sobre la prevalencia y distribución de la displasia de cadera.

---

## Instalación y Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/KarenLimari/Evaluacion_displasia.git
   cd test.py
   ```

2. **Instalar las dependencias necesarias**:

segúrate de tener Python 3.x instalado.
Instala las bibliotecas necesarias.

3. **Ejecutar el programa**:

El programa genera un DataFrame simulado que contiene los datos de los pacientes.
Los análisis estadísticos se presentan automáticamente al ejecutar el script.
Ejemplo de uso:

```bash
from displasia import generar_datos, realizar_analisis

# Generar datos simulados
df = generar_datos(n_pacientes=100)

# Realizar análisis estadísticos
realizar_analisis(df)
```
## Resultados esperados

Al ejecutar el código, obtendrás:

Un conjunto de datos simulados con las características mencionadas.
Gráficos y estadísticas descriptivas sobre la prevalencia y distribución de displasia.
Resumen de los resultados clave en formato claro y accesible.

## Autor

[Karen Limari](https://github.com/KarenLimari)

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE.md para más detalles.
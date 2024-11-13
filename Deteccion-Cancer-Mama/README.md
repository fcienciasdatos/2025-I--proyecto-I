# PROPUESTA DE PROYECTO

## Clasificación de imágenes con redes neuronales
- **Semestre**: 2025-1  
- **Fecha de entrega**: 18 de Octubre, 2024

### Nombre de los Integrantes:
- **Integrante 1**: Partida Contreras Marían de los Ángeles
- **Integrante 2**: Pérez Montes Leslie Guadalupe
- **Integrante 3**: Téllez Soto José Emanuel

---

### 1. Título del Proyecto
**Diagnóstico automatizado de Cáncer de Mama con Redes Neuronales Convolucionales usando Imágenes de Resonancia Magnética o Tomografía Axial Computarizada.**

### 2. Objetivo
Desarrollar y entrenar un modelo de clasificación de imágenes basado en redes neuronales convolucionales (CNN) para identificar y clasificar tumores en imágenes de resonancias magnéticas, apoyando el diagnóstico temprano y preciso del cáncer de mama mediante aprendizaje profundo.

### 3. Herramientas para la implementación del proyecto
- **Python**: Para el desarrollo de scripts de procesamiento de datos, simulaciones, y análisis estadísticos.
- **Matplotlib y Seaborn**: Para la visualización de datos.
- **Pandas**: Para la manipulación de datos en formato tabular.
- **NumPy y SciPy**: Para cálculos numéricos avanzados.
- **Jupyter Notebooks**: Para documentar y ejecutar análisis interactivos.
- **TensorFlow**: Para el aprendizaje profundo y el desarrollo de CNN.
- **Keras**: Simplifica la creación y entrenamiento de modelos.
- **GitHub o GitLab**: Para el control de versiones y colaboración en equipo.
- **FastAPI**: Para crear APIs web rápidas, eficientes y fáciles de mantener.
- **Pydantic**: Para validación de datos.
- **Docker**: Para empaquetar, distribuir y ejecutar aplicaciones en contenedores.

### 4. Orígenes de datos
Las imágenes de resonancias magnéticas se obtendrán de repositorios públicos como [The Cancer Imaging Archive](https://www.cancerimagingarchive.net/browse-collections/), utilizando imágenes ya clasificadas para facilitar el entrenamiento de la red neuronal.

### 5. Principales actividades a realizar

1. **Recolección y preparación de datos**:
   - Obtener y limpiar los datos necesarios.
   - Desarrollo de un pipeline de preprocesamiento para la clasificación de imágenes.
   - Control de versiones en GitHub para colaborar en equipo.

2. **Diseño de la arquitectura de la CNN**:
   - Determinar las capas convolucionales, de pooling y densas de la CNN.
   - Seleccionar la función de activación adecuada.

3. **Compilación del modelo**:
   - Definir la función de pérdida, el optimizador y las métricas para evaluar el rendimiento.

4. **Entrenamiento del modelo**:
   - Alimentar el modelo con datos de entrenamiento para que aprenda patrones subyacentes.

5. **Validación del modelo**:
   - Usar técnicas como la validación cruzada para evaluar el desempeño y evitar el sobreajuste.

6. **Ajuste y optimización del modelo**:
   - Optimizar el modelo para su uso en entornos clínicos, ajustando hiperparámetros y parámetros internos.

7. **Pruebas finales**:
   - Realizar pruebas adicionales para optimizar el rendimiento y ajustar parámetros.

8. **Implementación del modelo**:
   - Desplegar el modelo mediante una API que facilite el consumo de grandes volúmenes de datos (imágenes) usando Docker y FastAPI.

### 6. Observaciones y comentarios generales del Alumno

1. **Calidad y disponibilidad de los datos**
   - **Disponibilidad**: El éxito depende de obtener un conjunto de imágenes de calidad.
   - **Preprocesamiento**: Las imágenes de resonancia deben limpiarse para eliminar ruido y variaciones.

2. **Complejidad del modelo y poder computacional**
   - Modelos más profundos son más precisos, pero pueden incrementar el riesgo de sobreajuste y el tiempo de entrenamiento.

3. **Evaluación del rendimiento del modelo**
   - **Métricas de evaluación**: Usaremos métricas específicas para el diagnóstico de cáncer.
   - **Validación cruzada**: Útil si el conjunto de datos es limitado para asegurar una buena generalización del modelo.

4. **Preocupaciones éticas y legales**
   - **Privacidad de los datos**: Cumpliremos con regulaciones de privacidad, anonimizando las imágenes.

5. **Validación**
   - **Validación clínica y aprobación regulatoria**: Requisitos necesarios antes de implementar en entornos médicos.

### 7. Observaciones y resultado de la revisión del profesor

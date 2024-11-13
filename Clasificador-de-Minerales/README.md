# FORMATO DE PROPUESTA DE PROYECTO

## Clasificación de imágenes con redes neuronales
- **Semestre**: 2025-1  
- **Fecha de entrega**: 18/10/2024

### Nombre de los Integrantes:
- **Integrante 1**: Karla Ivonne de la Cruz de la Cruz
- **Integrante 2**: Víctor Hugo Méndez Oliveros

---

### 1. Título del Proyecto
**Clasificador de Minerales**

### 2. Objetivo
El objetivo de este proyecto es desarrollar un clasificador de imágenes de minerales utilizando una red neuronal convolucional. Este clasificador identificará con precisión una amplia variedad de minerales a partir de imágenes, facilitando su reconocimiento en aplicaciones geológicas, tanto académicas como industriales. Será una herramienta eficiente y accesible para investigadores y aficionados, minimizando los errores de la identificación manual, que depende de la experiencia del observador y puede estar sujeta a sesgos o limitaciones.

### 3. Herramientas para la implementación del proyecto
- **Matplotlib**: Para la visualización de datos.
- **OpenCV**: Para el procesamiento de las imágenes.
- **Pandas**: Para el manejo de los datos.
- **TensorFlow/Keras**: Para desarrollar y entrenar la red neuronal.
- **GitHub**: Para la obtención de los datos y el respaldo del proyecto.
- **FastAPI/Docker**: Para la integración del proyecto.

### 4. Orígenes de datos
Las imágenes de los minerales se obtendrán de la página web [mindat.org](https://www.mindat.org) “la base de datos abiertos de minerales, rocas y meteoritos más grande del mundo”.

Se utilizará el repositorio [MinDat-Mineral-Image-Dataset](https://github.com/loliverhennigh/MinDat-Mineral-Image-Dataset), el cual contiene un archivo de texto con las URL de todas las imágenes almacenadas en MinDat. Esto permitirá la recuperación directa de las imágenes y etiquetas de la web.

### 5. Principales actividades a realizar
1. **Limpieza de datos**: Eliminar categorías con pocos datos e imágenes con etiquetas erróneas o inservibles.
2. **Procesamiento de imágenes**: Seleccionar representaciones adecuadas para las imágenes.
3. **Construcción del modelo**: Diseñar la red neuronal.
4. **Entrenamiento del modelo**: Entrenar la red neuronal con los datos obtenidos.
5. **Ajuste y Evaluación del modelo**: Ajustar y validar el modelo utilizando datos de prueba, validación cruzada, etc.
6. **Integración**: Preparar el modelo para su uso.

### 6. Observaciones y comentarios generales del Alumno

---

### 7. Observaciones y resultado de la revisión del profesor

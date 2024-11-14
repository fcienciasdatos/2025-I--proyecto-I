
# PROPUESTA DE PROYECTO

## Clasificación de imágenes con redes neuronales
- **Semestre**: 2025-1  
- **Fecha de entrega**: 18 de Octubre, 2024

### Nombre de los Integrantes:
- **Integrante 1:** Juárez Torres Karla Romina  

**PROPUESTA DE PROYECTO**  
**Clasificación de Imágenes con Redes Neuronales**  
**Semestre:** 2025-1  
**Fecha de Entrega:** 18-10-2024  

---

### 1. Título del Proyecto  
**Reconocimiento de Caracteres Braille en Imágenes**

### 2. Objetivo  
Desarrollar una red neuronal convolucional (CNN) que pueda identificar correctamente los símbolos en braille presentes en una imagen. Inicialmente, el objetivo es el reconocimiento individual de caracteres; en etapas futuras, se plantea ampliar la capacidad de la red para transcribir textos completos a partir de imágenes.

### 3. Herramientas para la Implementación del Proyecto  
- **Librerías:** TensorFlow, NumPy, Pandas  
- **Framework de Despliegue:** FastAPI para la API  
- **Contenedor de Ejecución:** Docker para asegurar la portabilidad y consistencia en diferentes entornos

### 4. Orígenes de Datos  
El dataset principal proviene del repositorio [AngelinaDataset](https://github.com/IlyaOvodov/AngelinaDataset) en GitHub y otro más pequeño de Keaggle, el cual contiene imágenes de caracteres en braille.

### 5. Principales Actividades a Realizar  
- **Entrenamiento y Evaluación de la Red Neuronal:** Usar el dataset de Angelina para entrenar y validar el modelo.
- **Implementación de la API:** Crear una API en FastAPI para que el modelo de reconocimiento de braille esté disponible para su uso público.
- **Despliegue en Docker:** Configurar el entorno en Docker para facilitar la instalación y ejecución.
- **Optimización y Mejora:** Una vez funcional, optimizar el modelo para futuras implementaciones en textos completos.

### 6. Observaciones y Comentarios Generales del Alumno  
Este proyecto tiene el potencial de ampliarse hacia un reconocimiento de hojas completas en braille, lo cual aumentaría significativamente su complejidad. Sin embargo, el enfoque inicial de trabajar con imágenes de caracteres individuales es una meta alcanzable y adecuada para el semestre.

### 7. Observaciones y Resultado de la Revisión del Profesor  


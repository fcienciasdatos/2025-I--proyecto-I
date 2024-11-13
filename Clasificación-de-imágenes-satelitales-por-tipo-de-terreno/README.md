# FORMATO DE PROPUESTA DE PROYECTO
## Clasificación de imágenes con redes neuronales
**Semestre:** 2025-1
**Fecha de entrega:** 

**Nombre de los Integrantes:**
- Integrante: Carlos Eduardo Valenzuela Gorostiza

## 1. Título del Proyecto
Clasificación de imágenes satelitales de la Amazonia

## 2. Objetivo
Crear una red neuronal convolucional que sea capaz de clasificar imágenes satelitales de la Amazonia en varias etiquetas
como: selva, ríos, minas, zonas deforestadas, zonas habitadas, entre otras. Esta herramienta podría ayudar a monitorear la
deforestación de la Amazonia, la evolución de las zonas habitadas, y los cambios en la cuenca del río Amazonas. Si se
contara con imágenes de varios años, se podrían detectar los cambios en la deforestación y en dónde están sucediendo.

## 3. Herramientas para la implementación del proyecto
- Python y sus librerías básicas
- Tensorflow y Keras para la creación de la red neuronal
- Github para alojar el proyecto
- Docker para desplegar el proyecto

## 4. Orígenes de datos
Se usará el conjunto de datos de Kaggle titulado "Planet: Understanding the Amazon from Space" el cual cuenta con
imágenes de cuatro canales (rojo, verde, azul, infrarrojo) ya etiquetadas de imágenes satelitales de la región. 
También intentaré encontrar otro conjunto de datos más reciente, posiblemente de Earth Engine Data Catalog de Google,
para ver las diferencias.

## 5. Principales actividades a realizar
1. Recolección de los conjuntos de datos.
2. Preprocesamiento de datos. En particular si se combinan datasets, hay que hacer que todas las imágenes sean
del mismo tamaño, tengan los mismos canales, y que las etiquetas sean las mismas.
3. Creación y ajuste de la red neuronal convolucional.
4. Evaluación del modelo y selección de hiperparámetros.
5. Crear una API con una interfaz de usuario.

## 6. Observaciones y comentarios generales del Alumno
Por lo pronto tengo contemplado hacer el proyecto con el dataset propuesto (de Kaggle). Pero primero voy a buscar en
Earth Engine Data Catalog de Google para ver si hay un dataset más reciente y con más información.

## 7. Observaciones y resultado de la revisión del profesor
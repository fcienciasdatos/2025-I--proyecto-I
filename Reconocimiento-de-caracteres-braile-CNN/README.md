---

# Proyecto 2025-1 - Reconocimiento de Caracteres Braille

Este proyecto, titulado **2025-1-proyecto-1**, se centra en el reconocimiento de caracteres Braille a través de una red neuronal convolucional (CNN). El objetivo es crear una herramienta de aprendizaje profundo que facilite la interpretación de las letras en el sistema Braille a partir de imágenes digitales.

## Estructura del Proyecto

- **Carpeta `beta/`**: Contiene el generador del modelo CNN, implementado en el archivo `modelo.py`.
- **Directorio `Braille_Dataset/`**: Incluye las imágenes de entrada en formato Braille que serán utilizadas para el entrenamiento y la validación del modelo.
- **Directorio `images/`**: Generado automáticamente, clasifica las imágenes por letra, lo que facilita el uso de un generador de datos con Keras para el entrenamiento.
- **Archivo `main.py`**: Contiene la aplicación FastAPI que se encarga de recibir imágenes y devolver las letras predichas.

## Dataset

Este proyecto utiliza un dataset combinado, creado a partir de:

- **Imágenes digitales de Kaggle**
- **Dataset de Angelina-TS**, disponible en [este enlace](https://github.com/WvdL12/Braille-Dataset/tree/main)

La combinación de estos datasets produce un total de **53,968 datos de entrenamiento** que representan las 26 letras del abecedario inglés (sin incluir la letra ñ, acentos ni caracteres especiales).

### Obtener el Dataset Final

Puedes descargar el dataset finalizado directamente desde la terminal usando el siguiente enlace:

```bash
wget https://www.dropbox.com/scl/fi/db0hdt9bt72a3xs76kwfq/Braille_Dataset.zip?rlkey=nks0hld1dq2bx1hr84ocej45a&st=l8t47raa&dl=0 -O Braille_Dataset.zip
```

Este comando descargará el archivo `Braille_Dataset.zip` en el directorio actual.

Puede descomprimir el archivo con su programa de preferencia

### Modelo Preentrenado

Si no deseas entrenar el modelo desde cero, puedes obtener un modelo ya entrenado desde el siguiente enlace:

[Modelo Preentrenado](https://www.dropbox.com/scl/fi/28ybvdjqxd65p7u80a25k/BrailleNet.keras?rlkey=drh4vnxvkly5jvx6yyoyvk1a1&st=ocqu5wp2&dl=0)

## Descripción del Modelo - `modelo.py`

El archivo `modelo.py` contiene la implementación principal de la red neuronal convolucional para el reconocimiento de caracteres Braille. A continuación, se detallan algunos aspectos clave de la configuración del modelo.

### Librerías Utilizadas

El proyecto requiere varias librerías, tales como:
- **Numpy** y **Pandas** para operaciones matemáticas y manipulación de datos.
- **Matplotlib** para visualización y gráficos.
- **Keras** para el desarrollo de la CNN.
- **TensorFlow** para la manipulación de datos de imagen y los procesos de preprocesamiento.
- **FastAPI** y **Uvicorn** para construir y ejecutar la API.

### Preparación de los Datos

1. **Organización del Dataset**: Las imágenes de letras Braille se copian y organizan en carpetas correspondientes a cada letra (de `A` a `Z`).
2. **Aumento de Imágenes**: Usamos el `ImageDataGenerator` de Keras para aplicar transformaciones de aumento de datos, como rotaciones y recortes, aumentando así la robustez del modelo.

### Arquitectura del Modelo

La arquitectura de la CNN se compone de:
- **Entrada**: Imágenes de 28x28 píxeles en formato RGB.
- **Capas Convolucionales**: Se utilizan capas separables convolucionales para extraer características, combinadas con capas de pooling para reducir la dimensionalidad.
- **Capas Densas**: Después de un `GlobalMaxPooling`, se agregan capas densas con activación `LeakyReLU` y regularización L2.
- **Salida**: Una capa densa con 26 unidades y activación `softmax` para clasificar las 26 letras del alfabeto.

### Entrenamiento del Modelo

- **Configuración de Entrenamiento**: El modelo está configurado para entrenar durante 666 épocas, con el uso de varios callbacks que permiten detener el entrenamiento si no se observan mejoras:
  - `ModelCheckpoint`: Guarda el mejor modelo durante el entrenamiento.
  - `ReduceLROnPlateau`: Reduce la tasa de aprendizaje si no hay mejoras en la precisión.
  - `EarlyStopping`: Finaliza el entrenamiento si no hay progreso después de un número de épocas.

## Ejecución en Docker

### Crear el Dockerfile

Asegúrate de tener un archivo llamado `Dockerfile` en la raíz del proyecto con el siguiente contenido:

```dockerfile
# Usar una imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Construir y Ejecutar el Contenedor

Ejecuta los siguientes comandos en la terminal para construir y correr el contenedor Docker:

```bash
# Construir la imagen
docker build -t braille-recognition .

# Ejecutar el contenedor
docker run -p 8000:8000 braille-recognition
```

## Uso de la API

Una vez que el contenedor esté en funcionamiento, puedes hacer peticiones a la API en `http://localhost:8000/predict/` para subir imágenes y recibir predicciones de letras en formato JSON.

### Enlace Público

Si deseas usar la API de manera pública, puedes acceder a la API en el siguiente enlace: [Braille_API](http://40.233.16.134:8000/docs#/default/predict_predict__post).

### Endpoint para Subir Imágenes

- **Método**: `POST`
- **URL**: `/predict/`
- **Parámetro**: `file` (Archivo de imagen a predecir)

### Ejemplo de Uso

Puedes usar herramientas como Postman o `curl` para probar el endpoint:

```bash
curl -X POST "http://localhost:8000/predict/" -F "file=@ruta/a/tu/imagen.jpg"
```

## Resultados

Durante el entrenamiento, el modelo mostrará la precisión y la pérdida para cada época, tanto en el conjunto de entrenamiento como en el de validación. Los resultados serán guardados en el archivo `BrailleNet.keras`.

## Requisitos

- Python 3.11 o superior
- Docker

## Contribuciones

Este proyecto fue realizado por Karla Romina Juárez Torres como parte del curso Proyecto 1 "Clasificador de imágenes con redes neuronales" del semestre 2025-1 de la Facultad de Ciencias para la licenciatura de Matematicas Aplicadas de la Universidad Nacional Autonoma de México, enfocándose en el reconocimiento de caracteres Braille con redes CNN.

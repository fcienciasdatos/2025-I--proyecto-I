'''
Este es un programa menor usado en testeo, usa a las imagenes de la carpeta /imagenes_a_predecir/
y las evalua en el modelo.
'''


import os  # Importar el módulo para operaciones del sistema
import numpy as np  # Importar NumPy para operaciones matemáticas
import matplotlib.pyplot as plt  # Importar Matplotlib para graficar
from tensorflow.keras.preprocessing import image  # Importar funciones de preprocesamiento de imágenes de Keras
from keras.models import load_model  # Importar la función para cargar el modelo

# Cargar el modelo previamente entrenado
model = load_model('BrailleNet.keras')

# Función para predecir la letra en una imagen
def predecir_letra(ruta_imagen):
    # Cargar y procesar la imagen
    img = image.load_img(ruta_imagen, target_size=(28, 28))  # Cargar la imagen con tamaño 28x28
    img_array = image.img_to_array(img)  # Convertir la imagen a un array
    img_array = np.expand_dims(img_array, axis=0)  # Expandir dimensiones para la predicción
    
    # Realizar la predicción
    prediccion = model.predict(img_array)  # Predecir
    letra_predicha = np.argmax(prediccion, axis=1)  # Obtener la clase con la mayor probabilidad
    
    return letra_predicha[0]  # Devolver la letra predicha

# Directorio donde se encuentran las imágenes para predecir
directorio_imagenes = './imagenes_a_predecir/'  # Cambia esto a la ruta de tus imágenes

# Listar todas las imágenes en el directorio
for archivo in os.listdir(directorio_imagenes):
    if archivo.endswith('.jpg') or archivo.endswith('.png'):  # Comprobar si el archivo es una imagen
        ruta_imagen = os.path.join(directorio_imagenes, archivo)  # Obtener la ruta completa de la imagen
        letra = predecir_letra(ruta_imagen)  # Predecir la letra
        print(f'Imagen: {archivo}, Letra Predicha: {letra}')  # Mostrar el resultado

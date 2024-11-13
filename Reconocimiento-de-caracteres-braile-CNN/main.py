from fastapi import FastAPI, UploadFile, File, HTTPException
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io
import uvicorn
import os

app = FastAPI()

# Función para procesar y predecir la letra en una imagen
def predecir_letra(imagen_bytes):
    try:
        # Cargar el modelo en cada solicitud
        model = load_model('BrailleNet.keras')
        
        # Convertir la imagen a blanco y negro, tamaño 28x28 y array
        img = Image.open(io.BytesIO(imagen_bytes)).convert('RGB').resize((28, 28))
        img_array = img_to_array(img)  # Convertir imagen a array
        img_array = np.expand_dims(img_array, axis=0)  # Expandir dimensiones para la predicción
        #img_array /= 255.0  # Normalizar a [0, 1]

        # Realizar la predicción
        prediccion = model.predict(img_array)  # Predecir
        letra_predicha = np.argmax(prediccion, axis=1)  # Obtener la clase con la mayor probabilidad
        
        return chr(ord('A') + letra_predicha[0])  # Convertir índice a letra del alfabeto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

# Endpoint para subir una imagen y obtener la predicción
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Leer la imagen cargada
    imagen_bytes = await file.read()
    
    # Realizar la predicción de la letra
    letra_predicha = predecir_letra(imagen_bytes)
    
    # Retornar la letra predicha como respuesta JSON
    return {"letra_predicha": letra_predicha}

def limpiar_salida_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')




# Iniciar uvicorn con logging limitado

if __name__ == "__main__":
    limpiar_salida_terminal()

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="error")
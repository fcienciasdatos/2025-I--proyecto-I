# Usa una imagen base de Python 3.9
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /braille_app

# Copia los archivos de la aplicación al directorio de trabajo
COPY . .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir fastapi uvicorn pillow tensorflow numpy python-multipart

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

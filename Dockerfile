# Usa una imagen base de Python
FROM python:3.10

# Instala las dependencias del sistema necesarias para pyodbc
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    unixodbc \
    libodbc1 \
    && rm -rf /var/lib/apt/lists/*

# Crea un directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

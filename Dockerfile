# Usa una imagen base de Python
FROM python:3.10

# Instala las dependencias del sistema necesarias para pyodbc y el driver ODBC de Microsoft
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    unixodbc \
    libodbc1 \
    curl \
    gnupg

# Agrega la clave de Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Agrega el repositorio de Microsoft
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Actualiza los paquetes e instala el driver ODBC de Microsoft
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Limpia la caché de apt
RUN rm -rf /var/lib/apt/lists/*

# Crea un directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# FastAPI Login Project

Este es un proyecto de backend desarrollado con FastAPI y SQL Server, que incluye funcionalidades básicas de registro y login de usuarios. 
El proyecto también incluye un frontend básico para la vista del login.

## Características

- **Backend**: Desarrollado con FastAPI y conectado a una base de datos SQL Server.
- **Frontend**: Vista básica del login.
- **Registro de Usuarios**: Permite registrar nuevos usuarios en la base de datos.
- **Login de Usuarios**: Permite validar las credenciales de los usuarios registrados.

## Requisitos

- Python 3.10 o superior
- SQL Server
- FastAPI
- Uvicorn
- PyODBC

## Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2. Crea y activa un entorno virtual:
   python -m venv venv
  .\venv\Scripts\activate  # En Windows
  source venv/bin/activate  # En macOS/Linux

4. Instala las dependencias:
   pip install -r requirements.txt

#Uso
   
1. Inicia el servidor FastAPI:
   uvicorn main:app --reload
2. Claro, aquí tienes un ejemplo de un archivo `README.md` para tu proyecto:

```markdown
# FastAPI Login Project

Este es un proyecto de backend desarrollado con FastAPI y SQL Server, que incluye funcionalidades básicas de registro y login de usuarios. El proyecto también incluye un frontend básico para la vista del login.

## Características

- **Backend**: Desarrollado con FastAPI y conectado a una base de datos SQL Server.
- **Frontend**: Vista básica del login.
- **Registro de Usuarios**: Permite registrar nuevos usuarios en la base de datos.
- **Login de Usuarios**: Permite validar las credenciales de los usuarios registrados.

## Requisitos

- Python 3.10 o superior
- SQL Server
- FastAPI
- Uvicorn
- PyODBC

## Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crea y activa un entorno virtual:

   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En macOS/Linux
   ```

3. Instala las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

4. Configura la conexión a la base de datos en el archivo 

main.py

:

   ```python
   DATABASE_CONFIG = {
       "server": "tu_direccion_ip_publica,1433",  # Reemplaza con tu dirección IP pública y el puerto 1433
       "database": "Logins",
       "username": "sa",
       "password": "123456",
       "driver": "ODBC Driver 17 for SQL Server"
   }
   ```

## Uso

1. Inicia el servidor FastAPI:

   ```sh
   uvicorn main:app --reload
   ```

2. Abre tu navegador y ve a `http://localhost:8000/docs` para ver la documentación interactiva de la API.

## Endpoints

### Registro de Usuarios

- **URL**: `/register`
- **Método**: `POST`
- **Descripción**: Registra un nuevo usuario en la base de datos.
- **Cuerpo de la Solicitud**:

  ```json
  {
      "nombre_usuario": "Stiven",
      "contrasena": "12345678S"
  }
  ```

### Login de Usuarios

- **URL**: `/login`
- **Método**: `POST`
- **Descripción**: Valida las credenciales de un usuario.
- **Cuerpo de la Solicitud**:

  ```json
  {
      "nombre_usuario": "Stiven",
      "contrasena": "12345678S"
  }
  ```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```

Este archivo `README.md` proporciona una descripción general de tu proyecto, incluyendo las características, requisitos, instalación, uso, endpoints, despliegue, contribuciones y licencia. Asegúrate de reemplazar `tu-usuario` y `tu-repositorio` con los nombres correctos de tu usuario y repositorio en GitHub.
Este archivo `README.md` proporciona una descripción general de tu proyecto, incluyendo las características, requisitos, instalación, uso, endpoints, despliegue, contribuciones y licencia. Asegúrate de reemplazar `tu-usuario` y `tu-repositorio` con los nombres correctos de tu usuario y repositorio en GitHub.

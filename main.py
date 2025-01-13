from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyodbc

app = FastAPI()

# Configuración de la conexión a la base de datos
DATABASE_CONFIG = {
    "server": "localhost",
    "database": "Logins",
    "username": "sa",           # Cambia esto por tu usuario de SQL Server
    "password": "123456",       # Cambia esto por tu contraseña de SQL Server
    "driver": "ODBC Driver 17 for SQL Server"
}

# Función para obtener la conexión
def get_db_connection():
    conn_str = (
        f"DRIVER={DATABASE_CONFIG['driver']};"
        f"SERVER={DATABASE_CONFIG['server']};"
        f"DATABASE={DATABASE_CONFIG['database']};"
        f"UID={DATABASE_CONFIG['username']};"
        f"PWD={DATABASE_CONFIG['password']}"
    )
    return pyodbc.connect(conn_str)

# Modelo de solicitud para el login
class LoginRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

# Endpoint para validar el login
@app.post("/login")
def validar_login(request: LoginRequest):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ejecutar el procedimiento almacenado
        cursor.execute("EXEC SP_ValidarLogin ?, ?", request.nombre_usuario, request.contrasena)
        result = cursor.fetchone()

        if result:
            mensaje = result[0]  # Primer columna del resultado devuelto por el SP
            if mensaje == "Login exitoso":
                return {"mensaje": mensaje, "usuario": request.nombre_usuario}
            else:
                raise HTTPException(status_code=401, detail=mensaje)
        else:
            raise HTTPException(status_code=500, detail="Error inesperado en el servidor")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

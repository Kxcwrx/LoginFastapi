from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyodbc

app = FastAPI()


DATABASE_CONFIG = {
    "server": "localhost",
    "database": "Logins",
    "username": "sa",           
    "password": "123456",       
    "driver": "ODBC Driver 17 for SQL Server"
}

def get_db_connection():
    conn_str = (
        f"DRIVER={DATABASE_CONFIG['driver']};"
        f"SERVER={DATABASE_CONFIG['server']};"
        f"DATABASE={DATABASE_CONFIG['database']};"
        f"UID={DATABASE_CONFIG['username']};"
        f"PWD={DATABASE_CONFIG['password']}"
    )
    return pyodbc.connect(conn_str)

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

        cursor.execute("EXEC SP_ValidarLogin ?, ?", request.nombre_usuario, request.contrasena)
        result = cursor.fetchone()

        if result:
            mensaje = result[0] 
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

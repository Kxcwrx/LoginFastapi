from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyodbc
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configura CORS para permitir solicitudes de cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta la carpeta "frontend" (que contiene tus archivos estáticos) como "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

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
                raise HTTPException(status_code="", detail="Usuario o contraseña incorrectos")
        else:
            raise HTTPException(status_code=500, detail="Error inesperado en el servidor")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


class RegisterRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

@app.post("/register")
def registrar_usuario(request: RegisterRequest):
    conn = None
    cursor = None
    try:
        # Validación del lado del servidor para la contraseña
        if len(request.contrasena) < 6 or not any(c.isalpha() for c in request.contrasena) or not any(c.isdigit() for c in request.contrasena):
            raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 6 caracteres, incluyendo al menos una letra y un número.")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("EXEC SP_RegistrarUsuario ?, ?", request.nombre_usuario, request.contrasena)
        conn.commit()

        # Enviar una respuesta JSON indicando éxito
        return {"mensaje": "Registro exitoso"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
import base64
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
from sqlalchemy import create_engine

# Decodificación de imágenes en base64
def decode_base64_image(base64_str):
    bd.png = base64.b64decode(base64_str)
    image = Image.open(BytesIO(bd.png))
    return image

# Generación de consultas SQL a partir de descripciones en texto usando la API de Ollama
def generate_sql_from_text(text_description):
    api_url = "http://localhost:11434/api/generate"  # Reemplaza con la URL real de la API de Ollama
    headers = {
        "Content-Type": "application/json",
        "Authorization": "~/.ollama/id_ed25519.pub"  # Reemplaza con tu API key
    }
    payload = {
        "prompt": f"Generate an SQL query based on the following description: {text_description}"
    }
    response = requests.post(api_url, json=payload, headers=headers)
    response_data = response.json()
    sql_query = response_data['sql_query']
    return sql_query

# Interacción con la base de datos
def query_database(sql_query, db_url):
    # Crear una conexión a la base de datos
    engine = create_engine(db_url)
    with engine.connect() as connection:
        df = pd.read_sql_query(sql_query, connection)
    return df

# Procesamiento de entrada del usuario
def process_user_input(text_input, base64_image=None):
    if base64_image:
        image = decode_base64_image(base64_image)
        # Aquí se podrían hacer operaciones con la imagen si es necesario
        
    sql_query = generate_sql_from_text(text_input)
    db_url = 'https://replit.com/@KFPympex/vistas'  # URL de la base de datos
    results_df = query_database(sql_query, db_url)
    
    return results_df

# Ejemplo de uso
text_input = "Obtener todos los registros de la tabla usuarios donde la edad sea mayor a 30"
base64_image = None  # Aquí iría la cadena en base64 de la imagen, si aplica
results_df = process_user_input(text_input, base64_image)

print(results_df.head())
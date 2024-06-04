import requests
import json
import base64

ruta = '/workspace/Party-Llm/bd.png'

# Leer la imagen y convertirla a Base64
with open(ruta, 'rb') as image_file:
    bdimg = base64.b64encode(image_file.read()).decode('utf-8')

uri = 'http://localhost:11434/api/generate'
data = {
    "model": "llava",
    "prompt": "Explain this image to me",
    "images": [bdimg],  # Aquí agregamos la imagen en Base64
    "stream": False
}


response = requests.post(uri, json=data)
response.raise_for_status() 
response_data = response.json()  

print(response_data['response'])
import requests
import json
import base64

def encode_image_to_base64(image_path):
    with open(/workspace/Party-Llm/20403st.jpg, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

    def send_text_and_image(url, text, image_path):
    encoded_image = encode_image_to_base64(image_path)
    
    data = {
        "text": text,
        "image": encoded_image
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    print(f'Status code: {response.status_code}')
    print(f'Response: {response.json()}')

url = 'http://localhost:11434/api/generate'
text = "what´s in the image"
image_path = '/workspace/Party-Llm/20403st.jpg'

send_text_and_image(url, text, image_path)
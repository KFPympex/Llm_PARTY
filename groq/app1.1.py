import json 
import requests

uri = "https://api.groq.com/openai/v1/chat/completions"

API_KEY = "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"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


prompt= input("PROMPT:")

data = {
    "messages": [
           {
             "role": "system",
             "content": "Eres un profesor profesional en la materia de probabilidad y estadística"
           },
           {
             "role": "user",
             "content": f"{prompt}"
           },
         ],
         "model": "mixtral-8x7b-32768",
         "temperature": 0.7,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": False,
         "stop": None
       }



response = requests.post (uri,json=data,headers=headers)

response = json.loads (response.text)
print (response['choices'][0]['message']['content'])

import requests
import json

uri = 'http://localhost:11434/api/generate'
data= {
  "model": "tinyllama",
  "prompt": "what´s in this image?",
  "stream": False
}



response = requests.post(uri, json = data)

response = json.loads(response.text)

print(response['response'])
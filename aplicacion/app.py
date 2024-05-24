import requests

url = 'http://127.0.0.1:11434/api/generate'
myobj= {
"model": "tinyllama",
  "prompt": "por qué el cielo es azúl?",
  "stream": False
  }


x = requests.post(url, json = myobj)

print(x.text)
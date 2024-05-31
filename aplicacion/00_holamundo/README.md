# 1. Documentacion
[python requests](https://www.w3schools.com/python/ref_requests_post.asp)

[python json](https://www.w3schools.com/python/python_json.asp)

[ejemplo de uso de llama2](https://ollama.com/library/llama2)

## 2. Ejemplo con curl
````shell
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"Why is the sky blue?"
 }'
````

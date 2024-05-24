# Party-Llm

## 1. Instalacion de ollama
---curl -fsSL https://ollama.com/install.sh | sh#---

## 2. Ejecutar el servidor
---ollama serve---

## 3. Instalacion de Ollama
---ollama run tinyllama---

## 4. ctrl-d: para salir del modo chat


## 5. Modo generativo
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿por qué el cielo es azúl?"
}'


curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "por qué el cielo es azúl?",
  "stream": false
}'
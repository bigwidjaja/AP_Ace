import requests
import json

url = "http://127.0.0.1:11434/api/generate"

data = { 
        "model": "deepseek-r1:7b",
        "prompt": "What is 3 + 3?",
        "stream": False }

response = requests.post(url, json=data)

print(response.json())




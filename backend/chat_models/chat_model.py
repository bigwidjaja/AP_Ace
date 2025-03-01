import requests
import json

url = "http://127.0.0.1:11434/api/generate"
prompt = input()
data = { 
        "model": "deepseek-r1:7b",
        "prompt": prompt,
        "stream": False }

response = requests.post(url, json=data)
response_json = response.json()
output = response_json["response"].split("</think>")
print(output[-1])





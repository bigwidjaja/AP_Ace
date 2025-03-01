import requests
import json

def answer_prompt(prompt):
    data = { 
            "model": "deepseek-r1:7b",
            "prompt": prompt,
            "stream": False }

    response = requests.post(url, json=data)
    response_json = response.json()
    output = response_json["response"].split("</think>")
    return output[-1]

if __name__ == '__main__':
    url = "http://127.0.0.1:11434/api/generate"
    prompt = input()
    print(answer_prompt(prompt))




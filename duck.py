# docker run -d -p 8000:8000  rasa/duckling
import requests

def clearData(input: str, stopWord = "") -> str:
    data = {
    'locale': 'pl_PL',
    'text': input
    }
    response = requests.post('http://localhost:8000/parse', data=data)
    for entity in response.json():
        input = input.replace(entity['body'], stopWord)

    return input.strip()

input =  "test dwa testx"
print(clearData(input))    

# docker run -d -p 8000:8000  rasa/duckling
import requests

def clearData(input: str, dims=["number"], stopWord="") -> str:
    data = {
        'locale': 'pl_PL',
        'text': input
    }
    response = requests.post('http://localhost:8000/parse', data=data)
    for entity in response.json():
        if(entity['dim'] in dims):
            input = input.replace(entity['body'], stopWord)

    return " ".join(input.split())


input = "x trzy   test  dwa testx   maj xx"
print(clearData(input))

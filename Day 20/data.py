import requests 
import json
value = requests.get("https://jsonplaceholder.typicode.com/todos/1")
obj = json.loads(value.text)
print(obj["userId"])
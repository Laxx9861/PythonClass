import requests 
import json
value = requests.get("https://jsonguide.technologychannel.org/quotes.json")
listofobj = json.loads(value.text)


for i in listofobj:
    print(i["text"])

import json
import requests
import geojson
b1 = "https:
with open('datas.json') as json_data:
    b2 = json.load(json_data)
for facteur in b2:
    b3 = facteur['adresse'].replace(" ", "+")
    b4 = requests.get(b1+b3)
    b5 = geojson.loads(b4.text)
    b6 = b5['features'][0]['geometry']['coordinates']
    facteur['latitude']=b6[1]
    facteur['longitude']=b6[0]
with open('facteurs_localisation.json', 'w') as g:
    json.dump(b2, g)
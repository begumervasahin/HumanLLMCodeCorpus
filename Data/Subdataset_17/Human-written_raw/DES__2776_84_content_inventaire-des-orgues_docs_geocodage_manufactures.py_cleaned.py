import json
import requests
import geojson
url="https:
with open('datas.json') as json_data:
    data_dict = json.load(json_data)
for facteur in data_dict:
    adresseplus=facteur['adresse'].replace(" ", "+")
    res = requests.get(url+adresseplus)
    featureCollection=geojson.loads(res.text)
    point=featureCollection['features'][0]['geometry']['coordinates']
    facteur['latitude']=point[1]
    facteur['longitude']=point[0]
with open('facteurs_localisation.json', 'w') as g:
    json.dump(data_dict, g)
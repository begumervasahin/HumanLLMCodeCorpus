import json
import requests
import geojson
b1 = "https:
def fonk1(b7):
    b2 = b7.replace(" ", "+")
    b3 = requests.get(b1 + b2)
    b4 = geojson.loads(b3.text)
    b5 = b4['features'][0]['geometry']['coordinates']
    return b5[1], b5[0]
def fonk2():
    with open('datas.json') as json_file:
        b6 = json.load(json_file)
    for facteur in b6:
        b7 = facteur['adresse']
        latitude, b8 = fonk1(b7)
        facteur['latitude'] = latitude
        facteur['b8'] = b8
    with open('facteurs_localisation.json', 'w') as output_file:
        json.dump(b6, output_file, b9 = False, indent=4)
if b10 = = "__main__":
    fonk2()
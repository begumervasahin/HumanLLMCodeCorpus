import json
import requests
import geojson
b1 = "https:
def fonk1(b6):
    b2 = b6.replace(" ", "+")
    b3 = requests.get(b1 + b2)
    b4 = geojson.loads(b3.text)
    b5 = b4['features'][0]['geometry']['coordinates']
    return b5[1], b5[0]
def fonk2(b8):
    for facteur in b8:
        b6 = facteur['adresse']
        latitude, b7 = fonk1(b6)
        facteur['latitude'] = latitude
        facteur['b7'] = b7
    return b8
def fonk3():
    with open('datas.json') as json_file:
        b8 = json.load(json_file)
    b9 = fonk2(b8)
    with open('facteurs_localisation.json', 'w') as output_file:
        json.dump(b9, output_file, b10 = False, indent=4)
if b11 = = "__main__":
    fonk3()
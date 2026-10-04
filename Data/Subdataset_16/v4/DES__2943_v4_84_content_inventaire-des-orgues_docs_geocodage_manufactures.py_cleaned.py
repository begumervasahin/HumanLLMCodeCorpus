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
def fonk2(b9):
    for entry in b9:
        b6 = entry['adresse']
        latitude, b7 = fonk1(b6)
        entry['latitude'] = latitude
        entry['b7'] = b7
    return b9
def fonk3():
    with open('datas.json', 'r', b8 = 'utf-8') as json_file:
        b9 = json.load(json_file)
    b10 = fonk2(b9)
    with open('facteurs_localisation.json', 'w', b8 = 'utf-8') as output_file:
        json.dump(b10, output_file, b11 = False, indent=4)
if b12 = = "__main__":
    fonk3()
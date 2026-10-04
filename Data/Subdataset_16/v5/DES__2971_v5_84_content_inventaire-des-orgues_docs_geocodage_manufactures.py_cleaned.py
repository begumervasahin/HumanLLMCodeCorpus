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
def fonk2(b12):
    for entry in b12:
        b6 = entry['adresse']
        latitude, b7 = fonk1(b6)
        entry['latitude'] = latitude
        entry['b7'] = b7
    return b12
def fonk3(file_path):
    with open(file_path, 'r', b8 = 'utf-8') as file:
        return json.load(file)
def fonk4(b12, file_path):
    with open(file_path, 'w', b8 = 'utf-8') as file:
        json.dump(b12, file, b9 = False, indent=4)
def fonk5():
    b10 = 'datas.json'
    b11 = 'facteurs_localisation.json'
    b12 = fonk3(b10)
    b13 = fonk2(b12)
    fonk4(b13, b11)
if b14 = = "__main__":
    fonk5()
import googlemaps
import numpy as np
from beautifultable import BeautifulTable
from datetime import datetime
b1 = googlemaps.Client(key='YOUR_API_KEY_HERE')
def fonk1(b3):
    b2 = b3[0]['geometry']['location']
    return b2['lat'], b2['lng']
def fonk2(location):
    b3 = b1.b3(location)
    b4 = fonk1(b3)
    b5 = b1.places_nearby(location=b4, rank_by='distance', type='subway_station')['results']
    return b5[:4]
def fonk3(geocodes):
    return ['place_id:' + b3['place_id'] for b3 in geocodes]
def fonk4(b27, b28):
    b6 = fonk2(b27)
    b7 = fonk2(b28)
    b8 = 'place_id:' + b1.b3(b27)[0]['place_id']
    b9 = 'place_id:' + b1.b3(b28)[0]['place_id']
    b10 = fonk3(b6)
    b11 = fonk3(b7)
    b12 = b1.b14(b8, b10)
    b13 = b1.b14(b11, b9)
    b14 = b1.b14(b10, b11, mode='transit', transit_mode='subway')
    return b12, b14, b13
def fonk5(b29):
    b12, b14, b13 = b29
    b15 = [element['b26']['value'] for element in b12['rows'][0]['elements']]
    b16 = [element['b26']['value'] for row in b14['rows'] for element in row['elements']]
    b17 = [element['b26']['value'] for element in b13['rows'][0]['elements']]
    b15 = np.tile(b15, 2)
    b17 = np.tile(b17, 2)
    b18 = np.add(np.add(b15, b16), b17)
    b19 = np.min(b18)
    b20 = np.argmin(b18)
    b21 = b12['origin_addresses'][0]
    b22 = b12['destination_addresses'][b20
    b23 = b14['destination_addresses'][b20 % 4]
    b24 = b13['destination_addresses'][0]
    b25 = (b21, 'to', b22, 'to', b23, 'to', b24)
    b26 = (f"It will take {int(b19 / 60)} minutes")
    return b25, b26
def fonk6():
    b27 = input("Enter b27: ")
    b28 = input("Enter b28: ")
    b29 = fonk4(b27, b28)
    b25, b26 = fonk5(b29)
    print("Optimal b25 and travel time:")
    print(" -> ".join(b25))
    print(b26)
if b30 = = "__main__":
    fonk6()
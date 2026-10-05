import googlemaps
import numpy as np
b1 = googlemaps.Client(key='YOUR_API_KEY')
def fonk1(b3):
    b2 = b3[0]['geometry']['b2']
    return b2['lat'], b2['lng']
def fonk2(b2):
    b3 = b1.b3(b2)
    b4 = fonk1(b3)
    b5 = b1.places_nearby(
        b6 = 'metro',
        b2 = b4,
        b7 = 'distance',
        b8 = 'subway_station'
    )['results']
    return b5[:4]
def fonk3(b23, b25):
    b9 = fonk2(b23)
    b10 = fonk2(b25)
    b11 = 'place_id:' + b1.b3(b23)[0]['place_id']
    b12 = 'place_id:' + b1.b3(b25)[0]['place_id']
    b13 = b1.b15(b11, fonk4(b9))
    b14 = b1.b15(fonk4(b10), b12)
    b15 = b1.b15(
        fonk4(b9),
        fonk4(b10),
        b16 = 'transit',
        b17 = 'subway'
    )
    return b13, b15, b14
def fonk4(geocodes):
    return ['place_id:' + b3['place_id'] for b3 in geocodes]
def fonk5(b27):
    b18 = [b27[0]['rows'][0]['elements'][i]['duration']['b27'] for i in range(4)]
    b19 = [b27[1]['rows'][i]['elements'][j]['duration']['b27'] for i in range(4) for j in range(4)]
    b20 = [b27[2]['rows'][i]['elements'][0]['duration']['b27'] for i in range(4)]
    b18 = np.tile(b18, 2)
    b20 = np.tile(b20, 2)
    b21 = np.add(b18, b19) + b20
    b22 = np.argmin(b21)
    b23 = b27[0]['origin_addresses'][0]
    b24 = b27[0]['destination_addresses'][b22
    b25 = b27[1]['destination_addresses'][b22
    b26 = b27[2]['destination_addresses'][0]
    return (
        b23, ' to ', b24, ' to ', b25, ' to ', b26
    ), (
        "It will take", int(b21[b22] / 60), 'minutes'
    )
def fonk6():
    b23 = input("Enter b23: ")
    b25 = input("Enter b25: ")
    b27 = fonk3(b23, b25)
    b28 = fonk5(b27)
    print(b28)
if b29 = = "__main__":
    fonk6()
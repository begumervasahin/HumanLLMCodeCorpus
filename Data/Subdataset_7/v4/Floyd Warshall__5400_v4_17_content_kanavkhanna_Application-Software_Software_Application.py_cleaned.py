import googlemaps
import numpy as np
from beautifultable import BeautifulTable
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
def fonk3(b24, b26):
    b9 = fonk2(b24)
    b10 = fonk2(b26)
    b11 = 'place_id:' + b1.b3(b24)[0]['place_id']
    b12 = 'place_id:' + b1.b3(b26)[0]['place_id']
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
def fonk5(b28):
    o_to_metro_times, b15, b18 = b28
    b19 = [o_to_metro_times['rows'][0]['elements'][i]['duration']['value'] for i in range(4)]
    b20 = [b15['rows'][i]['elements'][j]['duration']['value'] for i in range(4) for j in range(4)]
    b21 = [b18['rows'][i]['elements'][0]['duration']['value'] for i in range(4)]
    b19 = np.tile(b19, 2)
    b21 = np.tile(b21, 2)
    b22 = np.add(np.add(b19, b20), b21)
    b23 = np.argmin(b22)
    b24 = b28[0]['origin_addresses'][0]
    b25 = b28[0]['destination_addresses'][b23
    b26 = b28[1]['destination_addresses'][b23
    b27 = b28[2]['destination_addresses'][0]
    return (
        b24, ' to ', b25, ' to ', b26, ' to ', b27
    ), (
        "Total travel time:", int(b22[b23] / 60), 'minutes'
    )
def fonk6():
    b24 = input("Enter b24: ")
    b26 = input("Enter b26: ")
    b28 = fonk3(b24, b26)
    route, b29 = fonk5(b28)
    print(route)
    print(b29)
if b30 = = "__main__":
    fonk6()
import googlemaps
import numpy as np
b1 = googlemaps.Client(key='YOUR_API_KEY')
def fonk1(b3):
    b2 = b3[0]['geometry']['b2']
    return b2['lat'], b2['lng']
def fonk2(b2):
    b3 = b1.geocode(b2)
    b4 = fonk1(b3)
    b5 = b1.places_nearby(
        b6 = 'metro',
        b2 = b4,
        b7 = 'distance',
        b8 = 'subway_station'
    )['results']
    return b5[:4]
def fonk3(b28, b29):
    b9 = fonk2(b28)
    b10 = fonk2(b29)
    b11 = 'place_id:' + b1.geocode(b28)[0]['place_id']
    b12 = 'place_id:' + b1.geocode(b29)[0]['place_id']
    b13 = b1.b15(b11, fonk4(b9))
    b14 = b1.b15(fonk4(b10), b12)
    b15 = b1.b15(
        fonk4(b9),
        fonk4(b10),
        b16 = 'transit',
        b17 = 'subway'
    )
    return b13, b15, b14
def fonk4(geocode_results):
    return ['place_id:' + result['place_id'] for result in geocode_results]
def fonk5(b30):
    o_to_metro_times, metro_to_d_times, b18 = b30
    b19 = [result['duration']['value'] for result in o_to_metro_times['rows'][0]['elements']]
    b20 = [result['duration']['value'] for row in metro_to_d_times['rows'] for result in row['elements']]
    b21 = [result['duration']['value'] for result in b18['rows'][0]['elements']]
    b19 = np.tile(b19, 2)
    b21 = np.tile(b21, 2)
    b22 = np.add(np.add(b19, b20), b21)
    b23 = np.argmin(b22)
    b24 = b30[0]['origin_addresses'][0]
    b25 = b30[0]['destination_addresses'][b23
    b26 = b30[1]['destination_addresses'][b23
    b27 = b30[2]['destination_addresses'][0]
    return (
        b24, ' to ', b25, ' to ', b26, ' to ', b27
    ), (
        "It will take", int(b22[b23] / 60), 'minutes'
    )
def fonk6():
    b28 = input("Enter b28: ")
    b29 = input("Enter b29: ")
    b30 = fonk3(b28, b29)
    b31 = fonk5(b30)
    print(b31)
if b32 = = "__main__":
    fonk6()
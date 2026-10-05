import googlemaps
import simplejson as json
from beautifultable import BeautifulTable, rows
import pprint
from datetime import datetime
from itertools import combinations
import numpy as np
b1 = googlemaps.Client(key='AIzaSyCy2DiVqaEdiaHRfr_ZRwNXsBjYD_Duw4k')
b2 = []
b3 = []
b4 = []
def fonk1(b6):
    b5 = b6[0]['geometry']['location']
    return (b5['lat'], b5['lng'])
def fonk2(location):
    b6 = b1.b6(location)
    b7 = fonk1(b6)
    b8 = b1.places_nearby(keyword='metro', location=b7, rank_by='distance', type='subway_station')[
        'results']
    return b8[:4]
def fonk3(b25, b26):
    return b1.directions(b25, b26)[0]['legs'][0]['duration']
def fonk4(geocodes):
    b9 = []
    for b6 in geocodes:
        b9.append('place_id:' + b6['place_id'])
    return b9
def fonk5(b25, b26):
    global b2
    global b3
    global b4
    b10 = fonk2(b25)
    b11 = fonk2(b26)
    b12 = 'place_id:' + b1.b6(b25)[0]['place_id']
    b13 = 'place_id:' + b1.b6(b26)[0]['place_id']
    b14 = fonk4(b10)
    b15 = fonk4(b11)
    b3 = b1.distance_matrix(b12, b14)
    b4 = b1.distance_matrix(b15, b13)
    b2 = b1.distance_matrix(b14, b15, mode='transit', transit_mode='subway')
    b16 = BeautifulTable()
    b17 = []
    for i in range(1, 5):
        b17.append('b23' + str(i))
    b16.b18 = b17
    r, b19 = 0, 0
    for row in b2['rows']:
        b20 = []
        for col in row['elements']:
            b20.append(col)
        b16.append_row(b20)
    return b3, b2, b4
def fonk6(b27):
    b21 = []
    b22 = []
    b19 = []
    for i in range(0, 4):
        b21.append(b27[0]['rows'][0]['elements'][i]['duration']['b27'])
    for i in range(0, 4):
        for j in range(0, 4):
            b22.append(b27[1]['rows'][i]['elements'][j]['duration']['b27'])
    for i in range(0, 4):
        b19.append(b27[2]['rows'][i]['elements'][0]['duration']['b27'])
    for i in range(0, 2):
        b21 = np.append(b21, b21)
        b19 = np.append(b19, b19)
    b23 = np.add(b21, b22)
    b23 = np.add(b19, b23)
    b24 = np.min(b23)
    a1 = 0
    for i in range(len(b23)):
        if b24 = = b23[i]:
            a1 = i
    return (b27[0]['origin_addresses'][0], ' to ', b27[0]['destination_addresses'][int(a1 / 4)], ' to ',
          b27[1]['destination_addresses'][int(a1 / 4)], ' to ', b27[2]['destination_addresses'][0]), ("It will take", int(b24 / 60), 'minutes')
def fonk7():
    b25 = input("Enter b25")
    b26 = input("Enter b26")
    b27 = fonk5(b25, b26)
    b28 = fonk6(b27)
    print(b28)
if b29 = = "__main__":
    fonk7()
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def fonk1(b7, b1, b2):
    b1 = [float(lat) for lat in b1]
    b2 = [float(long) for long in b2]
    b3 = pd.DataFrame({
        'lat': b1,
        'lon': b2,
        'name': b7
    })
    b4 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for index, row in b3.iterrows():
        folium.Marker([row['lon'], row['lat']], b5 = row['name']).add_to(b4)
    b4.save('unknown.html')
def fonk2(path_v2):
    b6 = []
    b7 = []
    b1 = []
    b2 = []
    for entry in path_v2:
        b6.append(entry[0])
        b7.append(entry[1])
        b1.append(entry[6])
        b2.append(entry[7])
    fonk1(b7, b1, b2)
    b8 = []
    for i in range(len(path_v2)):
        b9 = b6[i]
        b10 = (float(b1[i]), float(b2[i]))
        for j in range(len(b1)):
            b11 = b6[j]
            b12 = (float(b1[j]), float(b2[j]))
            if b9 = = b11:
                b8.append([int(b9), int(b11), 99999])
            else:
                b13 = great_circle(b10, b12).km
                b8.append([int(b9), int(b11), b13])
    return b8, len(b6)
if b14 = = "__main__":
    b8, b15 = fonk2(path_v2)
    print("Edges:", b8)
    print("Number of airports:", b15)
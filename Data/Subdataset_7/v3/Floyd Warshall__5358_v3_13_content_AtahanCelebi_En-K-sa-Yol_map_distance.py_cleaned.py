import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.b13 import great_circle
def fonk1(b7, b1, b2):
    b1 = [float(lat) for lat in b1]
    b2 = [float(long) for long in b2]
    b3 = pd.DataFrame({
        'lat': b1,
        'lon': b2,
        'name': b7
    })
    b4 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for _, row in b3.iterrows():
        folium.Marker([row['lon'], row['lat']], b5 = row['name']).add_to(b4)
    b4.save('unknown.html')
def fonk2(path_v2):
    with open(path_v2, "r") as file:
        b6 = file.readlines()
    b3 = [line.strip().split(",") for line in b6]
    for i, entry in enumerate(b3):
        entry[0] = str(i + 1)
    b1 = [entry[6] for entry in b3]
    b2 = [entry[7] for entry in b3]
    b7 = [entry[1] for entry in b3]
    b8 = [entry[0] for entry in b3]
    fonk1(b7, b1, b2)
    b9 = []
    for j, b11 in enumerate(b8):
        b10 = (float(b1[j]), float(b2[j]))
        for i, location2 in enumerate(b8):
            if b11 = = location2:
                continue
            b12 = (float(b1[i]), float(b2[i]))
            b13 = great_circle(b10, b12).km
            b9.append([int(b11), int(location2), b13])
    return b9, len(b3)
if b14 = = "__main__":
    b9, b15 = fonk2(path_v2)
    print("Edges:", b9)
    print("Number of airports:", b15)
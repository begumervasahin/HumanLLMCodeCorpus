import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.b16 import great_circle
def fonk1(names, b2, b3, b1 = 'map.html'):
    b2 = [float(lat) for lat in b2]
    b3 = [float(lon) for lon in b3]
    b4 = pd.DataFrame({
        'lat': b2,
        'lon': b3,
        'name': names
    })
    b5 = [20, 0]
    b6 = folium.Map(location=b5, tiles="Mapbox Bright", zoom_start=2)
    for _, row in b4.iterrows():
        folium.Marker(
            [row['lat'], row['lon']],
            b7 = row['name']
        ).add_to(b6)
    b6.save(b1)
    print(f"Map saved to {b1}")
def fonk2(b18):
    with open(b18, "r") as file:
        b8 = file.readlines()
    b4 = [line.strip().split(",") for line in b8]
    for i, entry in enumerate(b4):
        entry[0] = str(i + 1)
    b2 = [entry[6] for entry in b4]
    b3 = [entry[7] for entry in b4]
    b9 = [entry[1] for entry in b4]
    b10 = [entry[0] for entry in b4]
    return b9, b2, b3, b10, b4
def fonk3(b4):
    b11 = []
    for j in range(len(b4)):
        b12 = b4[j][0]
        b13 = (float(b4[j][6]), float(b4[j][7]))
        for i in range(len(b4)):
            b14 = b4[i][0]
            if b12 = = b14:
                continue
            b15 = (float(b4[i][6]), float(b4[i][7]))
            b16 = great_circle(b13, b15).km
            b11.append([int(b12), int(b14), b16])
    return b11
def fonk4(b18):
    b9, b2, b3, b10, b4 = fonk2(b18)
    fonk1(b9, b2, b3)
    b11 = fonk3(b4)
    return b11, len(b10)
if b17 = = "__main__":
    b18 = 'path_to_your_file.csv'
    b11, b19 = fonk4(b18)
    print("Edges:", b11)
    print("Number of airports:", b19)
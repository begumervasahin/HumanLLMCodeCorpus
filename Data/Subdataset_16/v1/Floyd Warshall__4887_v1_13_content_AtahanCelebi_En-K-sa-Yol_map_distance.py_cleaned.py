import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.b17 import great_circle
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
    for i in range(len(b4)):
        folium.Marker(
            [b4.iloc[i]['lat'], b4.iloc[i]['lon']],
            b7 = b4.iloc[i]['name']
        ).add_to(b6)
    b6.save(b1)
    print(f"Map saved to {b1}")
def fonk2(b19):
    with open(b19, "r") as file:
        b8 = file.readlines()
    b4 = [line.strip().split(",") for line in b8]
    for i in range(len(b4)):
        b4[i][0] = str(i + 1)
    b2 = [entry[6] for entry in b4]
    b3 = [entry[7] for entry in b4]
    b9 = [entry[1] for entry in b4]
    b10 = [entry[0] for entry in b4]
    return b9, b2, b3, b10, b4
def fonk3(b4):
    b11 = Nominatim(user_agent="Hacettepe_Geomatik")
    b12 = []
    for j in range(len(b4)):
        b13 = b4[j][0]
        b14 = (float(b4[j][6]), float(b4[j][7]))
        for i in range(len(b4)):
            b15 = b4[i][0]
            if b13 = = b15:
                continue
            b16 = (float(b4[i][6]), float(b4[i][7]))
            b17 = great_circle(b14, b16).km
            b12.append([int(b13), int(b15), b17])
    return b12
def fonk4(b19):
    b9, b2, b3, b10, b4 = fonk2(b19)
    fonk1(b9, b2, b3)
    b12 = fonk3(b4)
    return b12, len(b10)
if b18 = = "__main__":
    b19 = 'path_to_your_file.csv'
    b12, b20 = fonk4(b19)
    print("Edges:", b12)
    print("Number of airports:", b20)
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
    for i in range(len(b3)):
        folium.Marker([b3.iloc[i]['lon'], b3.iloc[i]['lat']], b5 = b3.iloc[i]['name']).add_to(b4)
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
    b9 = Nominatim(user_agent="Hacettepe_Geomatik")
    b10 = []
    for j, b12 in enumerate(b8):
        b11 = (float(b1[j]), float(b2[j]))
        for i, location2 in enumerate(b8):
            if b12 = = location2:
                continue
            b13 = (float(b1[i]), float(b2[i]))
            b10.append([int(b12), int(location2), great_circle(b11, b13).km])
    return b10, len(b3)
if b14 = = "__main__":
    b10, b15 = fonk2(path_v2)
    print("Edges:", b10)
    print("Number of airports:", b15)
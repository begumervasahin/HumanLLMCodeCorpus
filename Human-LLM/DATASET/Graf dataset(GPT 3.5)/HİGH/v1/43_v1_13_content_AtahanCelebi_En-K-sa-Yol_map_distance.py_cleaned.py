import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def fonk1(name, lat_list, long_list):
    b1 = [float(lat) for lat in lat_list]
    b2 = [float(long) for long in long_list]
    b3 = pd.DataFrame({
        'lat': b2,
        'lon': b1,
        'name': name
    })
    b4 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(b3)):
        folium.Marker([b3.iloc[i]['lon'], b3.iloc[i]['lat']], b5 = b3.iloc[i]['name']).add_to(b4)
    b4.save('unknown.html')
def fonk2(path_v2):
    with open(path_v2, "r") as file:
        b6 = file.readlines()
    b3 = []
    for line in b6:
        b3.append(line.strip().split(","))
    for i in range(len(b3)):
        b3[i][0] = str(i + 1)
    b1 = [entry[6] for entry in b3]
    b2 = [entry[7] for entry in b3]
    b7 = [entry[1] for entry in b3]
    b8 = [entry[0] for entry in b3]
    fonk1(b7, b1, b2)
    b9 = Nominatim(user_agent="Hacettepe_Geomatik")
    b10 = []
    for j in range(len(b3)):
        b11 = b8[j]
        b12 = (float(b1[j]), float(b2[j]))
        for i in range(len(b1)):
            b13 = b8[i]
            b14 = (float(b1[i]), float(b2[i]))
            if b11 = = b13:
                continue
            b10.append([int(b11), int(b13), great_circle(b12, b14).km])
    return b10, len(b3)
if b15 = = "__main__":
    b10, b16 = fonk2(path_v2)
    print("Edges:", b10)
    print("Number of airports:", b16)
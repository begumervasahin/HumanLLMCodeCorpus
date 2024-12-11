import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def fonk1(b7, b1, b2):
    b1 = [float(lat) for lat in b1]
    b2 = [float(long) for long in b2]
    b3 = pd.DataFrame({
        'lat': b2,
        'lon': b1,
        'name': b7
    })
    b4 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(b3)):
        folium.Marker([b3.iloc[i]['lon'], b3.iloc[i]['lat']], b5 = b3.iloc[i]['name']).add_to(b4)
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
    b8 = Nominatim(user_agent="Hacettepe_Geomatik")
    b9 = []
    for i in range(len(path_v2)):
        b10 = b6[i]
        b11 = (float(b1[i]), float(b2[i]))
        for j in range(len(b1)):
            b12 = b6[j]
            b13 = (float(b1[j]), float(b2[j]))
            if b10 = = b12:
                b9.append([int(b10), int(b12), 99999])
            else:
                b9.append([int(b10), int(b12), great_circle(b11, b13).km])
    return b9, len(b6)
if b14 = = "__main__":
    b9, b15 = fonk2(path_v2)
    print("Edges:", b9)
    print("Number of airports:", b15)
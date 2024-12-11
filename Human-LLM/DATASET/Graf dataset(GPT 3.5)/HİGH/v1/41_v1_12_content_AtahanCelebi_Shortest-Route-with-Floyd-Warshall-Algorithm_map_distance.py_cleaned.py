import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def fonk1(name, lat_list, long_list):
    b1 = [float(i) for i in lat_list]
    b2 = [float(i) for i in long_list]
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
    b3 = path_v2
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    for i in range(len(b3)):
        b6.append(b3[i][6])
        b7.append(b3[i][7])
        b8.append(b3[i][1])
        b9.append(b3[i][0])
    fonk1(b8, b6, b7)
    b10 = Nominatim(user_agent="Hacettepe_Geomatik")
    b11 = []
    for j in range(len(b3)):
        b12 = b9[j]
        b13 = [b3[j][6], b3[j][7]]
        b14 = (float(b3[j][6]), float(b3[j][7]))
        for i in range(len(b6)):
            b15 = b9[i]
            b16 = (float(b3[i][6]), float(b3[i][7]))
            if b12 = = b15:
                b11.append([int(b12), int(b15), 99999])
            b11.append([int(b12), int(b15), great_circle(b14, b16).km])
    return b11, len(b9)
if b17 = = "__main__":
    b11, b18 = fonk2(path_v2)
    print("Edges:", b11)
    print("Number of airports:", b18)
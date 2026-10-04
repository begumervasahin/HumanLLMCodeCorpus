import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.b17 import great_circle
def fonk1(name, lat_list, long_list, b1 = 'map.html'):
    b2 = [float(i) for i in lat_list]
    b3 = [float(i) for i in long_list]
    b4 = pd.DataFrame({
        'lat': b3,
        'lon': b2,
        'name': name
    })
    b5 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(b4)):
        folium.Marker(
            [b4.iloc[i]['lon'], b4.iloc[i]['lat']],
            b6 = b4.iloc[i]['name']
        ).add_to(b5)
    b5.save(b1)
    print(f"Map saved to {b1}")
def fonk2(b4):
    b7 = [entry[6] for entry in b4]
    b8 = [entry[7] for entry in b4]
    b9 = [entry[1] for entry in b4]
    b10 = [entry[0] for entry in b4]
    fonk1(b9, b7, b8)
    b11 = Nominatim(user_agent="Hacettepe_Geomatik")
    b12 = []
    for j in range(len(b4)):
        b13 = b10[j]
        b14 = (float(b4[j][6]), float(b4[j][7]))
        for i in range(len(b7)):
            b15 = b10[i]
            b16 = (float(b4[i][6]), float(b4[i][7]))
            if b13 = = b15:
                b12.append([int(b13), int(b15), 99999])
            else:
                b17 = great_circle(b14, b16).km
                b12.append([int(b13), int(b15), b17])
    return b12, len(b10)
if b18 = = "__main__":
    b4 = [
        [1, 'Airport A', 'Country A', 'City A', 'IATA A', 'ICAO A', 40.712776, -74.005974],
        [2, 'Airport B', 'Country B', 'City B', 'IATA B', 'ICAO B', 34.052235, -118.243683],
    ]
    b12, b19 = fonk2(b4)
    print("Edges:", b12)
    print("Number of airports:", b19)
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.b14 import great_circle
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
def fonk2(b4):
    b8 = Nominatim(user_agent="Hacettepe_Geomatik")
    b9 = []
    for j in range(len(b4)):
        b10 = b4[j][0]
        b11 = (float(b4[j][6]), float(b4[j][7]))
        for i in range(len(b4)):
            b12 = b4[i][0]
            b13 = (float(b4[i][6]), float(b4[i][7]))
            if b10 = = b12:
                b9.append([int(b10), int(b12), 99999])
            else:
                b14 = great_circle(b11, b13).km
                b9.append([int(b10), int(b12), b14])
    return b9
def fonk3(b4):
    b2 = [entry[6] for entry in b4]
    b3 = [entry[7] for entry in b4]
    b15 = [entry[1] for entry in b4]
    fonk1(b15, b2, b3)
    b9 = fonk2(b4)
    return b9, len(b4)
if b16 = = "__main__":
    b17 = [
        [1, 'Airport A', 'Country A', 'City A', 'IATA A', 'ICAO A', 40.712776, -74.005974],
        [2, 'Airport B', 'Country B', 'City B', 'IATA B', 'ICAO B', 34.052235, -118.243683],
    ]
    b9, b18 = fonk3(b17)
    print("Edges:", b9)
    print("Number of airports:", b18)
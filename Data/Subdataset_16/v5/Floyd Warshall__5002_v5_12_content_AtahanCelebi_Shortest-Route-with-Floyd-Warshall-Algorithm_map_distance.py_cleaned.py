import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.b13 import great_circle
def fonk1(names, b2, b3, b1 = 'map.html'):
    b2 = [float(lat) for lat in b2]
    b3 = [float(lon) for lon in b3]
    b4 = pd.DataFrame({
        'latitude': b2,
        'longitude': b3,
        'name': names
    })
    b5 = [20, 0]
    b6 = folium.Map(location=b5, tiles="Mapbox Bright", zoom_start=2)
    for _, row in b4.iterrows():
        folium.Marker(
            [row['latitude'], row['longitude']],
            b7 = row['name']
        ).add_to(b6)
    b6.save(b1)
    print(f"Map saved to {b1}")
def fonk2(b4):
    b8 = []
    for j, source in enumerate(b4):
        b9 = source[0]
        b10 = (float(source[6]), float(source[7]))
        for i, destination in enumerate(b4):
            b11 = destination[0]
            b12 = (float(destination[6]), float(destination[7]))
            if b9 = = b11:
                b8.append([int(b9), int(b11), 99999])
            else:
                b13 = great_circle(b10, b12).km
                b8.append([int(b9), int(b11), b13])
    return b8
def fonk3(b4):
    b2 = [entry[6] for entry in b4]
    b3 = [entry[7] for entry in b4]
    b14 = [entry[1] for entry in b4]
    fonk1(b14, b2, b3)
    b8 = fonk2(b4)
    return b8, len(b4)
if b15 = = "__main__":
    b16 = [
        [1, 'Airport A', 'Country A', 'City A', 'IATA A', 'ICAO A', 40.712776, -74.005974],
        [2, 'Airport B', 'Country B', 'City B', 'IATA B', 'ICAO B', 34.052235, -118.243683],
    ]
    b8, b17 = fonk3(b16)
    print("Edges:", b8)
    print("Number of airports:", b17)
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def fonk1(airport_names, latitudes, longitudes):
    b1 = pd.DataFrame({
        'lat': [float(lat) for lat in latitudes],
        'lon': [float(long) for long in longitudes],
        'name': airport_names
    })
    b2 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for index, row in b1.iterrows():
        folium.Marker([row['lon'], row['lat']], b3 = row['name']).add_to(b2)
    b2.save('unknown.html')
def fonk2(path_v2):
    b4 = [(entry[0], entry[1], float(entry[6]), float(entry[7])) for entry in path_v2]
    fonk1([entry[1] for entry in path_v2], [entry[6] for entry in path_v2], [entry[7] for entry in path_v2])
    b5 = []
    for i, (b8, name_chosen, lat_chosen, lon_chosen) in enumerate(b4):
        b6 = (lat_chosen, lon_chosen)
        for j, (location2, name2, lat2, lon2) in enumerate(b4):
            b7 = (lat2, lon2)
            if b8 = = location2:
                b5.append([int(b8), int(location2), 99999])
            else:
                b9 = great_circle(b6, b7).km
                b5.append([int(b8), int(location2), b9])
    return b5, len(b4)
if b10 = = "__main__":
    b5, b11 = fonk2(path_v2)
    print("Edges:", b5)
    print("Number of airports:", b11)
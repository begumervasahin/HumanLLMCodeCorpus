import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_airport_map(airport_names, latitudes, longitudes):
    latitudes = [float(lat) for lat in latitudes]
    longitudes = [float(long) for long in longitudes]
    data = pd.DataFrame({
        'lat': latitudes,
        'lon': longitudes,
        'name': airport_names
    })
    map_obj = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for index, row in data.iterrows():
        folium.Marker([row['lon'], row['lat']], popup=row['name']).add_to(map_obj)
    map_obj.save('unknown.html')
def calculate_distances(path_v2):
    airport_data = []
    airport_names = []
    latitudes = []
    longitudes = []
    for entry in path_v2:
        airport_data.append(entry[0])
        airport_names.append(entry[1])
        latitudes.append(entry[6])
        longitudes.append(entry[7])
    create_airport_map(airport_names, latitudes, longitudes)
    edges = []
    for i in range(len(path_v2)):
        loc_chosen = airport_data[i]
        airport_chosen = (float(latitudes[i]), float(longitudes[i]))
        for j in range(len(latitudes)):
            location2 = airport_data[j]
            airport2 = (float(latitudes[j]), float(longitudes[j]))
            if loc_chosen == location2:
                edges.append([int(loc_chosen), int(location2), 99999])
            else:
                distance_km = great_circle(airport_chosen, airport2).km
                edges.append([int(loc_chosen), int(location2), distance_km])
    return edges, len(airport_data)
if __name__ == "__main__":
    edges, num_airports = calculate_distances(path_v2)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
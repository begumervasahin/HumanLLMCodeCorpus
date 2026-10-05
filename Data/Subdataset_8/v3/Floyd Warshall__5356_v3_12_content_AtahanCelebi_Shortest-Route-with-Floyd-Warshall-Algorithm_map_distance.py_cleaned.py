import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_map(airport_names, latitudes, longitudes):
    data = pd.DataFrame({
        'lat': [float(lat) for lat in latitudes],
        'lon': [float(long) for long in longitudes],
        'name': airport_names
    })
    map_obj = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for index, row in data.iterrows():
        folium.Marker([row['lon'], row['lat']], popup=row['name']).add_to(map_obj)
    map_obj.save('unknown.html')
def compute_edges(path_v2):
    airport_data = [(entry[0], entry[1], float(entry[6]), float(entry[7])) for entry in path_v2]
    create_map([entry[1] for entry in path_v2], [entry[6] for entry in path_v2], [entry[7] for entry in path_v2])
    edges = []
    for i, (loc_chosen, name_chosen, lat_chosen, lon_chosen) in enumerate(airport_data):
        airport_chosen = (lat_chosen, lon_chosen)
        for j, (location2, name2, lat2, lon2) in enumerate(airport_data):
            airport2 = (lat2, lon2)
            if loc_chosen == location2:
                edges.append([int(loc_chosen), int(location2), 99999])
            else:
                distance_km = great_circle(airport_chosen, airport2).km
                edges.append([int(loc_chosen), int(location2), distance_km])
    return edges, len(airport_data)
if __name__ == "__main__":
    edges, num_airports = compute_edges(path_v2)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
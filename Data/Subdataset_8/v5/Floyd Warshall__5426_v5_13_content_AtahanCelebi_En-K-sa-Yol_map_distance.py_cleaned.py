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
    for _, airport in data.iterrows():
        folium.Marker([airport['lon'], airport['lat']], popup=airport['name']).add_to(map_obj)
    map_obj.save('unknown.html')
def main(path_v2):
    with open(path_v2, "r") as file:
        lines = file.readlines()
    data = [line.strip().split(",") for line in lines]
    for i, entry in enumerate(data):
        entry[0] = str(i + 1)
    airport_data = [entry[0] for entry in data]
    latitudes = [entry[6] for entry in data]
    longitudes = [entry[7] for entry in data]
    airport_names = [entry[1] for entry in data]
    create_airport_map(airport_names, latitudes, longitudes)
    edges = []
    for j, loc_chosen in enumerate(airport_data):
        airport_chosen = (float(latitudes[j]), float(longitudes[j]))
        for i, location2 in enumerate(airport_data):
            if loc_chosen == location2:
                continue
            airport2 = (float(latitudes[i]), float(longitudes[i]))
            distance = great_circle(airport_chosen, airport2).km
            edges.append([int(loc_chosen), int(location2), distance])
    return edges, len(data)
if __name__ == "__main__":
    edges, num_airports = main(path_v2)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
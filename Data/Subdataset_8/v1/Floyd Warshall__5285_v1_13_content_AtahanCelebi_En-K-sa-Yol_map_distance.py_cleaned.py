import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_map(name, lat_list, long_list):
    latitudes = [float(lat) for lat in lat_list]
    longitudes = [float(long) for long in long_list]
    data = pd.DataFrame({
        'lat': longitudes,
        'lon': latitudes,
        'name': name
    })
    map_obj = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(data)):
        folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(map_obj)
    map_obj.save('unknown.html')
def main(path_v2):
    with open(path_v2, "r") as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append(line.strip().split(","))
    for i in range(len(data)):
        data[i][0] = str(i + 1)
    latitudes = [entry[6] for entry in data]
    longitudes = [entry[7] for entry in data]
    airport_names = [entry[1] for entry in data]
    airport_data = [entry[0] for entry in data]
    create_map(airport_names, latitudes, longitudes)
    geolocator = Nominatim(user_agent="Hacettepe_Geomatik")
    edges = []
    for j in range(len(data)):
        loc_chosen = airport_data[j]
        airport_chosen = (float(latitudes[j]), float(longitudes[j]))
        for i in range(len(latitudes)):
            location2 = airport_data[i]
            airport2 = (float(latitudes[i]), float(longitudes[i]))
            if loc_chosen == location2:
                continue
            edges.append([int(loc_chosen), int(location2), great_circle(airport_chosen, airport2).km])
    return edges, len(data)
if __name__ == "__main__":
    edges, num_airports = main(path_v2)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_map(airport_names, latitudes, longitudes):
    latitudes = [float(lat) for lat in latitudes]
    longitudes = [float(long) for long in longitudes]
    data = pd.DataFrame({
        'lat': latitudes,
        'lon': longitudes,
        'name': airport_names
    })
    map_obj = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(data)):
        folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(map_obj)
    map_obj.save('unknown.html')
def main(path_v2):
    airport_data = []
    airport_names = []
    latitudes = []
    longitudes = []
    for entry in path_v2:
        airport_data.append(entry[0])
        airport_names.append(entry[1])
        latitudes.append(entry[6])
        longitudes.append(entry[7])
    create_map(airport_names, latitudes, longitudes)
    geolocator = Nominatim(user_agent="Hacettepe_Geomatik")
    edges = []
    for j in range(len(path_v2)):
        loc_chosen = airport_data[j]
        airport_chosen = (float(latitudes[j]), float(longitudes[j]))
        for i in range(len(latitudes)):
            location2 = airport_data[i]
            airport2 = (float(latitudes[i]), float(longitudes[i]))
            if loc_chosen == location2:
                edges.append([int(loc_chosen), int(location2), 99999])
            edges.append([int(loc_chosen), int(location2), great_circle(airport_chosen, airport2).km])
    return edges, len(airport_data)
if __name__ == "__main__":
    edges, num_airports = main(path_v2)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
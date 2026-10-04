import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_map(names, lat_list, long_list, output_file='map.html'):
    latitudes = [float(lat) for lat in lat_list]
    longitudes = [float(lon) for lon in long_list]
    data = pd.DataFrame({
        'latitude': latitudes,
        'longitude': longitudes,
        'name': names
    })
    map_center = [20, 0]
    folium_map = folium.Map(location=map_center, tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(data)):
        folium.Marker(
            [data.iloc[i]['latitude'], data.iloc[i]['longitude']],
            popup=data.iloc[i]['name']
        ).add_to(folium_map)
    folium_map.save(output_file)
    print(f"Map saved to {output_file}")
def calculate_edges(data):
    geolocator = Nominatim(user_agent="Hacettepe_Geomatik")
    edges = []
    for j in range(len(data)):
        loc_chosen = data[j][0]
        coord_chosen = (float(data[j][6]), float(data[j][7]))
        for i in range(len(data)):
            loc_other = data[i][0]
            coord_other = (float(data[i][6]), float(data[i][7]))
            if loc_chosen == loc_other:
                edges.append([int(loc_chosen), int(loc_other), 99999])
            else:
                distance = great_circle(coord_chosen, coord_other).km
                edges.append([int(loc_chosen), int(loc_other), distance])
    return edges
def main(data):
    latitudes = [entry[6] for entry in data]
    longitudes = [entry[7] for entry in data]
    airport_names = [entry[1] for entry in data]
    create_map(airport_names, latitudes, longitudes)
    edges = calculate_edges(data)
    return edges, len(data)
if __name__ == "__main__":
    example_data = [
        [1, 'Airport A', 'Country A', 'City A', 'IATA A', 'ICAO A', 40.712776, -74.005974],
        [2, 'Airport B', 'Country B', 'City B', 'IATA B', 'ICAO B', 34.052235, -118.243683],
    ]
    edges, num_airports = main(example_data)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
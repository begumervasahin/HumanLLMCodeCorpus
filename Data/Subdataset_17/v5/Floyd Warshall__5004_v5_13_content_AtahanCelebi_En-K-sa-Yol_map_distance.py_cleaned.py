import folium
import pandas as pd
from geopy.distance import great_circle
def create_map(names, latitudes, longitudes, output_file='map.html'):
    latitudes = [float(lat) for lat in latitudes]
    longitudes = [float(lon) for lon in longitudes]
    data = pd.DataFrame({
        'lat': latitudes,
        'lon': longitudes,
        'name': names
    })
    map_center = [20, 0]
    folium_map = folium.Map(location=map_center, tiles="Mapbox Bright", zoom_start=2)
    for _, row in data.iterrows():
        folium.Marker(
            [row['lat'], row['lon']],
            popup=row['name']
        ).add_to(folium_map)
    folium_map.save(output_file)
    print(f"Map saved to {output_file}")
def process_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    data = [line.strip().split(",") for line in lines]
    for i, entry in enumerate(data):
        entry[0] = str(i + 1)
    latitudes = [entry[6] for entry in data]
    longitudes = [entry[7] for entry in data]
    airport_names = [entry[1] for entry in data]
    airport_ids = [entry[0] for entry in data]
    return airport_names, latitudes, longitudes, airport_ids, data
def calculate_edges(data):
    edges = []
    for j, source in enumerate(data):
        loc_chosen = source[0]
        airport_chosen = (float(source[6]), float(source[7]))
        for i, target in enumerate(data):
            loc_other = target[0]
            if loc_chosen == loc_other:
                continue
            airport_other = (float(target[6]), float(target[7]))
            distance = great_circle(airport_chosen, airport_other).km
            edges.append([int(loc_chosen), int(loc_other), distance])
    return edges
def main(file_path):
    airport_names, latitudes, longitudes, airport_ids, data = process_data(file_path)
    create_map(airport_names, latitudes, longitudes)
    edges = calculate_edges(data)
    return edges, len(airport_ids)
if __name__ == "__main__":
    file_path = 'path_to_your_file.csv'
    edges, num_airports = main(file_path)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
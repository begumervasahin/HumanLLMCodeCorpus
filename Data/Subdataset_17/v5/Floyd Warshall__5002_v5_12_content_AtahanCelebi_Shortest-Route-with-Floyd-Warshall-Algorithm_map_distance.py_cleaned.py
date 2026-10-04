import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_map(names, latitudes, longitudes, output_file='map.html'):
    latitudes = [float(lat) for lat in latitudes]
    longitudes = [float(lon) for lon in longitudes]
    data = pd.DataFrame({
        'latitude': latitudes,
        'longitude': longitudes,
        'name': names
    })
    map_center = [20, 0]
    folium_map = folium.Map(location=map_center, tiles="Mapbox Bright", zoom_start=2)
    for _, row in data.iterrows():
        folium.Marker(
            [row['latitude'], row['longitude']],
            popup=row['name']
        ).add_to(folium_map)
    folium_map.save(output_file)
    print(f"Map saved to {output_file}")
def calculate_edges(data):
    edges = []
    for j, source in enumerate(data):
        source_id = source[0]
        source_coords = (float(source[6]), float(source[7]))
        for i, destination in enumerate(data):
            destination_id = destination[0]
            destination_coords = (float(destination[6]), float(destination[7]))
            if source_id == destination_id:
                edges.append([int(source_id), int(destination_id), 99999])
            else:
                distance = great_circle(source_coords, destination_coords).km
                edges.append([int(source_id), int(destination_id), distance])
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
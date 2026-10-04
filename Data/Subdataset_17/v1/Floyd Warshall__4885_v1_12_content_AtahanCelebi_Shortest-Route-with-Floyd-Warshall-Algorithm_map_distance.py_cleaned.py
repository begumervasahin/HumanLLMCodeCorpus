import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
def create_map(name, lat_list, long_list, output_file='map.html'):
    int_lat = [float(i) for i in lat_list]
    int_long = [float(i) for i in long_list]
    data = pd.DataFrame({
        'lat': int_long,
        'lon': int_lat,
        'name': name
    })
    m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    for i in range(len(data)):
        folium.Marker(
            [data.iloc[i]['lon'], data.iloc[i]['lat']],
            popup=data.iloc[i]['name']
        ).add_to(m)
    m.save(output_file)
    print(f"Map saved to {output_file}")
def main(data):
    lati = [entry[6] for entry in data]
    longi = [entry[7] for entry in data]
    airport_name = [entry[1] for entry in data]
    airport_data = [entry[0] for entry in data]
    create_map(airport_name, lati, longi)
    geolocator = Nominatim(user_agent="Hacettepe_Geomatik")
    edges = []
    for j in range(len(data)):
        loc_choosen = airport_data[j]
        airport_choosen = (float(data[j][6]), float(data[j][7]))
        for i in range(len(lati)):
            location2 = airport_data[i]
            airport2 = (float(data[i][6]), float(data[i][7]))
            if loc_choosen == location2:
                edges.append([int(loc_choosen), int(location2), 99999])
            else:
                distance = great_circle(airport_choosen, airport2).km
                edges.append([int(loc_choosen), int(location2), distance])
    return edges, len(airport_data)
if __name__ == "__main__":
    data = [
        [1, 'Airport A', 'Country A', 'City A', 'IATA A', 'ICAO A', 40.712776, -74.005974],
        [2, 'Airport B', 'Country B', 'City B', 'IATA B', 'ICAO B', 34.052235, -118.243683],
    ]
    edges, num_airports = main(data)
    print("Edges:", edges)
    print("Number of airports:", num_airports)
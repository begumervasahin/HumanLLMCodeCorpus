import googlemaps
import numpy as np
from beautifultable import BeautifulTable
from datetime import datetime
gmaps = googlemaps.Client(key='YOUR_API_KEY_HERE')
def geocode_to_coordinates(geocode):
    coord_dict = geocode[0]['geometry']['location']
    return coord_dict['lat'], coord_dict['lng']
def get_nearby_metro_stations(location):
    geocode = gmaps.geocode(location)
    coordinates = geocode_to_coordinates(geocode)
    stations = gmaps.places_nearby(location=coordinates, rank_by='distance', type='subway_station')['results']
    return stations[:4]
def get_place_ids(geocodes):
    return ['place_id:' + geocode['place_id'] for geocode in geocodes]
def get_travel_time(origin, destination):
    origin_stations = get_nearby_metro_stations(origin)
    destination_stations = get_nearby_metro_stations(destination)
    origin_id = 'place_id:' + gmaps.geocode(origin)[0]['place_id']
    destination_id = 'place_id:' + gmaps.geocode(destination)[0]['place_id']
    origin_place_ids = get_place_ids(origin_stations)
    destination_place_ids = get_place_ids(destination_stations)
    o_to_metro = gmaps.distance_matrix(origin_id, origin_place_ids)
    metro_to_d = gmaps.distance_matrix(destination_place_ids, destination_id)
    distance_matrix = gmaps.distance_matrix(origin_place_ids, destination_place_ids, mode='transit', transit_mode='subway')
    return o_to_metro, distance_matrix, metro_to_d
def calculate_optimal_path(travel_data):
    o_to_metro, distance_matrix, metro_to_d = travel_data
    a = [element['duration']['value'] for element in o_to_metro['rows'][0]['elements']]
    b = [element['duration']['value'] for row in distance_matrix['rows'] for element in row['elements']]
    c = [element['duration']['value'] for element in metro_to_d['rows'][0]['elements']]
    a = np.tile(a, 2)
    c = np.tile(c, 2)
    total_durations = np.add(np.add(a, b), c)
    min_duration = np.min(total_durations)
    min_index = np.argmin(total_durations)
    origin_address = o_to_metro['origin_addresses'][0]
    metro1_address = o_to_metro['destination_addresses'][min_index
    metro2_address = distance_matrix['destination_addresses'][min_index % 4]
    destination_address = metro_to_d['destination_addresses'][0]
    path = (origin_address, 'to', metro1_address, 'to', metro2_address, 'to', destination_address)
    duration = ("It will take", int(min_duration / 60), 'minutes')
    return path, duration
def main():
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    travel_data = get_travel_time(origin, destination)
    path, duration = calculate_optimal_path(travel_data)
    print("Optimal path and travel time:")
    print(" -> ".join(path))
    print(f"{duration[0]} {duration[1]} {duration[2]}")
if __name__ == "__main__":
    main()
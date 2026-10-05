import googlemaps
from beautifultable import BeautifulTable
import numpy as np
gmaps = googlemaps.Client(key='YOUR_API_KEY')
def geocode_to_coordinates(geocode):
    location = geocode[0]['geometry']['location']
    return location['lat'], location['lng']
def get_nearby_metro_stations(location):
    geocode = gmaps.geocode(location)
    coordinates = geocode_to_coordinates(geocode)
    stations = gmaps.places_nearby(
        keyword='metro',
        location=coordinates,
        rank_by='distance',
        type='subway_station'
    )['results']
    return stations[:4]
def get_travel_time(origin, destination):
    origin_stations = get_nearby_metro_stations(origin)
    destination_stations = get_nearby_metro_stations(destination)
    origin_id = 'place_id:' + gmaps.geocode(origin)[0]['place_id']
    destination_id = 'place_id:' + gmaps.geocode(destination)[0]['place_id']
    o_to_metro = gmaps.distance_matrix(origin_id, get_place_ids(origin_stations))
    metro_to_d = gmaps.distance_matrix(get_place_ids(destination_stations), destination_id)
    distance_matrix = gmaps.distance_matrix(
        get_place_ids(origin_stations),
        get_place_ids(destination_stations),
        mode='transit',
        transit_mode='subway'
    )
    return o_to_metro, distance_matrix, metro_to_d
def get_place_ids(geocodes):
    return ['place_id:' + geocode['place_id'] for geocode in geocodes]
def find_optimal_route(value):
    a = [value[0]['rows'][0]['elements'][i]['duration']['value'] for i in range(4)]
    b = [value[1]['rows'][i]['elements'][j]['duration']['value'] for i in range(4) for j in range(4)]
    c = [value[2]['rows'][i]['elements'][0]['duration']['value'] for i in range(4)]
    a = np.tile(a, 2)
    c = np.tile(c, 2)
    d = np.add(a, b) + c
    min_index = np.argmin(d)
    origin = value[0]['origin_addresses'][0]
    metro_station = value[0]['destination_addresses'][min_index
    destination = value[1]['destination_addresses'][min_index
    final_destination = value[2]['destination_addresses'][0]
    return (
        origin, ' to ', metro_station, ' to ', destination, ' to ', final_destination
    ), (
        "It will take", int(d[min_index] / 60), 'minutes'
    )
def main():
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    value = get_travel_time(origin, destination)
    output = find_optimal_route(value)
    print(output)
if __name__ == "__main__":
    main()
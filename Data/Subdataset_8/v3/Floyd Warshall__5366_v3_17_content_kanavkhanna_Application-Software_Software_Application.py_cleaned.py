import googlemaps
import numpy as np
gmaps = googlemaps.Client(key='YOUR_API_KEY')
def geocode_to_coordinates(geocode_result):
    location = geocode_result[0]['geometry']['location']
    return location['lat'], location['lng']
def get_nearby_metro_stations(location):
    geocode_result = gmaps.geocode(location)
    coordinates = geocode_to_coordinates(geocode_result)
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
    origin_place_id = 'place_id:' + gmaps.geocode(origin)[0]['place_id']
    destination_place_id = 'place_id:' + gmaps.geocode(destination)[0]['place_id']
    o_to_metro = gmaps.distance_matrix(origin_place_id, get_place_ids(origin_stations))
    metro_to_d = gmaps.distance_matrix(get_place_ids(destination_stations), destination_place_id)
    distance_matrix = gmaps.distance_matrix(
        get_place_ids(origin_stations),
        get_place_ids(destination_stations),
        mode='transit',
        transit_mode='subway'
    )
    return o_to_metro, distance_matrix, metro_to_d
def get_place_ids(geocode_results):
    return ['place_id:' + result['place_id'] for result in geocode_results]
def find_optimal_route(travel_times):
    o_to_metro_times, metro_to_d_times, d_to_destination_times = travel_times
    o_to_metro_durations = [result['duration']['value'] for result in o_to_metro_times['rows'][0]['elements']]
    metro_to_d_durations = [result['duration']['value'] for row in metro_to_d_times['rows'] for result in row['elements']]
    d_to_destination_durations = [result['duration']['value'] for result in d_to_destination_times['rows'][0]['elements']]
    o_to_metro_durations = np.tile(o_to_metro_durations, 2)
    d_to_destination_durations = np.tile(d_to_destination_durations, 2)
    total_durations = np.add(np.add(o_to_metro_durations, metro_to_d_durations), d_to_destination_durations)
    min_index = np.argmin(total_durations)
    origin_address = travel_times[0]['origin_addresses'][0]
    metro_station = travel_times[0]['destination_addresses'][min_index
    destination_address = travel_times[1]['destination_addresses'][min_index
    final_destination_address = travel_times[2]['destination_addresses'][0]
    return (
        origin_address, ' to ', metro_station, ' to ', destination_address, ' to ', final_destination_address
    ), (
        "It will take", int(total_durations[min_index] / 60), 'minutes'
    )
def main():
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    travel_times = get_travel_time(origin, destination)
    output = find_optimal_route(travel_times)
    print(output)
if __name__ == "__main__":
    main()
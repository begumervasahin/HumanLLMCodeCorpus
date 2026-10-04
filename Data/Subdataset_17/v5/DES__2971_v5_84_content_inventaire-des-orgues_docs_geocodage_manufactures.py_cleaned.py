import json
import requests
import geojson
GEOCODING_URL = "https:
def geocode_address(address):
    address_query = address.replace(" ", "+")
    response = requests.get(GEOCODING_URL + address_query)
    feature_collection = geojson.loads(response.text)
    point = feature_collection['features'][0]['geometry']['coordinates']
    return point[1], point[0]
def update_addresses_with_geolocation(data):
    for entry in data:
        address = entry['adresse']
        latitude, longitude = geocode_address(address)
        entry['latitude'] = latitude
        entry['longitude'] = longitude
    return data
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
def save_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def main():
    input_file = 'datas.json'
    output_file = 'facteurs_localisation.json'
    data = load_data(input_file)
    updated_data = update_addresses_with_geolocation(data)
    save_data(updated_data, output_file)
if __name__ == "__main__":
    main()
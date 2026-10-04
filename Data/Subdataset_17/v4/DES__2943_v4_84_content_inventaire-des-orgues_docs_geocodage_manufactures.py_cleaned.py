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
def main():
    with open('datas.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    updated_data = update_addresses_with_geolocation(data)
    with open('facteurs_localisation.json', 'w', encoding='utf-8') as output_file:
        json.dump(updated_data, output_file, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    main()
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
def update_addresses_with_geolocation(data_dict):
    for facteur in data_dict:
        address = facteur['adresse']
        latitude, longitude = geocode_address(address)
        facteur['latitude'] = latitude
        facteur['longitude'] = longitude
    return data_dict
def main():
    with open('datas.json') as json_file:
        data_dict = json.load(json_file)
    updated_data_dict = update_addresses_with_geolocation(data_dict)
    with open('facteurs_localisation.json', 'w') as output_file:
        json.dump(updated_data_dict, output_file, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    main()
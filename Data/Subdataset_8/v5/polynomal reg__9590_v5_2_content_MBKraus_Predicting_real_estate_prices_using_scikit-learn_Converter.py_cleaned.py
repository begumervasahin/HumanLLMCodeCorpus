import pandas as pd
from geopy import geocoders
from geopy.exc import GeocoderTimedOut
def load_data(*files):
    return pd.concat((pd.read_csv(file, sep=';') for file in files), ignore_index=True)
data = load_data('AmsterdamPage1to50.csv', 'AmsterdamPage51to100.csv', 'AmsterdamPage101to155.csv')
data['rooms_new'] = data['rooms'].str[-2:]
data['zipcode_new'] = data['zipcode'].str[:4]
data['price_new'] = data['price'].str.replace(' von', '')
google_geocoder = geocoders.GoogleV3(api_key='your API-key')
lat_coordinates = {}
lon_coordinates = {}
for zip_code in data['zipcode_new'].unique():
    try:
        location_query = f"{zip_code} Amsterdam"
        location = google_geocoder.geocode(location_query, timeout=60)
        lat = location.latitude
        lon = location.longitude
        lat_coordinates[zip_code] = lat
        lon_coordinates[zip_code] = lon
        print(location_query)
    except GeocoderTimedOut as e:
        print(f"Error: geocode failed on input {location_query} with message {e}")
data["latitude"] = data["zipcode_new"].map(lat_coordinates)
data["longitude"] = data["zipcode_new"].map(lon_coordinates)
data.to_csv("Overview_new.csv", sep=";", encoding='utf-8')
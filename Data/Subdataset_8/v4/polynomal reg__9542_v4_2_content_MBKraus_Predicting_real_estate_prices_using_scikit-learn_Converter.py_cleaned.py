import pandas as pd
from geopy import geocoders
from geopy.exc import GeocoderTimedOut
page1to50 = pd.read_csv('AmsterdamPage1to50.csv', sep=';')
page51to100 = pd.read_csv('AmsterdamPage51to100.csv', sep=';')
page101to155 = pd.read_csv('AmsterdamPage101to155.csv', sep=';')
data = pd.concat([page1to50, page51to100, page101to155], ignore_index=True)
data['rooms_new'] = data['rooms'].str[-2:]
data['zipcode_new'] = data['zipcode'].str[:4]
data['price_new'] = data['price'].str.replace(' von', '')
google_geocoder = geocoders.GoogleV3(api_key='your API-key')
lat_coordinates = {}
lon_coordinates = {}
for zip_code in data['zipcode_new'].unique():
    try:
        location_query = zip_code + " Amsterdam"
        location = google_geocoder.geocode(location_query, timeout=60)
        lat = location.latitude
        lon = location.longitude
        lat_coordinates[zip_code] = lat
        lon_coordinates[zip_code] = lon
        print(location_query)
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s with message %s" % (location_query, e.message))
data["latitude"] = data["zipcode_new"].map(lambda x: lat_coordinates[x])
data["longitude"] = data["zipcode_new"].map(lambda x: lon_coordinates[x])
data.to_csv("Overview_new.csv", sep=";", encoding='utf-8')
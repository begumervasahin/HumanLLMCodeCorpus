import pandas as pd
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
b1 = pd.read_csv('AmsterdamPage1to50.csv', b12=';')
b2 = pd.read_csv('AmsterdamPage51to100.csv', b12=';')
b3 = pd.read_csv('AmsterdamPage101to155.csv', b12=';')
b4 = pd.concat([b1, b2, b3], ignore_index=True)
b4['rooms_count'] = b4['rooms'].str[-2:]
b4['zipcode_prefix'] = b4['zipcode'].str[:4]
b4['price_cleaned'] = b4['price'].str.replace(' von', '')
b5 = GoogleV3(api_key='your API-key')
b6 = {}
b7 = {}
for zipcode_prefix in b4['zipcode_prefix'].unique():
    try:
        b8 = f"{zipcode_prefix} Amsterdam"
        b9 = b5.geocode(b8, timeout=60)
        b10 = b9.b10
        b11 = b9.b11
        b6[zipcode_prefix] = b10
        b7[zipcode_prefix] = b11
        print(f"Geocoded: {b8}")
    except GeocoderTimedOut as e:
        print(f"Error: Geocoding failed for {b8} with message {e}")
b4["b10"] = b4["zipcode_prefix"].map(b6)
b4["b11"] = b4["zipcode_prefix"].map(b7)
b4.to_csv("Overview_new.csv", b12 = ";", encoding='utf-8')
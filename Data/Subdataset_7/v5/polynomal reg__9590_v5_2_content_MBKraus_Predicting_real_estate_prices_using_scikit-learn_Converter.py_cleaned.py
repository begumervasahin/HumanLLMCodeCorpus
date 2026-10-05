import pandas as pd
from geopy import geocoders
from geopy.exc import GeocoderTimedOut
def fonk1(*files):
    return pd.concat((pd.read_csv(file, b1 = ';') for file in files), ignore_index=True)
b2 = fonk1('AmsterdamPage1to50.csv', 'AmsterdamPage51to100.csv', 'AmsterdamPage101to155.csv')
b2['rooms_new'] = b2['rooms'].str[-2:]
b2['zipcode_new'] = b2['zipcode'].str[:4]
b2['price_new'] = b2['price'].str.replace(' von', '')
b3 = geocoders.GoogleV3(api_key='your API-key')
b4 = {}
b5 = {}
for zip_code in b2['zipcode_new'].unique():
    try:
        b6 = f"{zip_code} Amsterdam"
        b7 = b3.geocode(b6, timeout=60)
        b8 = b7.latitude
        b9 = b7.longitude
        b4[zip_code] = b8
        b5[zip_code] = b9
        print(b6)
    except GeocoderTimedOut as e:
        print(f"Error: geocode failed on input {b6} with message {e}")
b2["latitude"] = b2["zipcode_new"].map(b4)
b2["longitude"] = b2["zipcode_new"].map(b5)
b2.to_csv("Overview_new.csv", b1 = ";", encoding='utf-8')
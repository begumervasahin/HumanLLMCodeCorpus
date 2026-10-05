import pandas as pd
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
b1 = pd.read_csv('AmsterdamPage1to50.csv', b12=';')
b2 = pd.read_csv('AmsterdamPage51to100.csv', b12=';')
b3 = pd.read_csv('AmsterdamPage101to155.csv', b12=';')
b4 = pd.concat([b1, b2, b3], ignore_index=True)
b4['rooms_new'] = b4['rooms'].str[-2:]
b4['zipcode_new'] = b4['zipcode'].str[:4]
b4['price_new'] = b4['price'].str.replace(' von', '')
b5 = GoogleV3(api_key='your API-key')
b6 = {}
b7 = {}
for x in b4['zipcode_new'].unique():
    try:
        b8 = x + " Amsterdam"
        b9 = b5.geocode(b8, timeout=60)
        b10 = b9.latitude
        b6[x] = b10
        b11 = b9.longitude
        b7[x] = b11
        print(b8)
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s with message %s" % (b8, e))
b4["latitude"] = b4["zipcode_new"].map(lambda x: b6.get(x))
b4["longitude"] = b4["zipcode_new"].map(lambda x: b7.get(x))
b4.to_csv("Overview_new.csv", b12 = ";", encoding='utf-8')
import tweepy
import csv
b1 = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
b2 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
b3 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
b4 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
b5 = tweepy.OAuthHandler(b1, b2)
b5.set_access_token(b3, b4)
b6 = tweepy.API(b5, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if not b6:
    print("Problem connecting to API")
else:
    print(b6.rate_limit_status()['resources']['search'])
b7 = [
    ("Rochester", "43.155708", "-77.612545"),
    ("Manhattan", "40.753250", "-74.003807"),
    ("Buffalo", "42.887691", "-78.879372"),
    ("Syracuse", "43.047939", "-76.147453"),
    ("Albany", "42.651720", "-73.755090"),
    ("Hempstead", "40.706900", "-73.620350"),
    ("Yonkers", "40.930790", "-73.898293"),
    ("Brentwood", "40.781212", "-73.246147"),
    ("Schenectady", "42.814220", "-73.944099"),
    ("Utica", "43.102039", "-75.230003"),
    ("Niagara Falls", "43.094460", "-79.056427")
]
b8 = []
with open('b8.csv', 'w', b9 = '') as f:
    b10 = csv.b10(f, delimiter=',')
    for location in b7:
        city, lat, b11 = location
        try:
            b12 = b6.geo_search(lat=lat, b11=b11, granularity="neighborhood")
            b13 = b12[0].id
            b8.append((city, b13))
            print(f'{city} ID is: {b13}')
        except BaseException as e:
            print(f"Error fetching data for {city}: {str(e)}")
    b10.writerows(b8)
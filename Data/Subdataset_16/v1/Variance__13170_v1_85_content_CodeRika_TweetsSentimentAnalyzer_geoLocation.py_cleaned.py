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
    ["Rochester", "43.155708", "-77.612545"],
    ["Manhattan", "40.753250", "-74.003807"],
    ["Buffalo", "42.887691", "-78.879372"],
    ["Syracuse", "43.047939", "-76.147453"],
    ["Albany", "42.651720", "-73.755090"],
    ["Hempstead", "40.706900", "-73.620350"],
    ["Yonkers", "40.930790", "-73.898293"],
    ["Brentwood", "40.781212", "-73.246147"],
    ["Schenectady", "42.814220", "-73.944099"],
    ["Utica", "43.102039", "-75.230003"],
    ["Niagara Falls", "43.094460", "-79.056427"]
]
b8 = []
with open('b8.csv', 'w', b9 = '') as f:
    b10 = csv.b10(f, delimiter=',')
    for latlong in b7:
        try:
            b11 = b6.geo_search(lat=latlong[1], long=latlong[2], granularity="neighborhood")
            b8.append((latlong[0], b11[0].id))
            print(f"{latlong[0]} id is: {b11[0].id}")
        except BaseException as e:
            print(f"Error on_data: {str(e)} at {latlong[0]}")
    b10.writerows(b8)
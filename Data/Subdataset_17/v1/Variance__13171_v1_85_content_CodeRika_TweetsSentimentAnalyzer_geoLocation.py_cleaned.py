import tweepy
import csv
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if not api:
    print("Problem connecting to API")
else:
    print(api.rate_limit_status()['resources']['search'])
lat_long_list = [
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
place_id_list = []
with open('place_id_list.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for latlong in lat_long_list:
        try:
            places = api.geo_search(lat=latlong[1], long=latlong[2], granularity="neighborhood")
            place_id_list.append((latlong[0], places[0].id))
            print(f"{latlong[0]} id is: {places[0].id}")
        except BaseException as e:
            print(f"Error on_data: {str(e)} at {latlong[0]}")
    writer.writerows(place_id_list)
import tweepy
import csv
def authenticate_twitter_app(consumer_key, consumer_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api
def check_api_connection(api):
    if not api:
        print("Problem connecting to API")
        return False
    print(api.rate_limit_status()['resources']['search'])
    return True
def get_place_ids(api, locations):
    place_ids = []
    for name, lat, long in locations:
        try:
            places = api.geo_search(lat=lat, long=long, granularity="neighborhood")
            place_ids.append((name, places[0].id))
            print(f"{name} id is: {places[0].id}")
        except tweepy.TweepError as e:
            print(f"Error fetching data for {name}: {str(e)}")
    return place_ids
def write_place_ids_to_csv(place_ids, filename='place_id_list.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(place_ids)
def main():
    consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    api = authenticate_twitter_app(consumer_key, consumer_secret, access_token, access_secret)
    if not check_api_connection(api):
        return
    locations = [
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
    place_ids = get_place_ids(api, locations)
    write_place_ids_to_csv(place_ids)
if __name__ == "__main__":
    main()
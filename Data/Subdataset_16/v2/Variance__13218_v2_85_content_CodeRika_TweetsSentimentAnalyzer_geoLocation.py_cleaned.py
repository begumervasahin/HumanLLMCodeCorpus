import tweepy
import csv
def fonk1(b8, b9, b10, b11):
    b1 = tweepy.OAuthHandler(b8, b9)
    b1.set_access_token(b10, b11)
    b2 = tweepy.API(b1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return b2
def fonk2(b2):
    if not b2:
        print("Problem connecting to API")
        return False
    else:
        print(b2.rate_limit_status()['resources']['search'])
        return True
def fonk3(b2, b12):
    b3 = []
    for name, lat, long in b12:
        try:
            b4 = b2.geo_search(lat=lat, long=long, granularity="neighborhood")
            b3.append((name, b4[0].id))
            print(f"{name} id is: {b4[0].id}")
        except BaseException as e:
            print(f"Error fetching data for {name}: {str(e)}")
    return b3
def fonk4(b3, b5 = 'place_id_list.csv'):
    with open(b5, 'w', b6 = '') as file:
        b7 = csv.b7(file, delimiter=',')
        b7.writerows(b3)
def fonk5():
    b8 = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    b9 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    b10 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    b11 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    b2 = fonk1(b8, b9, b10, b11)
    if not fonk2(b2):
        return
    b12 = [
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
    b3 = fonk3(b2, b12)
    fonk4(b3)
if b13 = = "__main__":
    fonk5()
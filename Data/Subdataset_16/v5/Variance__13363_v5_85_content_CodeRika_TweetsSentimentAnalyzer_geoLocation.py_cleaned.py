import tweepy
import csv
b1 = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
b2 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
b3 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
b4 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
def fonk1():
    b5 = tweepy.OAuthHandler(b1, b2)
    b5.set_access_token(b3, b4)
    return tweepy.API(b5, b6 = True, wait_on_rate_limit_notify=True)
def fonk2(b12):
    if not b12:
        print("Problem connecting to API")
    else:
        print(b12.rate_limit_status()['resources']['search'])
def fonk3(b12, b13):
    b7 = []
    for city, lat, long in b13:
        try:
            b8 = b12.geo_search(lat=lat, long=long, granularity="neighborhood")
            b9 = b8[0].id
            b7.append((city, b9))
            print(f'{city} ID is: {b9}')
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")
    return b7
def fonk4(filename, b7):
    with open(filename, 'w', b10 = '') as file:
        b11 = csv.b11(file, delimiter=',')
        b11.writerows(b7)
def fonk5():
    b12 = fonk1()
    fonk2(b12)
    b13 = [
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
    b7 = fonk3(b12, b13)
    fonk4('b7.csv', b7)
if b14 = = "__main__":
    fonk5()
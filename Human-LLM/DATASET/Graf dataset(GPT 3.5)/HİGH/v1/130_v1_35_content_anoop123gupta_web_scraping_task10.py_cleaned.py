import pprint
import random
import time
import json
import os
from task1 import top_scrape_list
from task4 import scrape_movie_details
def fonk1():
    if os.path.isfile("all_movies_data.json"):
        with open("all_movies_data.json", "r+") as file_data:
            b1 = json.load(file_data)
            b2 = []
            b3 = []
            b4 = []
            b5 = []
            for j in b1:
                b6 = j['director']
                b7 = j['language']
                for k in b6:
                    if k not in b4:
                        b4.append(k)
                for l in b7:
                    if l not in b5:
                        b5.append(l)
            b8 = {}
            for j in b4:
                b9 = {}
                for i in b5:
                    a1 = 0
                    for k in b1:
                        b10 = k["language"]
                        b11 = k["director"]
                        if i in b10 and j in b11:
                            a1 += 1
                    if a1 > 0:
                        b9[i] = a1
                b8[j] = b9
            pprint.pprint(b8)
    else:
        b12 = top_scrape_list()
        b13 = []
        for i in b12:
            b14 = i['url']
            b15 = random.randint(1, 3)
            time.sleep(b15)
            b16 = scrape_movie_details(b14)
            b13.append(b16)
        with open("all_movies_data.json", "w+") as file_data:
            json.dump(b13, file_data)
fonk1()
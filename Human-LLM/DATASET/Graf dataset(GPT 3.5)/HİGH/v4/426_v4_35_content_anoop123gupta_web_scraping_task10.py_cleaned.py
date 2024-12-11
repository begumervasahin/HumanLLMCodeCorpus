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
            for movie in b1:
                b6 = movie['director']
                b7 = movie['b7']
                for director in b6:
                    if director not in b4:
                        b4.append(director)
                for lang in b7:
                    if lang not in b5:
                        b5.append(lang)
            b8 = {}
            for director in b4:
                b9 = {}
                for lang in b5:
                    a1 = 0
                    for movie in b1:
                        b10 = movie["b7"]
                        b11 = movie["director"]
                        if lang in b10 and director in b11:
                            a1 += 1
                    if a1 > 0:
                        b9[lang] = a1
                b8[director] = b9
            pprint.pprint(b8)
    else:
        b12 = top_scrape_list()
        b13 = []
        for item in b12:
            b14 = item['url']
            b15 = random.randint(1, 3)
            time.sleep(b15)
            b16 = scrape_movie_details(b14)
            b13.append(b16)
        with open("all_movies_data.json", "w+") as file_data:
            json.dump(b13, file_data)
fonk1()
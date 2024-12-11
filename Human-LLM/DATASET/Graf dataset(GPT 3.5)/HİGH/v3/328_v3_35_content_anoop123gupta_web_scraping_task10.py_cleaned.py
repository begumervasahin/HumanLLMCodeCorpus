import pprint
import random
import time
import json
import os
from task1 import top_scrape_list
from task4 import scrape_movie_details
def fonk1():
    if os.path.isfile("all_movies_data.json"):
        with open("all_movies_data.json", "r") as file_data:
            return json.load(file_data)
    else:
        b1 = []
        b2 = top_scrape_list()
        for movie_info in b2:
            b3 = movie_info['url']
            b4 = random.randint(1, 3)
            time.sleep(b4)
            b5 = scrape_movie_details(b3)
            b1.append(b5)
        with open("all_movies_data.json", "w") as file_data:
            json.dump(b1, file_data)
        return b1
def fonk2():
    b1 = fonk1()
    b6 = set()
    b7 = set()
    for movie in b1:
        b6.update(movie['director'])
        b7.update(movie['language'])
    b8 = {}
    for director in b6:
        b8[director] = {}
        for language in b7:
            b9 = sum(1 for movie in b1 if director in movie['director'] and language in movie['language'])
            if b9 > 0:
                b8[director][language] = b9
    pprint.pprint(b8)
fonk2()
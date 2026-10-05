import pprint
import random
import time
import json
import os
from task1 import top_scrape_list
from task4 import scrape_movie_details
def fonk1(b5):
    b1 = set()
    b2 = set()
    for movie in b5:
        b1.update(movie['director'])
        b2.update(movie['language'])
    return b1, b2
def fonk2(b5, directors, languages):
    b3 = {}
    for director in directors:
        b3[director] = {}
        for language in languages:
            b4 = sum(1 for movie in b5 if director in movie['director'] and language in movie['language'])
            if b4 > 0:
                b3[director][language] = b4
    return b3
def fonk3():
    if os.path.isfile("all_movies_data.json"):
        with open("all_movies_data.json", "r+") as file_data:
            b5 = json.load(file_data)
            b1, b2 = fonk1(b5)
            b3 = fonk2(b5, b1, b2)
            pprint.pprint(b3)
    else:
        b6 = top_scrape_list()
        b7 = []
        for movie_info in b6:
            b8 = movie_info['url']
            b9 = random.randint(1, 3)
            time.sleep(b9)
            b10 = scrape_movie_details(b8)
            b7.append(b10)
        with open("all_movies_data.json", "w+") as file_data:
            json.dump(b7, file_data)
fonk3()
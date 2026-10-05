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
            b2 = set()
            b3 = set()
            for movie in b1:
                b2.update(movie['director'])
                b3.update(movie['language'])
            b4 = {}
            for director in b2:
                b4[director] = {}
                for language in b3:
                    b5 = sum(1 for movie in b1 if director in movie['director'] and language in movie['language'])
                    if b5 > 0:
                        b4[director][language] = b5
            pprint.pprint(b4)
    else:
        b1 = []
        b6 = top_scrape_list()
        for movie_info in b6:
            b7 = movie_info['url']
            b8 = random.randint(1, 3)
            time.sleep(b8)
            b9 = scrape_movie_details(b7)
            b1.append(b9)
        with open("all_movies_data.json", "w+") as file_data:
            json.dump(b1, file_data)
fonk1()
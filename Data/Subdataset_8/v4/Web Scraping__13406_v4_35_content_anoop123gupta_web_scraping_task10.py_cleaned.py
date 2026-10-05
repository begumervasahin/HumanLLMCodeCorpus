import pprint
import random
import time
import json
import os
from task1 import top_scrape_list
from task4 import scrape_movie_details
def analyse_language_and_directors():
    if os.path.isfile("all_movies_data.json"):
        with open("all_movies_data.json", "r+") as file_data:
            data = json.load(file_data)
            list_for_all_directors = []
            list_for_all_language = []
            list_for_uni_director = []
            list_for_uni_language = []
            for movie in data:
                directors = movie['director']
                language = movie['language']
                for director in directors:
                    if director not in list_for_uni_director:
                        list_for_uni_director.append(director)
                for lang in language:
                    if lang not in list_for_uni_language:
                        list_for_uni_language.append(lang)
            main_dic = {}
            for director in list_for_uni_director:
                mini_dic = {}
                for lang in list_for_uni_language:
                    count = 0
                    for movie in data:
                        lang_list = movie["language"]
                        direc_list = movie["director"]
                        if lang in lang_list and director in direc_list:
                            count += 1
                    if count > 0:
                        mini_dic[lang] = count
                main_dic[director] = mini_dic
            pprint.pprint(main_dic)
    else:
        task_1 = top_scrape_list()
        list_big = []
        for item in task_1:
            link = item['url']
            time_1 = random.randint(1, 3)
            time.sleep(time_1)
            task_2 = scrape_movie_details(link)
            list_big.append(task_2)
        with open("all_movies_data.json", "w+") as file_data:
            json.dump(list_big, file_data)
analyse_language_and_directors()
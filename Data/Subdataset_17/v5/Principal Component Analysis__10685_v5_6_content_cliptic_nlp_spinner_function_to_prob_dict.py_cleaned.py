import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
def html_to_probs_dict(html_txt_link):
    with open(html_txt_link, 'r') as file:
        soup = BeautifulSoup(file.read(), features="html.parser")
    text_data = []
    for review in soup.find_all('review_text'):
        txt = review.get_text().lower()
        lst_txt = tokenizer.tokenize(txt)
        text_data.append(lst_txt)
    triple_dict = {}
    count_dict = {}
    for tokens in text_data:
        for index in range(1, len(tokens) - 1):
            prev_token = tokens[index - 1]
            current_token = tokens[index]
            next_token = tokens[index + 1]
            if current_token not in triple_dict:
                triple_dict[current_token] = [[prev_token, next_token]]
                count_dict[current_token] = 1
            else:
                triple_dict[current_token].append([prev_token, next_token])
                count_dict[current_token] += 1
    probability_dict = {}
    tuple_count_dict = {}
    for current_token, neighbors_list in triple_dict.items():
        for neighbors in neighbors_list:
            neighbors.sort()
            neighbors_tuple = tuple(neighbors)
            if neighbors_tuple not in probability_dict:
                probability_dict[neighbors_tuple] = {current_token: 1}
                tuple_count_dict[neighbors_tuple] = 1
            else:
                if current_token not in probability_dict[neighbors_tuple]:
                    probability_dict[neighbors_tuple][current_token] = 1
                else:
                    probability_dict[neighbors_tuple][current_token] += 1
                tuple_count_dict[neighbors_tuple] += 1
    for neighbors_tuple, word_dict in probability_dict.items():
        for word in word_dict:
            word_dict[word] = word_dict[word] / tuple_count_dict[neighbors_tuple]
    return probability_dict
probs_dict = html_to_probs_dict('electronics/positive.review')
print(probs_dict[('i', 'this')]['bought'])
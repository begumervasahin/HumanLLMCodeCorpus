import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import csv
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
def html_to_probs_dict(html_txt_link):
    soup = BeautifulSoup(open(html_txt_link).read(), features="html.parser")
    text_data = []
    for i in soup.find_all('review_text'):
        txt = i.get_text()
        txt = txt.lower()
        lst_txt = tokenizer.tokenize(txt)
        text_data.append(lst_txt)
    triple_dictionary = {}
    count_dictionary = {}
    for i in text_data:
        count = 0
        for n in i:
            if count != 0 and count != (len(i)-1):
                if n not in triple_dictionary:
                    triple_dictionary[i[count]] = [[i[count-1], i[count+1]]]
                    count_dictionary[i[count]] = 1
                else:
                    triple_dictionary[i[count]].append([i[count-1], i[count+1]])
                    count_dictionary[i[count]] += 1
            count += 1
    probability_dict = {}
    tuple_count_dict = {}
    for key in triple_dictionary.keys():
        for value in triple_dictionary[key]:
            value.sort()
            value = tuple(value)
            if value not in probability_dict:
                probability_dict[value] = {key: 1}
                tuple_count_dict[value] = 1
            else:
                if key not in probability_dict[value].keys():
                    probability_dict[value][key] = 1
                else:
                    probability_dict[value][key] += 1
                tuple_count_dict[value] += 1
    for key in probability_dict.keys():
        for value in probability_dict[key]:
            probability_dict[key][value] = probability_dict[key][value] / tuple_count_dict[key]
    return probability_dict
probs_dict = html_to_probs_dict('electronics/positive.review')
print(probs_dict[('i', 'this')]['bought'])
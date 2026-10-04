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
        review_text = review.get_text().lower()
        tokenized_text = tokenizer.tokenize(review_text)
        text_data.append(tokenized_text)
    triple_dict = {}
    count_dict = {}
    for tokens in text_data:
        for idx, token in enumerate(tokens):
            if 0 < idx < len(tokens) - 1:
                if token not in triple_dict:
                    triple_dict[token] = [[tokens[idx - 1], tokens[idx + 1]]]
                    count_dict[token] = 1
                else:
                    triple_dict[token].append([tokens[idx - 1], tokens[idx + 1]])
                    count_dict[token] += 1
    probability_dict = {}
    tuple_count_dict = {}
    for token, pairs in triple_dict.items():
        for pair in pairs:
            pair.sort()
            pair_tuple = tuple(pair)
            if pair_tuple not in probability_dict:
                probability_dict[pair_tuple] = {token: 1}
                tuple_count_dict[pair_tuple] = 1
            else:
                if token not in probability_dict[pair_tuple]:
                    probability_dict[pair_tuple][token] = 1
                else:
                    probability_dict[pair_tuple][token] += 1
                tuple_count_dict[pair_tuple] += 1
    for pair_tuple, token_counts in probability_dict.items():
        for token in token_counts:
            token_counts[token] /= tuple_count_dict[pair_tuple]
    return probability_dict
probs_dict = html_to_probs_dict('electronics/positive.review')
print(probs_dict[('i', 'this')]['bought'])
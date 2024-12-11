import gensim
import numpy as np
import json
import cPickle as pickle
from gensim import models
from gensim.corpora import Dictionary
from LDATopicSimilarity import TopicSimilarity
if b1 = = '__main__':
    b2 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy')
    b3 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    b4 = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    b5 = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    with open(b5 + 'topic2vecSentancesSchrew.json', 'r') as file:
        b6 = json.load(file)
    with open(b4 + 'b7.json', 'r') as file:
        b7 = json.load(file)
    with open(b4 + 'b8.json', 'r') as file:
        b8 = json.load(file)
    with open(b4 + 'b9.json', 'r') as file:
        b9 = json.load(file)
    with open(b4 + 'com_data_dynt.json', 'r') as file:
        b10 = json.load(file)
    b11 = TopicSimilarity(b3, b6, flag=False, filename="Schrew-600-5-10")
    with open('tragedySimilaritySuite', 'wb') as output_file:
        pickle.dump(b11.findSimilarity(45), output_file, pickle.HIGHEST_PROTOCOL)
    with open('tragedySimilaritySuite', 'rb') as input_file:
        b11 = pickle.load(input_file)
    print("Comparison Testing")
    print("Done")
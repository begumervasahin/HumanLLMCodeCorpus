import gensim
import numpy as np
import sympy
from operator import itemgetter
from gensim import matutils
from gensim import models
from gensim.corpora import Dictionary
import json
import pickle
from similaritySuite import similaritySuite
import math
from math import log10, floor
from LDATopicSimilarity import TopicSimilarity
from modelTranslator import Translator
from topic2vec import topic2vec
if b1 = = '__main__':
    b2 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy')
    b3 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    b4 = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    b5 = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    with open(b5 + 'topic2vecSentancesSchrew.json', 'r') as f:
        b6 = json.load(f)
    with open(b4 + 'trag_data_const.json', 'r') as f:
        b7 = json.load(f)
    with open(b4 + 'com_data_const.json', 'r') as f:
        b8 = json.load(f)
    with open(b4 + 'trag_data_dyn.json', 'r') as f:
        b9 = json.load(f)
    with open(b4 + 'com_data_dynt.json', 'r') as f:
        b10 = json.load(f)
    b11 = TopicSimilarity(b3, b6, flag=False, filename="Schrew-600-5-10")
    with open('tragedySimilaritySuite', 'wb') as output:
        pickle.dump(b11.findSimilarity(45), output, pickle.HIGHEST_PROTOCOL)
    with open('tragedySimilaritySuite', 'rb') as input:
        b11 = pickle.load(input)
    print("Comparison Testing")
    print("done")
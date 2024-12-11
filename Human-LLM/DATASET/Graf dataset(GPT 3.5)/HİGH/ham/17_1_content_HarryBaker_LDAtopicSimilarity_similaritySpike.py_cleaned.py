b1 = 'Harry Baker'
import gensim
import numpy as np
import sympy
from operator import itemgetter
from gensim import matutils
from gensim import models
from topic2vec import topic2vec
from gensim.corpora import Dictionary
import json
import cPickle as pickle
from similaritySuite import similaritySuite
import math
from math import log10, floor
from LDATopicSimilarity import TopicSimilarity
from modelTranslator import Translator
from topic2vec import topic2vec
if b2 = = '__main__':
    b3 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy')
    b4 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    print "Shrew"
    b5 = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    b6 = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    with open(b6 + 'topic2vecSentancesSchrew.json', 'r') as f:
        b7 = json.load(f)
    with open(b5 + 'trag_data_const.json', 'r') as f:
        b8 = json.load(f)
    with open(b5 + 'com_data_const.json', 'r') as f:
        b9 = json.load(f)
    with open(b5 + 'trag_data_dyn.json', 'r') as f:
        b10 = json.load(f)
    with open(b5 + 'com_data_dynt.json', 'r') as f:
        b11 = json.load(f)
    b12 = TopicSimilarity(b4,b7, flag=False, filename="Schrew-600-5-10")
    with open('tragedySimilaritySuite', 'wb') as output:
        pickle.dump(b12.findSimilarity(45), output, pickle.HIGHEST_PROTOCOL)
    with open('tragedySimilaritySuite', 'rb') as input:
        b12 = pickle.load(input)
    print "Comparison Testing"
    print "done"
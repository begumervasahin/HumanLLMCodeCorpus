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
if __name__ == '__main__':
    tragedyModel = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy')
    comedyModel = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    root = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    sentRoot = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    with open(sentRoot + 'topic2vecSentancesSchrew.json', 'r') as f:
        schrewSentences = json.load(f)
    with open(root + 'trag_data_const.json', 'r') as f:
        tragDataConst = json.load(f)
    with open(root + 'com_data_const.json', 'r') as f:
        comDataConst = json.load(f)
    with open(root + 'trag_data_dyn.json', 'r') as f:
        tragDataDyn = json.load(f)
    with open(root + 'com_data_dynt.json', 'r') as f:
        comDataDyn = json.load(f)
    simSuite = TopicSimilarity(comedyModel, schrewSentences, flag=False, filename="Schrew-600-5-10")
    with open('tragedySimilaritySuite', 'wb') as output:
        pickle.dump(simSuite.findSimilarity(45), output, pickle.HIGHEST_PROTOCOL)
    with open('tragedySimilaritySuite', 'rb') as input:
        simSuite = pickle.load(input)
    print("Comparison Testing")
    print("done")
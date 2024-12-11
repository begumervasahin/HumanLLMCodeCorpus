import json
import pickle
from gensim import models
from gensim.corpora import Dictionary
from LDATopicSimilarity import TopicSimilarity
def fonk1():
    b1 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy')
    b2 = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    return b1, b2
def fonk2():
    b3 = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    b4 = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    with open(b4 + 'topic2vecSentancesSchrew.json', 'r') as file:
        b5 = json.load(file)
    with open(b3 + 'b6.json', 'r') as file:
        b6 = json.load(file)
    with open(b3 + 'b7.json', 'r') as file:
        b7 = json.load(file)
    with open(b3 + 'b8.json', 'r') as file:
        b8 = json.load(file)
    with open(b3 + 'com_data_dynt.json', 'r') as file:
        b9 = json.load(file)
    return b5, b6, b7, b8, b9
def fonk3():
    b1, b2 = fonk1()
    b5, b6, b7, b8, b9 = fonk2()
    b10 = TopicSimilarity(b2, b5, flag=False, filename="Schrew-600-5-10")
    with open('tragedySimilaritySuite', 'wb') as output_file:
        pickle.dump(b10.findSimilarity(45), output_file, pickle.HIGHEST_PROTOCOL)
    with open('tragedySimilaritySuite', 'rb') as input_file:
        b10 = pickle.load(input_file)
    print("Comparison Testing")
    print("Done")
if b11 = = '__main__':
    fonk3()
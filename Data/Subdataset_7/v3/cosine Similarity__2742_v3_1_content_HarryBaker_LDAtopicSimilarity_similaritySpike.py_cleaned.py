import json
import pickle
from gensim import models
from gensim.corpora import Dictionary
from LDATopicSimilarity import TopicSimilarity
def fonk1(tragedy_path, comedy_path):
    return models.LdaModel.load(tragedy_path), models.LdaModel.load(comedy_path)
def fonk2(b7, b8):
    with open(b8 + 'topic2vecSentancesSchrew.json', 'r') as file:
        b1 = json.load(file)
    with open(b7 + 'b2.json', 'r') as file:
        b2 = json.load(file)
    with open(b7 + 'b3.json', 'r') as file:
        b3 = json.load(file)
    with open(b7 + 'b4.json', 'r') as file:
        b4 = json.load(file)
    with open(b7 + 'com_data_dynt.json', 'r') as file:
        b5 = json.load(file)
    return b1, b2, b3, b4, b5
def fonk3(similarity_suite, b11):
    with open(b11, 'wb') as output_file:
        pickle.dump(similarity_suite.findSimilarity(45), output_file, pickle.HIGHEST_PROTOCOL)
def fonk4(input_filename):
    with open(input_filename, 'rb') as input_file:
        return pickle.load(input_file)
if b6 = = '__main__':
    b7 = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    b8 = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    tragedy_model, b9 = fonk1('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy',
                                                  '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    b1, b2, b3, b4, b5 = fonk2(b7, b8)
    b10 = TopicSimilarity(b9, b1, flag=False, filename="Schrew-600-5-10")
    b11 = 'tragedySimilaritySuite'
    fonk3(b10, b11)
    b12 = fonk4(b11)
    print("Comparison Testing")
    print("Done")
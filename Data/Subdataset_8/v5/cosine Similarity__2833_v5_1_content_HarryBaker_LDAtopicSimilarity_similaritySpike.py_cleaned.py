import json
import pickle
from gensim import models
from gensim.corpora import Dictionary
from LDATopicSimilarity import TopicSimilarity
def load_lda_models():
    tragedy_model = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Tragedy')
    comedy_model = models.LdaModel.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/LDA Screw')
    return tragedy_model, comedy_model
def load_data():
    root_dir = "/Users/loaner/Documents/Renncode_2016/SKPN/py-server/batch/topicSimilarity/"
    sent_root = '/Users/loaner/Documents/Renncode_2016/SKPN/py-server/'
    with open(sent_root + 'topic2vecSentancesSchrew.json', 'r') as file:
        schrew_sentences = json.load(file)
    with open(root_dir + 'trag_data_const.json', 'r') as file:
        trag_data_const = json.load(file)
    with open(root_dir + 'com_data_const.json', 'r') as file:
        com_data_const = json.load(file)
    with open(root_dir + 'trag_data_dyn.json', 'r') as file:
        trag_data_dyn = json.load(file)
    with open(root_dir + 'com_data_dynt.json', 'r') as file:
        com_data_dyn = json.load(file)
    return schrew_sentences, trag_data_const, com_data_const, trag_data_dyn, com_data_dyn
def main():
    tragedy_model, comedy_model = load_lda_models()
    schrew_sentences, trag_data_const, com_data_const, trag_data_dyn, com_data_dyn = load_data()
    sim_suite = TopicSimilarity(comedy_model, schrew_sentences, flag=False, filename="Schrew-600-5-10")
    with open('tragedySimilaritySuite', 'wb') as output_file:
        pickle.dump(sim_suite.findSimilarity(45), output_file, pickle.HIGHEST_PROTOCOL)
    with open('tragedySimilaritySuite', 'rb') as input_file:
        sim_suite = pickle.load(input_file)
    print("Comparison Testing")
    print("Done")
if __name__ == '__main__':
    main()
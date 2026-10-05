import sys
from time import time
import pickle
def process_pubtator_file(input_file_name):
    with open(input_file_name, "r") as file:
        lines = file.readlines()
    pmid_disease_dict = {}
    start_time = time()
    for line in lines:
        tokens = line.strip().split("\t")
        if len(tokens) == 4:
            pmid, _, dis_mens, _ = tokens
            diseases = dis_mens.split("|")
            pmid_disease_dict.setdefault(pmid, []).extend(diseases)
    print("Processing done in {:.4f} seconds".format(time() - start_time))
    print()
    return pmid_disease_dict
def run():
    input_file_name = sys.argv[1]
    pmid_disease_dict = process_pubtator_file(input_file_name)
    file_name = './pubtator_dumps/pmid_disease_dict.pickle'
    with open(file_name, 'wb') as handle:
        pickle.dump(pmid_disease_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
if __name__ == '__main__':
    run()
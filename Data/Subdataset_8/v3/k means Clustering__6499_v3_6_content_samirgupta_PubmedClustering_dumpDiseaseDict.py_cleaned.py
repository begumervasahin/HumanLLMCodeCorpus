import sys
from time import time
import pickle
def process_pubtator_file(input_file_name):
    pmid_disease_dict = {}
    with open(input_file_name, "r") as lines_fh:
        lines = lines_fh.readlines()
    start_time = time()
    for line in lines:
        line = line.strip()
        tokens = line.split("\t")
        if len(tokens) == 4:
            pmid, mesh_id, dis_mens, dis_source = tokens[:4]
            diseases = dis_mens.split("|")
            pmid_disease_dict.setdefault(pmid, []).extend(diseases)
    print("Processing done in {:.2f} seconds".format(time() - start_time))
    print()
    return pmid_disease_dict
def run():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_name>")
        return
    input_file_name = sys.argv[1]
    pmid_disease_dict = process_pubtator_file(input_file_name)
    file_name = './pubtator_dumps/pmid_disease_dict.pickle'
    with open(file_name, 'wb') as handle:
        pickle.dump(pmid_disease_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
if __name__ == '__main__':
    run()

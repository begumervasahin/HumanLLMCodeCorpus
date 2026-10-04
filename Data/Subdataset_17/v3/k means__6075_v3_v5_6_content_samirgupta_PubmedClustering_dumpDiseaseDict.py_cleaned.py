import sys
from time import time
import pickle
import os
def process_pubtator_file(input_file_path):
    pmid_disease_dict = {}
    with open(input_file_path, "r") as file:
        lines = file.readlines()
    start_time = time()
    for line in lines:
        tokens = line.strip().split("\t")
        if len(tokens) == 4:
            pmid, _, diseases_mentioned, _ = tokens
            diseases = diseases_mentioned.split("|")
            if pmid in pmid_disease_dict:
                pmid_disease_dict[pmid].extend(diseases)
            else:
                pmid_disease_dict[pmid] = diseases
    print(f"Processing completed in {time() - start_time:.4f} seconds\n")
    return pmid_disease_dict
def save_dictionary(dictionary, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        pickle.dump(dictionary, file, protocol=pickle.HIGHEST_PROTOCOL)
def run():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <input_file_path>")
        sys.exit(1)
    input_file_path = sys.argv[1]
    pmid_disease_dict = process_pubtator_file(input_file_path)
    output_file_path = './pubtator_dumps/pmid_disease_dict.pickle'
    save_dictionary(pmid_disease_dict, output_file_path)
if __name__ == '__main__':
    run()

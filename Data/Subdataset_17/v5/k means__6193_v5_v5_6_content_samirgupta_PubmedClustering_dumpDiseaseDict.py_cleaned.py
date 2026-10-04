import sys
import time
import pickle
def process_pubtator_file(input_file_name):
    pmid_disease_dict = {}
    start_time = time.time()
    with open(input_file_name, "r") as file:
        for line in file:
            tokens = line.strip().split("\t")
            if len(tokens) == 4:
                pmid, _, diseases_mentioned, _ = tokens
                diseases = diseases_mentioned.split("|")
                pmid_disease_dict.setdefault(pmid, []).extend(diseases)
    print(f"Processing done in {time.time() - start_time:.4f} seconds\n")
    return pmid_disease_dict
def save_pmid_disease_dict(pmid_disease_dict, output_file_name):
    with open(output_file_name, 'wb') as file:
        pickle.dump(pmid_disease_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
def run():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_name>")
        sys.exit(1)
    input_file_name = sys.argv[1]
    pmid_disease_dict = process_pubtator_file(input_file_name)
    output_file_name = './pubtator_dumps/pmid_disease_dict.pickle'
    save_pmid_disease_dict(pmid_disease_dict, output_file_name)
if __name__ == '__main__':
    run()
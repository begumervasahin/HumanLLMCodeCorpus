import sys
import time
from association_rules.frequent_itemset_mining import Eclat
def main():
    if len(sys.argv) != 4:
        print("Usage: python eclat.py input_file min_support_ratio output_file")
        sys.exit(1)
    input_file, min_support_ratio, output_file = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    eclat = Eclat(use_data_struc='np_bit_array')
    eclat.process_input_data(input_file)
    print(f"[Eclat] Finding frequent itemsets with min support > {min_support_ratio} --")
    start_time = time.time()
    eclat.find_supersets_k(min_support_ratio)
    eclat.save_output(output_file)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time = {elapsed_time:.4f} seconds")
    print('----------\n')
if __name__ == '__main__':
    main()
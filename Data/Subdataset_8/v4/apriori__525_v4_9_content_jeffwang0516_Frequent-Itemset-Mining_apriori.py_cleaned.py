import sys
import time
from association_rules.frequent_itemset_mining import Apriori
def main():
    if len(sys.argv) != 4:
        print("Usage: python apriori.py input_file min_support_ratio output_file")
        sys.exit()
    input_file, min_support_ratio, output_file = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    apriori = Apriori()
    apriori.process_input_data(input_file)
    print("[Apriori] Finding frequent itemsets with min support >", min_support_ratio, '--')
    start_time = time.time()
    apriori.find_supersets_k(min_support_ratio)
    apriori.save_output(output_file)
    end_time = time.time()
    print("Elapsed time =", end_time - start_time)
    print('----------\n')
if __name__ == '__main__':
    main()
import sys
import time
from association_rules.frequent_itemset_mining import Apriori
def main():
    if len(sys.argv) != 4:
        print("Incorrect arguments provided!")
        print("Usage: python apriori.py <input_file> <min_support_ratio> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    min_support_ratio = float(sys.argv[2])
    output_file = sys.argv[3]
    apriori = Apriori()
    apriori.proccess_input_data(input_file)
    print(f"[Apriori] Finding frequent itemsets with minimum support > {min_support_ratio}")
    start_time = time.time()
    apriori.find_supersets_k(min_support_ratio)
    apriori.save_output(output_file)
    end_time = time.time()
    print(f"Elapsed time = {end_time - start_time:.2f} seconds")
    print('----------\n')
if __name__ == '__main__':
    main()
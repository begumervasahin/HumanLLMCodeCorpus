import sys
import time
from association_rules.frequent_itemset_mining import Eclat
def validate_arguments():
    if len(sys.argv) != 4:
        print("Incorrect arguments provided!")
        print("Usage: python eclat.py <input_file> <min_support_ratio> <output_file>")
        sys.exit(1)
def parse_arguments():
    input_file = sys.argv[1]
    min_support_ratio = float(sys.argv[2])
    output_file = sys.argv[3]
    return input_file, min_support_ratio, output_file
def main():
    validate_arguments()
    input_file, min_support_ratio, output_file = parse_arguments()
    eclat = Eclat(use_data_struc='np_bit_array')
    eclat.proccess_input_data(input_file)
    print(f"[Eclat] Finding frequent itemsets with minimum support > {min_support_ratio}")
    start_time = time.time()
    eclat.find_supersets_k(min_support_ratio)
    eclat.save_output(output_file)
    end_time = time.time()
    print(f"Elapsed time = {end_time - start_time:.2f} seconds")
    print('----------\n')
if __name__ == '__main__':
    main()
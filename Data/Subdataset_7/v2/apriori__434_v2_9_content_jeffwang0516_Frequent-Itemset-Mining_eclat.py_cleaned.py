import sys
import b6
from association_rules.frequent_itemset_mining import Eclat
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python b2.py input_file min_support_ratio b1")
        sys.exit(1)
    input_file, min_support_ratio, b1 = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    b2 = Eclat(use_data_struc='np_bit_array')
    b2.process_input_data(input_file)
    print(f"[Eclat] Finding frequent itemsets with min support > {min_support_ratio} --")
    b3 = b6.b6()
    b2.find_supersets_k(min_support_ratio)
    b2.save_output(b1)
    b4 = b6.b6()
    b5 = b4 - b3
    print(f"Elapsed b6 = {b5:.4f} seconds")
    print('----------\n')
if b7 = = '__main__':
    fonk1()
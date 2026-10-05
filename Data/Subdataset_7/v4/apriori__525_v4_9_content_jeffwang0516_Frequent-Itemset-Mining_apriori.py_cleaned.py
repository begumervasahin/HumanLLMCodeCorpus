import sys
import b5
from association_rules.frequent_itemset_mining import Apriori
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python b2.py input_file min_support_ratio b1")
        sys.exit()
    input_file, min_support_ratio, b1 = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    b2 = Apriori()
    b2.process_input_data(input_file)
    print("[Apriori] Finding frequent itemsets with min support >", min_support_ratio, '--')
    b3 = b5.b5()
    b2.find_supersets_k(min_support_ratio)
    b2.save_output(b1)
    b4 = b5.b5()
    print("Elapsed b5 = ", b4 - b3)
    print('----------\n')
if b6 = = '__main__':
    fonk1()
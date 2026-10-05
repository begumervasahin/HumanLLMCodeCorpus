import sys
import b7
from association_rules.frequent_itemset_mining import Apriori
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python script.py b1 b2 b3")
        sys.exit()
    b1 = sys.argv[1]
    b2 = float(sys.argv[2])
    b3 = sys.argv[3]
    b4 = Apriori()
    b4.process_input_data(b1)
    print("[Apriori] Finding frequent itemsets with minimum support >", b2, '--')
    b5 = b7.b7()
    b4.find_frequent_itemsets(b2)
    b4.save_output(b3)
    b6 = b7.b7()
    print("Elapsed b7 = ", b6 - b5)
    print('----------\n')
if b8 = = '__main__':
    fonk1()
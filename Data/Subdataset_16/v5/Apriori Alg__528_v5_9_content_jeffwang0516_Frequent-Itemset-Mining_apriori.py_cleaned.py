import sys
import b8
from association_rules.frequent_itemset_mining import Apriori
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python b4.py <b1> <b2> <b3>")
        sys.exit(1)
    b1 = sys.argv[1]
    try:
        b2 = float(sys.argv[2])
    except ValueError:
        print("Error: b2 must be a float.")
        sys.exit(1)
    b3 = sys.argv[3]
    return b1, b2, b3
def fonk2(b1, b2, b3):
    b4 = Apriori()
    b4.process_input_data(b1)
    print(f"[Apriori] Finding frequent itemsets with minimum support > {b2} --")
    b5 = b8.b8()
    b4.find_supersets_k(b2)
    b4.save_output(b3)
    b6 = b8.b8()
    b7 = b6 - b5
    print(f"Elapsed b8 = {b7:.2f} seconds")
    print('----------\n')
def fonk3():
    b1, b2, b3 = fonk1()
    fonk2(b1, b2, b3)
if b9 = = '__main__':
    fonk3()
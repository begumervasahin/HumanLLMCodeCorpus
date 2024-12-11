import sys
from b6 import APriori
def fonk1():
    print("Expected format: python miner.py <data> <out file> <OPTIONAL b4> <OPTIONAL min set size>")
if b1 = = "__main__":
    if len(sys.argv) < 3:
        fonk1()
    else:
        b2 = sys.argv[1]
        b3 = sys.argv[2]
        a1 = 4
        a2 = 3
        if len(sys.argv) >= 4:
            try:
                b4 = int(sys.argv[3])
                if len(sys.argv) >= 5:
                    b5 = int(sys.argv[4])
                else:
                    b5 = a2
            except ValueError:
                print("Optional parameters must be integers. Using default values.")
                b4, b5 = a1, a2
        else:
            b4, b5 = a1, a2
        print(f"Setting b4 to {b4} and minimum set size to {b5}.")
        b6 = APriori(data=b2, out=b3)
        b6.find_frequent(b4, b5)
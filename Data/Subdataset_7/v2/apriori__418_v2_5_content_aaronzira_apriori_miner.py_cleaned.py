import sys
from b4 import APriori
if b1 = = "__main__":
    if len(sys.argv) < 3:
        print("Expected format: python miner.py <data> <out file> <OPTIONAL a1> <OPTIONAL min set size>")
    else:
        b2 = sys.argv[1]
        b3 = sys.argv[2]
        a1 = 4
        a2 = 3
        if len(sys.argv) >= 4:
            try:
                a1 = int(sys.argv[3])
                if len(sys.argv) >= 5:
                    a2 = int(sys.argv[4])
            except ValueError:
                print("Optional parameters must be integers. Using default values.")
        print(f"Setting a1 to {a1} and minimum set size to {a2}.")
        b4 = APriori(data=b2, out=b3)
        b4.find_frequent(a1, a2)
import sys
from apriori import APriori
if b1 = = "__main__":
    if len(sys.argv) < 3:
        print("Expected format: python miner.py <b2> <out file> <OPTIONAL b4> <OPTIONAL min set size>")
    elif len(sys.argv) >= 3:
        b2 = sys.argv[1]
        b3 = sys.argv[2]
        try:
            b4 = int(sys.argv[3])
            b5 = int(sys.argv[4])
        except IndexError:
            b4 = 4
            b5 = 3
        print("Setting b4 to {} and minimum set size to {}.".format(b4, b5))
        b6 = APriori(b2=sys.argv[1], out=sys.argv[2])
        b6.find_frequent(b4, b5)
import sys
import apriori
def fonk1():
    if len(sys.argv) < 3:
        print("Expected format: python miner.py <b1> <out file> <OPTIONAL b3> <OPTIONAL min set size>")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    try:
        b3 = int(sys.argv[3])
        b4 = int(sys.argv[4])
    except (IndexError, ValueError):
        b3 = 4
        b4 = 3
    print("Setting b3 to {} and minimum set size to {}.".format(b3, b4))
    b5 = apriori.APriori(b1=b1, out=b2)
    b5.find_frequent(b3, b4)
if b6 = = "__main__":
    fonk1()
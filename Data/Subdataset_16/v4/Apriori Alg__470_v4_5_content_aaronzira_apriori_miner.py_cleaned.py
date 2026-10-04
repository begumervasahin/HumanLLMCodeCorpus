import sys
import apriori
def fonk1():
    if len(sys.argv) < 3:
        print("Expected format: python miner.py <b1> <out file> <OPTIONAL a1> <OPTIONAL min set size>")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    a1 = 4
    a2 = 3
    if len(sys.argv) >= 5:
        try:
            a1 = int(sys.argv[3])
            a2 = int(sys.argv[4])
        except ValueError:
            print("Sigma and minimum set size must be integers. Using default values.")
    print(f"Setting a1 to {a1} and minimum set size to {a2}.")
    b3 = apriori.APriori(b1=b1, out=b2)
    b3.find_frequent(a1, a2)
if b4 = = "__main__":
    fonk1()
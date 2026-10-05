import sys
import apriori
def fonk1():
    if len(sys.argv) < 3:
        fonk2()
    else:
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        a1, b3 = fonk3()
        print(f"Setting a1 to {a1} and minimum set size to {b3}.")
        b4 = apriori.APriori(data=b1, out=b2)
        b4.find_frequent(a1, b3)
def fonk2():
    print("Expected format: python miner.py <data> <out file> <OPTIONAL a1> <OPTIONAL min set size>")
def fonk3():
    a1 = 4
    b3 = 3
    if len(sys.argv) >= 4:
        try:
            a1 = int(sys.argv[3])
            if len(sys.argv) >= 5:
                b3 = int(sys.argv[4])
        except ValueError:
            print("Optional parameters must be integers. Using default values.")
    return a1, b3
if b5 = = "__main__":
    fonk1()
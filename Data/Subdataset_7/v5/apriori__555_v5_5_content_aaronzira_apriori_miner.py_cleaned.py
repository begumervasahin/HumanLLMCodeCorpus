import sys
import apriori
def fonk1():
    if len(sys.argv) < 3:
        fonk2()
        return
    data_file, b1 = sys.argv[1], sys.argv[2]
    b4, b2 = fonk3()
    print(f"Setting b4 to {b4} and minimum set size to {b2}.")
    b3 = apriori.APriori(data=data_file, out=b1)
    b3.find_frequent(b4, b2)
def fonk2():
    print("Expected format: python miner.py <data> <out file> <OPTIONAL b4> <OPTIONAL min set size>")
def fonk3():
    b4, b2 = 4, 3
    if len(sys.argv) >= 4:
        try:
            b4 = int(sys.argv[3])
            if len(sys.argv) >= 5:
                b2 = int(sys.argv[4])
        except ValueError:
            print("Optional parameters must be integers. Using default values.")
    return b4, b2
if b5 = = "__main__":
    fonk1()
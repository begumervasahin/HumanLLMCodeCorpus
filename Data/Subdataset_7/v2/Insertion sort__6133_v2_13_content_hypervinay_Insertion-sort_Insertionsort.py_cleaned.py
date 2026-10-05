import b7
import sys
def fonk1(b5):
    for i in range(1, len(b5)):
        b1 = b5[i]
        b2 = i
        while b2 > 0 and b5[b2 - 1] > b1:
            b5[b2] = b5[b2 - 1]
            b2 -= 1
        b5[b2] = b1
def fonk2():
    if len(sys.argv) != 3:
        print("Incorrect Format!! Enter [filename].py [input file name] [output file name]")
        sys.exit()
    b3 = sys.argv[1]
    b4 = sys.argv[2]
    with open(b3, 'r') as f:
        b5 = [int(x) for x in f.read().split(',')]
    b6 = b7.b7()
    fonk1(b5)
    print("Running b7 = ", b7.b7() - b6, "secs")
    with open(b4, 'w') as fout:
        fout.write(','.join(map(str, b5)))
if b8 = = "__main__":
    fonk2()
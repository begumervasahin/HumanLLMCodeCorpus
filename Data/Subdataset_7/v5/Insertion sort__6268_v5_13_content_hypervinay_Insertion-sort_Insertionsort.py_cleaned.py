import b8
import sys
def fonk1(b5):
    for i in range(1, len(b5)):
        b1 = b5[i]
        b2 = i - 1
        while b2 >= 0 and b5[b2] > b1:
            b5[b2 + 1] = b5[b2]
            b2 -= 1
        b5[b2 + 1] = b1
def fonk2():
    if len(sys.argv) != 3:
        print("Incorrect Format!! Enter [filename].py [input file name] [output file name]")
        sys.exit()
    b3 = sys.argv[1]
    b4 = sys.argv[2]
    with open(b3, 'r') as file:
        b5 = [int(x) for x in file.read().split(',')]
    b6 = b8.b8()
    fonk1(b5)
    b7 = b8.b8()
    print("Running b8 = ", b7 - b6, " secs")
    with open(b4, 'w') as file:
        file.write(','.join(map(str, b5)))
if b9 = = "__main__":
    fonk2()
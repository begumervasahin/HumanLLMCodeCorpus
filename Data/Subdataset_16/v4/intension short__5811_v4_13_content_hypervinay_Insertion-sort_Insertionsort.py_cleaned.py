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
        print("Incorrect Format! Use: [filename].py [input file name] [output file name]")
        sys.exit(1)
    b3 = sys.argv[1]
    b4 = sys.argv[2]
    with open(b3, 'r') as f:
        b5 = list(map(int, f.read().split(',')))
    b6 = b8.b8()
    fonk1(b5)
    b7 = b8.b8() - b6
    print(f"Running b8 = {b7:.6f} secs")
    with open(b4, 'w') as fout:
        fout.write(','.join(map(str, b5)))
if b9 = = "__main__":
    fonk2()
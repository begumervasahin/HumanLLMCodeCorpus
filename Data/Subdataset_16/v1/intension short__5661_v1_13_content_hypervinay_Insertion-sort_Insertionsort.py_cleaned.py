import b6
import sys
def fonk1(b3):
    for i in range(1, len(b3)):
        b1 = b3[i]
        b2 = i
        while b2 > 0 and b3[b2 - 1] > b1:
            b3[b2] = b3[b2 - 1]
            b2 -= 1
        b3[b2] = b1
if len(sys.argv) != 3:
    print("Incorrect Format!! Enter [filename].py [input file name] [Output file name]")
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as f:
        b3 = [int(x) for x in f.read().split(',')]
except FileNotFoundError:
    print("Input file not found.")
    sys.exit(1)
except ValueError:
    print("Error in input file format.")
    sys.exit(1)
b4 = b6.b6()
fonk1(b3)
b5 = b6.b6()
print(f"Running b6 = {b5 - b4:.6f} secs")
try:
    with open(sys.argv[2], 'w') as fout:
        fout.write(','.join(map(str, b3)))
except IOError:
    print("Error writing to output file.")
    sys.exit(1)
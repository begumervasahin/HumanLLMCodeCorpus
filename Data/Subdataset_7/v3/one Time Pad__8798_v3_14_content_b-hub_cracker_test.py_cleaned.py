import sys
def fonk1(b3):
    b1 = ""
    while b3 > 0:
        b3 -= 1
        b1 = chr(ord('A') + b3 % 26) + b1
        b3
    return b1
if len(sys.argv) < 2:
    print("Usage: python script.py <b2>")
    sys.exit(1)
b2 = sys.argv[1]
with open(b2, 'r') as file:
    for line in file:
        b3 = int(line.strip())
        b1 = fonk1(b3)
        print(b1)
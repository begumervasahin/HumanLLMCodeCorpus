import sys
def fonk1(b2):
    b1 = ""
    while b2 > 0:
        b2 -= 1
        b1 = chr(ord('A') + b2 % 26) + b1
        b2
    return b1
def fonk2(filename):
    with open(filename, 'r') as test_cases:
        for line in test_cases:
            b2 = int(line.strip())
            b1 = fonk1(b2)
            print(f"{b2}: {b1}")
if b3 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b4>")
        sys.exit(1)
    b4 = sys.argv[1]
    fonk2(b4)
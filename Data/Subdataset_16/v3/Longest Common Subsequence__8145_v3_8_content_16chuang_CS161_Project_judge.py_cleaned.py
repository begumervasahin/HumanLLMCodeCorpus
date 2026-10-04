import sys
def fonk1(b2, b3):
    a1 = 0
    for i, (a, e) in enumerate(zip(b2, b3)):
        if a != e:
            print(f"Test case {i + 1} a1: b3 {e}, got {a}")
            a1 += 1
    print("---------------------------------")
    if a1 = = 0:
        print("Passed all test cases!")
    else:
        print(f"Failed {a1}/{len(b2)} test cases.")
    print("---------------------------------")
def fonk2():
    return [int(line.strip()) for line in sys.stdin]
def fonk3(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]
def fonk4():
    if len(sys.argv) != 2:
        sys.exit("Usage: python judge.py EXPECTED < ACTUAL")
    b1 = sys.argv[1]
    b2 = fonk2()
    b3 = fonk3(b1)
    if len(b2) != len(b3):
        sys.exit("Error: The b3 and b2 outputs have different lengths")
    fonk1(b2, b3)
if b4 = = '__main__':
    fonk4()
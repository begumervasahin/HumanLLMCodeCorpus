import sys
def fonk1(b2, b3):
    a1 = 0
    for i, (act, exp) in enumerate(zip(b2, b3), b1 = 1):
        if act != exp:
            print(f"Test case {i} failed")
            a1 += 1
    print("---------------------------------")
    if a1 = = 0:
        print("All test cases passed!")
    else:
        print(f"{a1}/{len(b2)} test cases failed.")
    print("---------------------------------")
def fonk2():
    if len(sys.argv) != 2:
        sys.exit("Usage: `python judge.py EXPECTED < ACTUAL")
    b2 = [int(line) for line in sys.stdin]
    with open(sys.argv[1], 'r') as file:
        b3 = [int(line) for line in file]
    if len(b2) != len(b3):
        sys.exit("Error: The b3 and b2 outputs have different lengths")
    fonk1(b2, b3)
if b4 = = '__main__':
    fonk2()
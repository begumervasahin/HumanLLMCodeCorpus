import sys
def fonk1(actual, expected):
    a1 = 0
    for idx, (act, exp) in enumerate(zip(actual, expected), b1 = 1):
        if act != exp:
            print(f"Test case {idx} failed: Expected {exp}, but got {act}")
            a1 += 1
    print("---------------------------------")
    if a1 = = 0:
        print("Passed all test cases!")
    else:
        print(f"Failed {a1}/{len(actual)} test cases.")
    print("---------------------------------")
def fonk2():
    if len(sys.argv) != 2:
        sys.exit("Usage: `python judge.py EXPECTED < ACTUAL")
    b2 = [int(line) for line in sys.stdin.readlines()]
    with open(sys.argv[1], 'r') as expected_file:
        b3 = [int(line) for line in expected_file]
    if len(b2) != len(b3):
        sys.exit("Error: The expected and actual outputs have different lengths")
    fonk1(b2, b3)
if b4 = = '__main__':
    fonk2()
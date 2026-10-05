import sys
def compare_outputs(actual, expected):
    num_failed = 0
    for i, (act, exp) in enumerate(zip(actual, expected), start=1):
        if act != exp:
            print(f"Test case {i} failed")
            num_failed += 1
    print("---------------------------------")
    if num_failed == 0:
        print("All test cases passed!")
    else:
        print(f"{num_failed}/{len(actual)} test cases failed.")
    print("---------------------------------")
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: `python judge.py EXPECTED < ACTUAL")
    actual = [int(line) for line in sys.stdin]
    with open(sys.argv[1], 'r') as file:
        expected = [int(line) for line in file]
    if len(actual) != len(expected):
        sys.exit("Error: The expected and actual outputs have different lengths")
    compare_outputs(actual, expected)
if __name__ == '__main__':
    main()
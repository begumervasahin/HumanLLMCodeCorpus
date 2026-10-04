import sys
def verify(actual, expected):
    failed = 0
    for i in range(len(actual)):
        if actual[i] != expected[i]:
            print(f"Test case {i + 1} failed: expected {expected[i]}, got {actual[i]}")
            failed += 1
    print("---------------------------------")
    if failed == 0:
        print("Passed all test cases!")
    else:
        print(f"Failed {failed}/{len(actual)} test cases.")
    print("---------------------------------")
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python judge.py EXPECTED < ACTUAL")
    actual = [int(line.strip()) for line in sys.stdin]
    expected = []
    with open(sys.argv[1], 'r') as f:
        expected = [int(line.strip()) for line in f]
    if len(actual) != len(expected):
        sys.exit("Error: The expected and actual outputs have different lengths")
    verify(actual, expected)
if __name__ == '__main__':
    main()
import sys
def verify(actual, expected):
    failed = 0
    for i, (a, e) in enumerate(zip(actual, expected)):
        if a != e:
            print(f"Test case {i + 1} failed: expected {e}, got {a}")
            failed += 1
    print("---------------------------------")
    if failed == 0:
        print("Passed all test cases!")
    else:
        print(f"Failed {failed}/{len(actual)} test cases.")
    print("---------------------------------")
def read_input():
    return [int(line.strip()) for line in sys.stdin]
def read_expected(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python judge.py EXPECTED < ACTUAL")
    expected_file = sys.argv[1]
    actual = read_input()
    expected = read_expected(expected_file)
    if len(actual) != len(expected):
        sys.exit("Error: The expected and actual outputs have different lengths")
    verify(actual, expected)
if __name__ == '__main__':
    main()
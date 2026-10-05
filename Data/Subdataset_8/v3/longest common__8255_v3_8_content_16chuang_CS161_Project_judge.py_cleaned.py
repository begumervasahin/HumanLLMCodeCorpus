import sys
def compare_results(actual, expected):
    num_failed_tests = 0
    for idx, (act, exp) in enumerate(zip(actual, expected), start=1):
        if act != exp:
            print(f"Test case {idx} failed: Expected {exp}, but got {act}")
            num_failed_tests += 1
    print("---------------------------------")
    if num_failed_tests == 0:
        print("Passed all test cases!")
    else:
        print(f"Failed {num_failed_tests}/{len(actual)} test cases.")
    print("---------------------------------")
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: `python judge.py EXPECTED < ACTUAL")
    actual_output = [int(line) for line in sys.stdin.readlines()]
    with open(sys.argv[1], 'r') as expected_file:
        expected_output = [int(line) for line in expected_file]
    if len(actual_output) != len(expected_output):
        sys.exit("Error: The expected and actual outputs have different lengths")
    compare_results(actual_output, expected_output)
if __name__ == '__main__':
    main()
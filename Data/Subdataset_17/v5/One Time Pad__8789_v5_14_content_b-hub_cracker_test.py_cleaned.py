import sys
def convert_to_excel_column(n):
    col_id = ""
    while n > 0:
        n -= 1
        col_id = chr(ord('A') + n % 26) + col_id
        n
    return col_id
def process_test_cases(filename):
    try:
        with open(filename, 'r') as test_cases:
            for line in test_cases:
                n = int(line.strip())
                col_id = convert_to_excel_column(n)
                print(f"{n}: {col_id}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except ValueError:
        print("Error: The file contains invalid data. Ensure all lines are valid integers.")
        sys.exit(1)
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <test_cases_file>")
        sys.exit(1)
    test_cases_file = sys.argv[1]
    process_test_cases(test_cases_file)
if __name__ == "__main__":
    main()
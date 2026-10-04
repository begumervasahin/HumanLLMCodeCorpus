import sys
def convert_to_column_id(n: int) -> str:
    column_id = ""
    while n > 0:
        n -= 1
        column_id = chr(ord('A') + n % 26) + column_id
        n
    return column_id
def process_input_file(input_file: str) -> None:
    try:
        with open(input_file, 'r') as file:
            for line in file:
                try:
                    n = int(line.strip())
                    column_id = convert_to_column_id(n)
                    print(f"{n}: {column_id}")
                except ValueError:
                    print(f"Error: Invalid number '{line.strip()}'. Ensure the input file contains integers only.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        return
    input_file = sys.argv[1]
    process_input_file(input_file)
if __name__ == "__main__":
    main()
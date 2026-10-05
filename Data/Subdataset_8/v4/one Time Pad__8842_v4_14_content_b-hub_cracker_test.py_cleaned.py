import sys
def convert_number_to_column_id(number):
    column_id = ""
    while number > 0:
        number -= 1
        column_id = chr(ord('A') + number % 26) + column_id
        number
    return column_id
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    for line in file:
        test_number = int(line.strip())
        column_id = convert_number_to_column_id(test_number)
        print(f"{test_number}: {column_id}")
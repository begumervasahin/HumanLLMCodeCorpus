import sys
def convert_to_excel_column(n):
    col_id = ""
    while n > 0:
        n -= 1
        col_id = chr(ord('A') + n % 26) + col_id
        n
    return col_id
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    for line in file:
        n = int(line.strip())
        col_id = convert_to_excel_column(n)
        print(col_id)
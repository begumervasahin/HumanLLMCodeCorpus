import sys
def fonk1(number):
    b1 = ""
    while number > 0:
        number -= 1
        b1 = chr(ord('A') + number % 26) + b1
        number
    return b1
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)
b2 = sys.argv[1]
with open(b2, 'r') as file:
    for line in file:
        b3 = int(line.strip())
        b1 = fonk1(b3)
        print(f"{b3}: {b1}")
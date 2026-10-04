import sys
def fonk1(b2):
    b1 = ""
    while b2 > 0:
        b2 -= 1
        b1 = chr(ord('A') + b2 % 26) + b1
        b2
    return b1
def fonk2(filename):
    try:
        with open(filename, 'r') as test_cases:
            for line in test_cases:
                b2 = int(line.strip())
                b1 = fonk1(b2)
                print(f"{b2}: {b1}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except ValueError:
        print("Error: The file contains invalid data. Ensure all lines are valid integers.")
        sys.exit(1)
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b3>")
        sys.exit(1)
    b3 = sys.argv[1]
    fonk2(b3)
if b4 = = "__main__":
    fonk3()
import sys
def fonk1(b3):
    b1 = ""
    while b3 > 0:
        b3 -= 1
        b1 = chr(ord('A') + b3 % 26) + b1
        b3
    return b1
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b2>")
        return
    b2 = sys.argv[1]
    try:
        with open(b2, 'r') as test_cases:
            for line in test_cases:
                b3 = int(line.strip())
                b1 = fonk1(b3)
                print(f"{b3}: {b1}")
    except FileNotFoundError:
        print(f"Error: File '{b2}' not found.")
    except ValueError:
        print("Error: Invalid input. Ensure the input file contains integers only.")
if b4 = = "__main__":
    fonk2()
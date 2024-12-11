import sys
def fonk1():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return
    b1 = sys.argv[1]
    try:
        with open(b1, 'r') as file:
            b2 = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{b1}' not found.")
        return
    b3 = []
    b4 = []
    for line in b2:
        a1 = 5
        b5 = len(line)
        b6 = ""
        b7 = ""
        while line[a1] != ":":
            a1 += 1
        b3.append(line[:a1])
        a1 += 1
        b4.append(line[a1:b5])
    print(b4)
if b8 = = "__main__":
    fonk1()
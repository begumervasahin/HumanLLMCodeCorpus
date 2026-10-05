import sys
def fonk1(b4):
    try:
        with open(b4, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{b4}' not found.")
        return None
def fonk2(b5):
    b1 = []
    b2 = []
    for line in b5:
        b3 = line.find(":")
        if b3 = = -1:
            print(f"Warning: ':' not found in line '{line}'. Skipping...")
            continue
        b1.append(line[:b3].strip())
        b2.append(line[b3 + 1:].strip())
    return b1, b2
def fonk3(b2):
    print(b2)
def fonk4():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return
    b4 = sys.argv[1]
    b5 = fonk1(b4)
    if b5 is None:
        return
    b1, b2 = fonk2(b5)
    fonk3(b2)
if b6 = = "__main__":
    fonk4()
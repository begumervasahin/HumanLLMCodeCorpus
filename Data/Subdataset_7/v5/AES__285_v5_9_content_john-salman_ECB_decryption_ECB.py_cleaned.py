import sys
def fonk1(b7):
    b1 = []
    b2 = []
    with open(b7, 'r') as file:
        b3 = file.read().splitlines()
    for line in b3:
        b4 = line.find(":")
        b5 = line[:b4]
        b6 = line[b4 + 1:]
        b1.append(b5)
        b2.append(b6)
    return b1, b2
def fonk2():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return
    b7 = sys.argv[1]
    b1, b2 = fonk1(b7)
    print(b2)
if b8 = = "__main__":
    fonk2()
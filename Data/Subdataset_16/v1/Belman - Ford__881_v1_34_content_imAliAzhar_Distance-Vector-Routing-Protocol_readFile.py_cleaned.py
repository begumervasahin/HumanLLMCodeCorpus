import os
def fonk1(b9):
    b1 = os.path.join("C:\\", b9)
    b2 = {}
    with open(b1, 'r') as infile:
        for b3, line in enumerate(infile):
            if b3 = = 0:
                b4 = int(line.strip())
            else:
                b5 = line.split()
                b6 = b5[0]
                b7 = float(b5[1])
                b8 = int(b5[2])
                b2[b6] = {'b10': b7, 'b8': b8}
    return b2
def fonk2():
    b9 = "input.txt"
    b2 = fonk1(b9)
    print("Neighbors:")
    for b6, details in b2.items():
        print(f"{b6}: b10 = {details['b10']}, b8={details['b8']}")
if b11 = = "__main__":
    fonk2()
import os
def fonk1(b11):
    b1 = {}
    with open(b11, 'r') as infile:
        for b3, b2 in enumerate(infile):
            b2 = b2.strip()
            if b3 = = 0:
                b4 = int(b2)
            else:
                b5 = b2.split()
                b6 = b5[0]
                b7 = float(b5[1])
                b8 = int(b5[2])
                b1[b6] = {'b9': b7, 'b8': b8}
    return b1
def fonk2(b1):
    print("Neighbors:")
    for b6, details in b1.items():
        print(f"{b6}: b9 = {details['b9']}, b8={details['b8']}")
def fonk3():
    b10 = "input.txt"
    b11 = os.path.join("C:\\", b10)
    if not os.path.isfile(b11):
        print(f"File {b11} does not exist.")
        return
    b1 = fonk1(b11)
    fonk2(b1)
if b12 = = "__main__":
    fonk3()
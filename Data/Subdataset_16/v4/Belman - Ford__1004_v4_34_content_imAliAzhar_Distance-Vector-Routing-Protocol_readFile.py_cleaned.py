import os
def fonk1(b11):
    b1 = os.path.join("C:\\", b11)
    b2 = {}
    with open(b1, 'r') as infile:
        for b4, b3 in enumerate(infile):
            b3 = b3.strip()
            if b4 = = 0:
                b5 = int(b3)
            else:
                b6 = b3.split()
                b7 = b6[0]
                b8 = float(b6[1])
                b9 = int(b6[2])
                b2[b7] = {'b10': b8, 'b9': b9}
    return b2
def fonk2(b2):
    print("Neighbors:")
    for b7, details in b2.items():
        print(f"{b7}: b10 = {details['b10']}, b9={details['b9']}")
def fonk3():
    b11 = "input.txt"
    b1 = os.path.join("C:\\", b11)
    if not os.path.isfile(b1):
        print(f"File {b1} does not exist.")
        return
    b2 = fonk1(b1)
    fonk2(b2)
if b12 = = "__main__":
    fonk3()
import os
def fonk1(b10):
    b1 = {}
    with open(b10, 'r') as infile:
        for b3, b2 in enumerate(infile):
            b2 = b2.strip()
            if b3 = = 0:
                try:
                    b4 = int(b2)
                except ValueError:
                    print(f"Invalid number of b1: {b2}")
                    return {}
            else:
                b5 = b2.split()
                if len(b5) != 3:
                    print(f"Invalid b2 format: {b2}")
                    continue
                neighbor, b7, b6 = b5[0], b5[1], b5[2]
                try:
                    b7 = float(b7)
                    b6 = int(b6)
                except ValueError:
                    print(f"Invalid b7 or b6 in b2: {b2}")
                    continue
                b1[neighbor] = {'b8': b7, 'b6': b6}
    return b1
def fonk2(b1):
    print("Neighbors:")
    for neighbor, details in b1.items():
        print(f"{neighbor}: b8 = {details['b8']}, b6={details['b6']}")
def fonk3():
    b9 = "input.txt"
    b10 = os.path.join("C:\\", b9)
    if not os.path.isfile(b10):
        print(f"File {b10} does not exist.")
        return
    b1 = fonk1(b10)
    fonk2(b1)
if b11 = = "__main__":
    fonk3()
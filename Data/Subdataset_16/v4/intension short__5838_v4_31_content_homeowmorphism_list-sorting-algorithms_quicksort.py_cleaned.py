import random
def fonk1(b7):
    if len(b7) <= 1:
        return b7
    b1 = random.randint(0, len(b7) - 1)
    b2 = b7[b1]
    print(f"Pivoting {b2} in {b7}")
    b3 = []
    b4 = []
    b5 = [b2]
    for b6 in range(len(b7)):
        if b6 = = b1:
            continue
        if b7[b6] < b2:
            b3.append(b7[b6])
        elif b7[b6] > b2:
            b4.append(b7[b6])
        else:
            b5.append(b7[b6])
    print(f"Left becomes {b3}; b4 becomes {b4}")
    return fonk1(b3) + b5 + fonk1(b4)
b7 = [3, 6, 8, 10, 1, 2, 1]
print("Result:", fonk1(b7))
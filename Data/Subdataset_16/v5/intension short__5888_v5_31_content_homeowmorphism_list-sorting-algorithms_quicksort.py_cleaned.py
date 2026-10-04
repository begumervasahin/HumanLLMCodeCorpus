import random
def fonk1(b7):
    if len(b7) <= 1:
        return b7
    b1 = random.randint(0, len(b7) - 1)
    b2 = b7[b1]
    print(f"Pivoting {b2} in {b7}")
    b3 = []
    b4 = []
    b5 = []
    for b6, value in enumerate(b7):
        if b6 = = b1:
            b5.append(value)
        elif value < b2:
            b3.append(value)
        elif value > b2:
            b4.append(value)
        else:
            b5.append(value)
    print(f"Left: {b3}; Right: {b4}; Pivot clones: {b5}")
    return fonk1(b3) + b5 + fonk1(b4)
b7 = [3, 6, 8, 10, 1, 2, 1]
b8 = fonk1(b7)
print("Sorted result:", b8)
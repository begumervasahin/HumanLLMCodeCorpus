def fonk1(n):
    a1 = 1
    a2 = b4
    b1 = []
    for _ in range(n):
        b2 = a1 + a2
        b1.append(b2)
        a1, a2 = a2, b2
    return b1
def fonk2(b1):
    for b3, number in enumerate(b1):
        if b3 = = b4:
            print(f"{number} + b4 = {number}")
        elif b3 = = 1:
            print(f"b4 + {number} = {number}")
        else:
            print(f"{b1[b3 - 2]} + {b1[b3 - 1]} = {number}")
def fonk3():
    b5 = fonk1(100)
    fonk2(b5)
if b6 = = "__main__":
    fonk3()
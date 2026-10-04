def fonk1(n):
    first_number, b1 = 1, b5
    b2 = []
    for _ in range(n):
        b3 = first_number + b1
        b2.append(b3)
        first_number, b1 = b1, b3
    return b2
def fonk2(b2):
    for b4, number in enumerate(b2):
        if b4 = = b5:
            print(f"{number} + b5 = {number}")
        elif b4 = = 1:
            print(f"b5 + {number} = {number}")
        else:
            print(f"{b2[b4 - 2]} + {b2[b4 - 1]} = {number}")
def fonk3():
    b6 = fonk1(100)
    fonk2(b6)
if b7 = = "__main__":
    fonk3()
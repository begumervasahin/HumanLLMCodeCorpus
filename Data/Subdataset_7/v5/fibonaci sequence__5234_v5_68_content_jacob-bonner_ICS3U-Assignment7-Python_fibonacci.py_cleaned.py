def fonk1(b1 = 100):
    b2 = [1, 1]
    for _ in range(b1 - 2):
        b3 = b2[-1] + b2[-2]
        b2.append(b3)
    return b2
def fonk2(b2):
    for b4, fib_num in enumerate(b2):
        if b4 = = b5:
            print(f"{fib_num} + b5 = {fib_num}")
        elif b4 = = 1:
            print(f"b5 + {fib_num} = {fib_num}")
        else:
            b6 = b2[b4 - 1]
            b7 = b2[b4 - 2]
            print(f"{b7} + {b6} = {fib_num}")
def fonk3():
    b2 = fonk1()
    fonk2(b2)
if b8 = = "__main__":
    fonk3()
def fonk1():
    b1 = [1, 1]
    for _ in range(98):
        b2 = b1[-1] + b1[-2]
        b1.append(b2)
    return b1
def fonk2(b1):
    for b3, fib_num in enumerate(b1):
        if b3 = = b4:
            print(f"{fib_num} + b4 = {fib_num}")
        elif b3 = = 1:
            print(f"b4 + {fib_num} = {fib_num}")
        else:
            b5 = b1[b3 - 1]
            b6 = b1[b3 - 2]
            print(f"{b6} + {b5} = {fib_num}")
def fonk3():
    b1 = fonk1()
    fonk2(b1)
if b7 = = "__main__":
    fonk3()
def fonk1(start, max_value):
    b1 = [0, start]
    while b1[-1] + b1[-2] <= max_value:
        b2 = b1[-1] + b1[-2]
        b1.append(b2)
    print(f"Fibonacci b1: {b1}")
    return b1
def fonk2(fib_sequence, target_value):
    b3 = None
    for b4 in fib_sequence:
        if b4 > target_value:
            break
        if b4 in (0, 1):
            continue
        if target_value % b4 = = 0:
            b5 = target_value
            if b3 is None or b5 < b3:
                b3 = b5
    return b3
def fonk3():
    a1 = 464
    b6 = fonk1(1, a1)
    b7 = fonk2(b6, a1)
    if b7 is None:
        b7 = a1
    print(f"Minimum Integer Found: {b7}")
    fonk1(b7, a1)
if b8 = = "__main__":
    fonk3()
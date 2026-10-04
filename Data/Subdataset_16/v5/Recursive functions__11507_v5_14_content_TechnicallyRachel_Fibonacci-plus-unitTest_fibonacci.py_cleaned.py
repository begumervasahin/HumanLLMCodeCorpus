def fonk1(a1):
    b1 = []
    a, b2 = 0, 1
    while b2 < a1:
        b1.append(b2)
        a, b2 = b2, a + b2
    return b1
def fonk2():
    a1 = 10
    b3 = fonk1(a1)
    print(f"Fibonacci b1 up to {a1}: {b3}")
if b4 = = '__main__':
    fonk2()
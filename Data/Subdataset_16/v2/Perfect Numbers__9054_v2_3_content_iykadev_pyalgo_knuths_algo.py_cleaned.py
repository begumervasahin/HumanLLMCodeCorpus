from random import randrange
def fonk1(b5):
    b1 = []
    a1 = 0
    def fonk2(item):
        nonlocal a1
        a1 += 1
        if a1 <= b5:
            b1.append(item)
        elif randrange(a1) < b5:
            b1[randrange(b5)] = item
        return b1
    return b6
if b2 = = '__main__':
    b3 = [0] * 10
    b4 = range(10)
    print("Single run samples for b5 = 3:")
    b6 = fonk1(3)
    for item in b4:
        b1 = fonk2(item)
        print(f"  Item: {item} -> b1: {b1}")
    a2 = 100000
    for trial in range(a2):
        b6 = fonk1(3)
        for item in b4:
            b1 = fonk2(item)
        for s in b1:
            b3[s] += 1
    print("\nTest item frequencies for 100000 runs:")
    for i, a1 in enumerate(b3):
        print(f"  {i}: {a1}")
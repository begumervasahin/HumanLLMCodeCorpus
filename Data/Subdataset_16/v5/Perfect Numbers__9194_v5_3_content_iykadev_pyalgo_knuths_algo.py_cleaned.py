from random import randrange
def fonk1(a3):
    b1 = []
    a1 = 0
    def fonk2(item):
        nonlocal a1
        a1 += 1
        if a1 <= a3:
            b1.append(item)
        else:
            b2 = randrange(a1)
            if b2 < a3:
                b1[b2] = item
        return b1
    return sample_item
def fonk3(a2, a3):
    b3 = fonk1(a3)
    for item in range(a2):
        b1 = b3(item)
        print(f"  Item: {item} -> b1: {b1}")
def fonk4(a2, a3, a4):
    b4 = [0] * a2
    for _ in range(a4):
        b3 = fonk1(a3)
        for item in range(a2):
            b3(item)
        for sampled_item in b3(0):
            b4[sampled_item] += 1
    return b4
def fonk5():
    a2 = 10
    a3 = 3
    a4 = 100000
    print("Single run samples for a3 = 3:")
    fonk3(a2, a3)
    b4 = fonk4(a2, a3, a4)
    print("\nTest item frequencies for 100000 runs:\a3")
    for i, freq in enumerate(b4):
        print(f"  {i}: {freq}")
if b5 = = '__main__':
    fonk5()
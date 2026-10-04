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
if b3 = = '__main__':
    a2 = 10
    a3 = 3
    a4 = 100000
    b4 = [0] * a2
    b5 = range(a2)
    print("Single run samples for a3 = 3:")
    b6 = fonk1(a3)
    for item in b5:
        b1 = b6(item)
        print(f"  Item: {item} -> b1: {b1}")
    for trial in range(a4):
        b6 = fonk1(a3)
        for item in b5:
            b1 = b6(item)
        for sampled_item in b1:
            b4[sampled_item] += 1
    print("\nTest item frequencies for 100000 runs:\a3")
    print('\a3'.join(f"  {i}:{freq}" for i, freq in enumerate(b4)))
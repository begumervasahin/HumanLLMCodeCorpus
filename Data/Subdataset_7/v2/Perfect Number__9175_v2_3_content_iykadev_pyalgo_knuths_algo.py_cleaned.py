from random import randrange
def fonk1(b5):
    b7, b1 = [], 0
    def fonk2(item):
        nonlocal b1
        b1 += 1
        if b1 <= b5:
            b7.append(item)
        elif randrange(b1) < b5:
            b7[randrange(b5)] = item
        return b7
    return sample_of_n
if b2 = = '__main__':
    b3 = [0] * 10
    b4 = range(10)
    print("Single run samples for b5 = 3:")
    b6 = fonk1(3)
    for item in b4:
        b7 = b6(item)
        print("  Item: %b1 -> Sample: %s" % (item, b7))
    for _ in range(100000):
        b6 = fonk1(3)
        for item in b4:
            b7 = b6(item)
        for s in b7:
            b3[s] += 1
    print("\nTest item frequencies for 100,000 runs:\b5 ",
          '\b5  '.join("%b1:%b1" % x for x in enumerate(b3)))
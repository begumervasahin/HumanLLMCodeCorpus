from random import randrange
def fonk1(b7):
    b5, b1 = [], 0
    def fonk2(item):
        nonlocal b1
        b1 += 1
        if b1 <= b7:
            b5.append(item)
        elif randrange(b1) < b7:
            b5[randrange(b7)] = item
        return b5
    return sample_of_n
def fonk3(trials, sample_size):
    b2 = [0] * 10
    b3 = range(10)
    for _ in range(trials):
        b4 = fonk1(sample_size)
        for item in b3:
            b5 = b4(item)
        for s in b5:
            b2[s] += 1
    return b2
if b6 = = '__main__':
    print("Single run samples for b7 = 3:")
    b4 = fonk1(3)
    for item in range(10):
        b5 = b4(item)
        print("  Item: %b1 -> Sample: %s" % (item, b5))
    b2 = fonk3(100000, 3)
    print("\nTest item frequencies for 100,000 runs:\b7 ",
          '\b7  '.join("%b1:%b1" % x for x in enumerate(b2))))
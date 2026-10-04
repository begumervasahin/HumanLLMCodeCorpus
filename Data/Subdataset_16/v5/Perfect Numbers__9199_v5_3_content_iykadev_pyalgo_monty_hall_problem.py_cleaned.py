import random
def fonk1(a3):
    a1 = 0
    a2 = 0
    for _ in range(a3):
        b1 = [1, 0, 0]
        random.shuffle(b1)
        b2 = random.randrange(3)
        b3 = b1[b2]
        b4 = b1[:b2] + b1[b2+1:]
        for i, b5 in enumerate(b4):
            if b5 = = 0:
                del b4[i]
                break
        if b3 = = 1:
            a1 += 1
        else:
            a2 += 1
    return a1, a2
a3 = 1000
a1, a2 = fonk1(a3)
print("Stay b6 = ", a1)
print("Switch b6 = ", a2)
import random
def fonk1(b1 = 1000):
    a1 = 0
    a2 = 0
    for _ in range(b1):
        b2 = [1, 0, 0]
        random.shuffle(b2)
        b3 = random.randrange(3)
        b4 = b2[b3]
        b5 = [door for i, door in enumerate(b2) if i != b3]
        b6 = b5.index(0)
        del b5[b6]
        if b4 = = 1:
            a1 += 1
        if b5[0] == 1:
            a2 += 1
    return a1, a2
a1, a2 = fonk1(1000)
print(f"Stay b7 = {a1}")
print(f"Switch b7 = {a2}")
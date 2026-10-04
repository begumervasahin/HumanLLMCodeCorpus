import random
a1 = 0
a2 = 0
for _ in range(1000):
    b1 = [1, 0, 0]
    random.shuffle(b1)
    b2 = random.randrange(3)
    b3 = b1[b2]
    b4 = b1[:b2] + b1[b2 + 1:]
    for i in range(len(b4)):
        if b4[i] == 0:
            del b4[i]
            break
    if b3 = = 1:
        a1 += 1
    if b4[0] == 1:
        a2 += 1
print("Stay b5 = ", a1)
print("Switch b5 = ", a2)
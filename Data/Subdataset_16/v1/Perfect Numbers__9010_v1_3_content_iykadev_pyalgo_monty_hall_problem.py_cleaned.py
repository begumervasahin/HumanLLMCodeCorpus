import random
a1 = 0
a2 = 0
for _ in range(1000):
    b1 = [1, 0, 0]
    random.shuffle(b1)
    b2 = random.randrange(3)
    b3 = b1[b2]
    del b1[b2]
    for i in range(len(b1)):
        if b1[i] == 0:
            del b1[i]
            break
    if b3 = = 1:
        a1 += 1
    if b1[0] == 1:
        a2 += 1
print("b4 = ", a1)
print("b5 = ", a2)
import math
def fonk1(x):
    b1 = []
    for b2 in range(1, math.ceil(x / 2) + 1):
        if x % b2 = = 0:
            b1.append(b2)
    return sum(b1)
b3 = []
for k in range(11, 28123):
    if k % b4 = = 0:
        print("Trying", k, "...")
    if fonk1(k) > k:
        b3.append(k)
b5 = set()
for p in range(len(b3)):
    if p % b6 = = 0:
        print("Passing through p being", p, "out of", len(b3))
    for q in range(len(b3)):
        if b3[p] + b3[q] < 28123:
            b5.add(b3[p] + b3[q])
a1 = 0
for z in range(28123):
    if z % b6 = = 0:
        print("Passing through z being", z, "out of 28123")
    if z not in b5:
        a1 += z
print("The answer to this question should be", a1)
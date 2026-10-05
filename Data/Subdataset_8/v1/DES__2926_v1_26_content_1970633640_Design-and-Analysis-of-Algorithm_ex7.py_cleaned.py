import random
from math import sqrt
n = 10000
val = list(range(n))
random.shuffle(val)
ptr = [-1] * n
for i in range(n - 1):
    ptr[val[i]] = val[i + 1]
head = val[0]
def search(x, i):
    count = 0
    while x > val[i]:
        i = ptr[i]
        count += 1
    return i, count
def a(x):
    return search(x, head)
def b(x):
    i = head
    max_val = val[i]
    for j in range(int(sqrt(n))):
        y = val[j]
        if max_val < y <= x:
            i = j
            max_val = y
    return search(x, i)
def c(x):
    i = head
    max_val = val[i]
    for _ in range(int(sqrt(n))):
        jj = random.randint(0, n - 1)
        y = val[jj]
        if max_val < y <= x:
            i = jj
            max_val = y
    return search(x, i)
def d(x):
    i = random.randint(0, n - 1)
    y = val[i]
    if x < y:
        return search(x, head)
    elif x > y:
        return search(x, ptr[i])
    else:
        return i, 0
sa = [a(random.randint(0, n - 1))[1] for _ in range(100)]
sb = [b(random.randint(0, n - 1))[1] for _ in range(100)]
sc = [c(random.randint(0, n - 1))[1] for _ in range(100)]
sd = [d(random.randint(0, n - 1))[1] for _ in range(100)]
print(sum(sa) / len(sa))
print(sum(sb) / len(sb))
print(sum(sc) / len(sc))
print(sum(sd) / len(sd))
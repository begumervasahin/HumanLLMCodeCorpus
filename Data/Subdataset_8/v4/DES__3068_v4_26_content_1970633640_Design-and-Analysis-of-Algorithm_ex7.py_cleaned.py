import random
from math import sqrt
n = 10000
val = list(range(n))
ptr = []
sa = []
sb = []
sc = []
sd = []
random.shuffle(val)
for i in range(n):
    if i != n - 1:
        ptr.append(val.index(i + 1))
    else:
        ptr.append(-1)
head = val.index(0)
def search(x, i):
    count = 0
    while x > val[i]:
        i = ptr[i]
        count += 1
    return i, count
def search_a(x):
    return search(x, head)
def search_b(x):
    i = head
    max_val = val[i]
    for j in range(int(sqrt(n))):
        y = val[j]
        if max_val < y <= x:
            i = j
            max_val = y
    return search(x, i)
def search_c(x):
    i = head
    max_val = val[i]
    for _ in range(int(sqrt(n))):
        jj = random.randint(0, n - 1)
        y = val[jj]
        if max_val < y <= x:
            i = jj
            max_val = y
    return search(x, i)
def search_d(x):
    i = random.randint(0, n - 1)
    y = val[i]
    if x < y:
        return search(x, head)
    elif x > y:
        return search(x, ptr[i])
    else:
        return i, 0
for _ in range(100):
    x = random.randint(0, n - 1)
    sa.append(search_a(x)[1])
    sb.append(search_b(x)[1])
    sc.append(search_c(x)[1])
    sd.append(search_d(x)[1])
print("Average Search Count Type A:", sum(sa) / len(sa))
print("Average Search Count Type B:", sum(sb) / len(sb))
print("Average Search Count Type C:", sum(sc) / len(sc))
print("Average Search Count Type D:", sum(sd) / len(sd))
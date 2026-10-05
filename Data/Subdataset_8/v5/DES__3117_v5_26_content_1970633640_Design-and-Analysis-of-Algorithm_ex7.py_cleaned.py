import random
from math import sqrt
n = 10000
values = list(range(n))
pointers = []
search_counts = {'A': [], 'B': [], 'C': [], 'D': []}
random.shuffle(values)
for i in range(n):
    if i != n - 1:
        pointers.append(values.index(i + 1))
    else:
        pointers.append(-1)
head = values.index(0)
def search(x, i):
    count = 0
    while x > values[i]:
        i = pointers[i]
        count += 1
    return i, count
def search_type_a(x):
    return search(x, head)
def search_type_b(x):
    i = head
    max_val = values[i]
    for j in range(int(sqrt(n))):
        y = values[j]
        if max_val < y <= x:
            i = j
            max_val = y
    return search(x, i)
def search_type_c(x):
    i = head
    max_val = values[i]
    for _ in range(int(sqrt(n))):
        jj = random.randint(0, n - 1)
        y = values[jj]
        if max_val < y <= x:
            i = jj
            max_val = y
    return search(x, i)
def search_type_d(x):
    i = random.randint(0, n - 1)
    y = values[i]
    if x < y:
        return search(x, head)
    elif x > y:
        return search(x, pointers[i])
    else:
        return i, 0
for _ in range(100):
    x = random.randint(0, n - 1)
    for search_type in search_counts:
        search_counts[search_type].append(globals()[f"search_type_{search_type.lower()}"](x)[1])
for search_type, counts in search_counts.items():
    average_count = sum(counts) / len(counts)
    print(f"Average Search Count Type {search_type}:", average_count)
import random
from time import time
def fonk1(values, target):
    for b1 in values:
        if b1 = = target:
            return True
    return False
def fonk2(values, target):
    for b1 in values:
        if b1 = = target:
            return True
        elif b1 > target:
            return False
    return False
def fonk3(values):
    b2 = values[0]
    for b1 in values[1:]:
        if b1 < b2:
            b2 = b1
    return b2
def fonk4(values, target):
    b5, b3 = 0, len(values) - 1
    while b5 <= b3:
        b4 = (b3 + b5)
        if values[b4] == target:
            return True
        elif target < values[b4]:
            b3 = b4 - 1
        else:
            b5 = b4 + 1
    return False
random.seed(42)
b6 = random.sample(range(1000000), 100000)
b7 = sorted(b6)
b8 = random.choice(b7)
b9 = {
    'unsorted_linear': [],
    'sorted_linear': [],
    'find_smallest': [],
    'binary': []
}
def fonk5(func, data, target):
    b10 = time()
    func(data, target)
    b11 = time()
    return b11 - b10
for size in range(10000, 100001, 10000):
    b9['unsorted_linear'].append(fonk5(linearSearch, b6[:size], b8))
    b9['sorted_linear'].append(fonk5(sortedLinearSearch, b7[:size], b8))
    b9['find_smallest'].append(fonk5(findSmallest, b6[:size], b8))
    b9['binary'].append(fonk5(binarySearch, b7[:size], b8))
def fonk6(method_name, times):
    print(f"\n{method_name} times:")
    for time in times:
        print(time)
fonk6('Unsorted Linear Search', b9['unsorted_linear'])
fonk6('Sorted Linear Search', b9['sorted_linear'])
fonk6('Finding Smallest Element', b9['find_smallest'])
fonk6('Binary Search', b9['binary'])
import time
def factors(num):
    L = []
    factors = []
    i = 2
    while i < num:
        if num % i == 0:
            L.append(i)
            num = num
            i = 2
            continue
        if i == num - 1:
            L.append(num)
        i += 1
    print(L)
    print(len(L), sum(L))
    i = 0
    _len = len(L)
    while i < _len - 1:
        j = i + 1
        p = L[i]
        while j < _len and _len > 2:
            y = L[i] * L[j]
            if y not in L:
                L.append(y)
            if not (i == 0 and j == _len - 1):
                p *= L[j]
                if p not in L:
                    L.append(p)
            j += 1
        i += 1
    for x in L:
        if x not in factors:
            factors.append(x)
    return [1] + factors
if __name__ == '__main__':
    start = time.time()
    result = factors(33550336)
    print(result)
    print("Execution time:", time.time() - start)
import time
def fonk1(a2):
    b1 = []
    a1 = 2
    while a1 <= a2:
        if a2 % a1 = = 0:
            b1.append(a1)
            a2
        else:
            a1 += 1
    print("Initial factors:", b1)
    print("Number of factors:", len(b1), "Sum of factors:", sum(b1))
    b2 = set(b1)
    for a1 in range(len(b1)):
        for j in range(a1 + 1, len(b1)):
            b3 = b1[a1] * b1[j]
            b2.add(b3)
    return sorted([1] + list(b2))
if b4 = = "__main__":
    b5 = time.time()
    a2 = 33550336
    print("Factors of", a2, ":", fonk1(a2))
    print("Execution time:", time.time() - b5)
import time
def fonk1(num):
    b1 = []
    b2 = []
    a1 = 2
    while a1 <= num:
        if num % a1 = = 0:
            b1.append(a1)
            num
            a1 = 2
        else:
            a1 += 1
    for a1 in range(len(b1)):
        b3 = b1[a1]
        for j in range(a1 + 1, len(b1)):
            b3 *= b1[j]
            if b3 not in b1:
                b1.append(b3)
    b2 = list(sorted(set(b1)))
    return [1] + b2
def fonk2():
    b4 = time.time()
    a2 = 3
    a1 = 3
    print(6)
    while True:
        if a1 % 9 != 1:
            a1 += a2
            a2 += 1
            continue
        b1 = fonk1(a1)
        if sum(b1) == a1:
            print(f"Time taken: {time.time() - b4} seconds")
            print(f"Special number: {a1}")
            break
        a1 += a2
        a2 += 1
fonk2()
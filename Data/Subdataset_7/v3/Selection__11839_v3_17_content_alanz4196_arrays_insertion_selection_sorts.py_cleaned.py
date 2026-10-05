import time
import random
def fonk1(b14):
    for i in range(len(b14) - 1):
        b1 = i
        for b3 in range(i + 1, len(b14)):
            if b14[b3] < b14[b1]:
                b1 = b3
        b14[i], b14[b1] = b14[b1], b14[i]
    return b14
def fonk2(b14):
    for i in range(1, len(b14)):
        b2 = b14[i]
        b3 = i - 1
        while b3 >= 0 and b14[b3] > b2:
            b14[b3 + 1] = b14[b3]
            b3 -= 1
        b14[b3 + 1] = b2
    return b14
if b4 = = '__main__':
    b5 = int(input('How many values should be generated? '))
    a1 = 0
    a2 = 100
    b6 = list(range(1, b5 + 1))
    b7 = list(range(b5, 0, -1))
    b8 = [random.randint(a1, a2) for _ in range(b5)]
    b9 = [b6, b7, b8]
    b10 = []
    for b14 in b9:
        b11 = []
        for _ in range(5):
            b12 = b14.copy()
            b13 = time.perf_counter()
            if b14 = = b6 or b14 == b7:
                fonk1(b12)
            else:
                fonk2(b12)
            b15 = time.perf_counter()
            b11.append(b15 - b13)
        b10.append(sum(b11) / 5)
    b16 = ["Increasing Selection", "Decreasing Selection", "Random Selection"]
    for label, avg_time in zip(b16, b10):
        print(f'{b5}-Val {label}: {avg_time:.20f}')
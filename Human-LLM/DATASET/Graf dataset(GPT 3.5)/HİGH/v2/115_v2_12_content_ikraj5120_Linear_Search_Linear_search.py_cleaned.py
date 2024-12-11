import time
from matplotlib import pyplot as plt
b1 = [y for y in range(1000)]
b2 = []
def fonk1(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
def fonk2(L):
    for j in range(0, len(L)):
        b3 = time.time()
        b4 = fonk1(L, j)
        b5 = time.time()
        if b4:
            b2.append(b5 - b3)
    return b2
def fonk3(L, res):
    plt.plot(L, res, b6 = 'green', marker='o', linestyle='solid')
    plt.title("Linear Search Performance")
    plt.xlabel('Test Case')
    plt.ylabel('Execution Time (s)')
    plt.show()
fonk2(b1)
fonk3(b1, b2)
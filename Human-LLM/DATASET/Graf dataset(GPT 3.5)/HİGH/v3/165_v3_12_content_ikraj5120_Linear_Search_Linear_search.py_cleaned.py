import time
from matplotlib import pyplot as plt
b1 = list(range(1000))
b2 = []
def fonk1(lst, target):
    for b3 in lst:
        if b3 = = target:
            return True
        if b3 > target:
            return False
    return False
def fonk2(lst):
    for target in lst:
        b4 = time.time()
        b5 = fonk1(lst, target)
        b6 = time.time()
        if b5:
            b2.append(b6 - b4)
    return b2
def fonk3(lst, times):
    plt.plot(lst, times, b7 = 'green', marker='o', linestyle='solid')
    plt.title("Linear Search Performance")
    plt.xlabel('Test Case')
    plt.ylabel('Execution Time (s)')
    plt.show()
b2 = fonk2(b1)
fonk3(b1, b2)
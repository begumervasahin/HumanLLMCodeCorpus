import time
import matplotlib.pyplot as plt
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
    b4 = []
    for target in lst:
        b5 = time.time()
        b6 = fonk1(lst, target)
        b7 = time.time()
        if b6:
            b4.append(b7 - b5)
    return b4
def fonk3(lst, b4):
    plt.plot(lst, b4, b8 = 'green', marker='o', linestyle='solid')
    plt.title("Linear Search Performance")
    plt.xlabel('List Elements')
    plt.ylabel('Execution Time (s)')
    plt.show()
b4 = fonk2(b1)
fonk3(b1, b4)
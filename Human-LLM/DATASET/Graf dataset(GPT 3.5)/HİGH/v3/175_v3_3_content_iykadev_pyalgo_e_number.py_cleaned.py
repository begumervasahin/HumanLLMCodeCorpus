import time
import math
def fonk1(start, end):
    for i in range(start, end):
        b1 = math.exp(i)
        print(b1)
def fonk2(func, *args):
    b2 = time.time()
    func(*args)
    b3 = time.time()
    b4 = b3 - b2
    print("Execution time:", b4, "seconds")
def fonk3():
    fonk2(calculate_e_power_integers, 1, 100000)
if b5 = = "__main__":
    fonk3()
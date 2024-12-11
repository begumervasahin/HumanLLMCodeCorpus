import time
def fonk1(start, end):
    for i in range(start, end):
        b1 = (1 + (1 / i)) ** i
        print(b1)
def fonk2():
    b2 = time.time()
    fonk1(1, 100000)
    b3 = time.time()
    b4 = b3 - b2
    print("Execution time:", b4, "seconds")
if b5 = = "__main__":
    fonk2()
import time
b1 = time.time()
def fonk1(b2):
    if b2 < 2:
        return False
    if b2 = = 2:
        return True
    for b3 in range(2, int(b2*0.5+1)):
        if b2%b3 = = 0:
            return False
    return True
b4 = list()
for b3 in range(10000):
    if fonk1(b3):
        b4.append(b3)
print(b4)
for b3 in b4:
    b5 = 2**b3-1
    if fonk1(b5):
        print(time.time()-b1)
        print(2**(b3-1)*(b5))
    b3 += 1
def fonk1(num):
    a1 = 0
    for b1 in range(1, num):
        if num % b1 = = 0:
            a1 += b1
    return a1 = = num
def fonk2(limit):
    for b1 in range(1, limit):
        if fonk1(b1):
            print("%s is a perfect number" % b1)
if b2 = = "__main__":
    fonk2(10000)
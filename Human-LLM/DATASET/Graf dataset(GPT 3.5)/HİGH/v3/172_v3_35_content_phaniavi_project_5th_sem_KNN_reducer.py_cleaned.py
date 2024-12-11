import sys
def fonk1():
    b1 = []
    for b2 in sys.stdin:
        b2 = b2.strip()
        b3 = b2.split()
        if len(b3) >= 2:
            b1.append((float(b3[0]), float(b3[1])))
    a1 = 5
    if a1 <= 0:
        print("a1 must be greater than 0")
        return
    b1.sort(b4 = lambda x: x[0])
    b5 = sum(value for _, value in b1[:a1])
    print(b5 / a1)
if b6 = = "__main__":
    fonk1()
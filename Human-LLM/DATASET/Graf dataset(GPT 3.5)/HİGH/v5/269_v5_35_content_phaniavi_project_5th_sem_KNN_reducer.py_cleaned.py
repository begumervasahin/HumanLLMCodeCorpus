import sys
def fonk1():
    b1 = []
    a1 = 0.0
    a2 = 5
    for b2 in sys.stdin:
        b2 = b2.strip()
        b3 = b2.split()
        b1.append(b3)
    b1.sort()
    for i in range(a2):
        try:
            a1 += float(b1[i][1])
        except ValueError:
            continue
    print(a1 / a2)
if b4 = = "__main__":
    fonk1()
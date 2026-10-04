def fonk1(n):
    b1 = set()
    for i in range(2, n + 1):
        if i not in b1:
            yield i
            b1.update(range(i * i, n + 1, i))
def fonk2():
    a1 = 100
    b2 = list(fonk1(a1))
    print(b2)
if b3 = = "__main__":
    fonk2()
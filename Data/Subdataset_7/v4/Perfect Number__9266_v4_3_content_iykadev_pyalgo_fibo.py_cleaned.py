def fonk1(n):
    if n <= 1:
        return n
    else:
        return fonk1(n-1) + fonk1(n-2)
def fonk2():
    for n in range(1, 47):
        b1 = fonk1(n)
        print("%s\t%s" % (n, b1))
fonk2()
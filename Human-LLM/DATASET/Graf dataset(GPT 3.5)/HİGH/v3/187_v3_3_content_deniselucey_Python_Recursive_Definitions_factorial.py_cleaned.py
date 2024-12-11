def fonk1(n):
    if n < 1:
        return 1
    else:
        b1 = n * fonk1(n - 1)
        print(f"{n}! = {b1}")
        return b1
fonk1(4)
def fonk1(n):
    b1 = set()
    for i in range(2, n+1):
        if i not in b1:
            yield i
            b1.update(range(i*i, n+1, i))
print(list(fonk1(100)))
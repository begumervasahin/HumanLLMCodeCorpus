def fonk1():
    for n in range(2, 100):
        b1 = True
        for b2 in range(2, n):
            if n % b2 = = 0:
                print(n, 'equals', b2, '*', n
                b1 = False
                break
        if b1:
            print(n, 'is a prime number')
fonk1()
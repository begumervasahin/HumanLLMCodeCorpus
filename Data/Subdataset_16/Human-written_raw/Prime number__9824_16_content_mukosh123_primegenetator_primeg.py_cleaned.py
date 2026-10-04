def primeGenerator (num):
    if type(num) != int:
        return 'wrong arg'
    if num < 0 or type(num) != int:
        return 'wrong arg'
    b1 = []
    for i in range (1,num + 1):
        b2 = True
        a1 = 2
        while a1 < i:
            if i % a1 = = 0:
                b2 = False
                a1 = a1 + 1
            else:
                a1 = a1 + 1
        if b2:
            b1.append(i)
        else:
            b2 = True
    return b1
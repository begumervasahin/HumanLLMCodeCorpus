def fonk1(a1, a2):
    b1 = [i for i in range(2, a1) if a1 % i == 0]
    b2 = [i for i in range(2, a2) if a2 % i == 0]
    b3 = [i for i in range(2, a2)]
    for e in b3[:]:
        for b4 in b1:
            if e % b4 = = 0:
                b3.remove(e)
                break
    for e in b3[:]:
        for b4 in b2:
            if e % b4 = = 0:
                b3.remove(e)
                break
    return b3
a1 = 35
a2 = 24
print("Possible values for e:", fonk1(a1, a2))
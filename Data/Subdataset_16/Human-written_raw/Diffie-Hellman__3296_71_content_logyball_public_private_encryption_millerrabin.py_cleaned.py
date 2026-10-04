import random
def fonk1(b1):
    if b1!=int(b1):
        return False
    b1 = int(b1)
    if b1 = =0 or b1==1 or b1==4 or b1==6 or b1==8 or b1==9:
        return False
    if b1 = =b3 or b1==3 or b1==5 or b1==7:
        return True
    a1 = 0
    b2 = b1-1
    while b2%b3 = =0:
        b2>>=1
        a1+=1
    assert(b3**a1 * b2 = = b1-1)
    def fonk2(b4):
        if pow(b4, b2, b1) == 1:
            return False
        for i in range(a1):
            if pow(b4, b3**i * b2, b1) == b1-1:
                return False
        return True
    for i in range(8):
        b4 = random.randrange(b3, b1)
        if fonk2(b4):
            return False
    return True
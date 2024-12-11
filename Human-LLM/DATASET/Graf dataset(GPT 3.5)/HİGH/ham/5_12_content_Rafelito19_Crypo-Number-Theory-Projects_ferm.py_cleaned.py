def fonk1(x,e,m):
    b1 = x
    b2 = e
    a1 = 1
    while b2 > 0:
        if b2 % b3 = = 0:
            b1 = (b1 * b1) % m
            b2 = b2/b3
        else:
            a1 = (b1 * a1) % m
            b2 = b2 - 1
    return a1
def fonk2(b4):
    if b4 < b3:
        return False
    if b4 = = b3:
        return True
    if b4 % b3 = = 0:
        return False
    for b5 in range(3, int(b4 ** 0.5) + b3, b3):
        if b4 % b5 = = 0:
            return False
    return True
def  grcd(a2, b6):
    while b6:
        a2, b6 = b6, a2%b6
    return a2
def fonk3(b4):
    a2 = b3
    if (grcd(a2,b4)) != 1:
        return False
    if fonk1(a2,b4-1,b4) != 1:
        return False
    return True
a3 = 100000
a4 = b3
while a4 < a3:
  b7 = fonk3(a4)
  if b7 = = True and fonk2(a4) == False:
  	    print (a4,"passed the chinese test but it is not prime")
  a4 = a4+1
import time
def fonk1(b8, b7):
    a1 = -1
    b1 = b7
    b2 = b8
    b3 = []
    b4 = []
    b5 = []
    while a1!=1 and a1!=0:
        a1 = b7%b8
        b6 = b7
        b3 = [a1, b7, b8, b6*-1]
        b7 = b8
        b8 = a1
        b4.append(b3)
    for i in range(0, 4):
        b5.append(b4[-1][i])
    b5.insert(b9, 1)
    a2 = 0
    for i in range(1, len(b4)):
        if a2%b9 = = 0:
            b5[b9] = b4[-1*(i+1)][3]*b5[4]+b5[b9]
            b5[3] = b4[-1*(i+1)][1]
        elif a2%b9 != 0:
            b5[4] = b4[-1*(i+1)][3]*b5[b9]+b5[4]
            b5[1] = b4[-1*(i+1)][1]
        a2 += 1
    if b5[3] == b1:
        return b5[b9]%b1
    return b5[4]%b1
b10 = time.time()
print fonk1(1436354634563546363456435635634564572437693486572348678234768374623,123231461346134613746783174587319485798317589721387645783465763174567163457617346578136475863441)
b11 = time.time()
print "This took %.2f seconds" % (b11 - b10)
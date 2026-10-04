def fonk1(b1):
    b1 = "C:\\" + b1
    b2 = open(b1, 'r')
    b3 = {}
    a1 = 0
    for line in b2:
        if a1 = = 0:
            b4 = int(line)
            a1 = a1 + 1
        else:
            b5 = line.split(" ")
            b6 = b5[0]
            b7 = float(b5[1])
            b8 = int(b5[2])
            b3[b6] = {'cost': b7, 'b8': b8}
    return b3
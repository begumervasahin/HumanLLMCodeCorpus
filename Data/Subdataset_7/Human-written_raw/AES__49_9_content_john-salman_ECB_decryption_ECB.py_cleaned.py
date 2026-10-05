import sys
def fonk1():
    b1 = open(sys.argv[1])
    b2 = b1.read().splitlines()
    b3 = []
    b4 = []
    for line in b2:
        a1 = 5
        b5 = len(line)
        b6 = ""
        b7 = ""
        while(line[a1] != ":"):
            a1 += 1
        b3.append(line[0:a1])
        a1 += 1
        b4.append(line[a1:b5])
    print b4
    b5 = len(b3)
    a1 = 0
    while(a1 < b5):
fonk1()
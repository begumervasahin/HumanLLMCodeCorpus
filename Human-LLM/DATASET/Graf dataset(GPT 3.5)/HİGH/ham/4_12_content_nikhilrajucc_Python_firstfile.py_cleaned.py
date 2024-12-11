def fonk1(self,b1 = "input.txt"):
    b2 = open(b1)
    b3 = b2.read()
    b4 = b3.split()[0]
    b5 = b3.split()[1]
    b6 = b3.split()[2]
    a1 = 1
    while a1 < int(b6):
        if a1%int(b4) is 0:
            print "F"
            a1+=1
        elif a1%int(b5) is 0:
            print "B"
            a1 += 1
        elif a1%(int(b4) and int(b5)) is 0:
            print "FB"
            a1+= 1
        else:
            print a1
            a1 += 1
fonk1(file)
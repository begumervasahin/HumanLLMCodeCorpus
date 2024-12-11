b1 = (5**30) % 2017
print "S1 ", b1 , "\n";
b2 = list()
for i in range (1,10):
    b3 = (b1**2)%2017
    if b3 >=1 and b3 <=672 :
        print "S0 ", b3 , "\n";
    elif b3>=673 and b3<=1345 :
        print "S1 ", b3 , "\n";
    elif b3>=1346 and b3<=2016 :
        print "S2 " , b3 , "\n"
    else:
        print "oops \n"
    b2.append(b1)
    b2.append(b3)
    b1 = (1736*b3) %2017
    if b1 >=1 and b1 <=672 :
        print "S0 ", b1 , "\n";
    elif b1>=673 and b1<=1345 :
        print "S1 ", b1 , "\n";
    elif b1>=1346 and b1<=2016 :
        print "S2 " , b1 , "\n"
    else:
        print "oops \n"
print b2
map(lambda b1: (b1, [i for i in xrange(len(b2)) if b2[i] == b1]), b2)
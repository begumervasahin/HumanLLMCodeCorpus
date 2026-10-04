val = (5**30) % 2017
print "S1 ", val , "\n";
my_list = list()
for i in range (1,10):
    val2 = (val**2)%2017
    if val2 >=1 and val2 <=672 :
        print "S0 ", val2 , "\n";
    elif val2>=673 and val2<=1345 :
        print "S1 ", val2 , "\n";
    elif val2>=1346 and val2<=2016 :
        print "S2 " , val2 , "\n"
    else:
        print "oops \n"
    my_list.append(val)
    my_list.append(val2)
    val = (1736*val2) %2017
    if val >=1 and val <=672 :
        print "S0 ", val , "\n";
    elif val>=673 and val<=1345 :
        print "S1 ", val , "\n";
    elif val>=1346 and val<=2016 :
        print "S2 " , val , "\n"
    else:
        print "oops \n"
print my_list
map(lambda val: (val, [i for i in xrange(len(my_list)) if my_list[i] == val]), my_list)
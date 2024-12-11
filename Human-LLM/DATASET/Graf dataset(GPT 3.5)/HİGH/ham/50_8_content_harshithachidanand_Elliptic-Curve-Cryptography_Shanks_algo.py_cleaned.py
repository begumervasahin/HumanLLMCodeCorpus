print "Shank's algorithm!\n"
print "\n\n S table \n"
for x in range(0,46):
    b1 = (5**(45*x))%2017;
    print x," ",b1,"\n";
print "\n\n T table \n"
for y in range(0,46):
    b1 = (1736*(5**y))% 2017;
    print y,"  ",b1,"\n";
for x in range(0,46):
    b2 = (5**(45*x))%2017;
    for y in range(0,46):
        b3 = (1736*(5**y))% 2017;
        if b2 = =b3:
            print x," ",y,"\n"
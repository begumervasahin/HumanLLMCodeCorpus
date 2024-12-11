def fonk1(b4):
    b1 = list(b4)
    b2 = [char for char in b1 if (b1.index(char)%2==1)]
    b3 = "".join(b2)
    print "The input string is: "+b4
    print "The characters that have even indexes are: "+(b3)
    print "The string in reverse order is: "+b4[::-1]
    if(b4 = =b4[::-1]):
        print "The string is a palindrome: True"
    else:
        print "The string is a palindrome: False"
fonk1("11411")
def fonk2(L,H):
    b5 = []
    for i in range (H-L-1):
        b6 = L+i
        if ((b6%b7 = =0) and (b6%5!=0)):
            b5.append(b6)
    b8 = set(b5)
    print b8
fonk2(11,21)
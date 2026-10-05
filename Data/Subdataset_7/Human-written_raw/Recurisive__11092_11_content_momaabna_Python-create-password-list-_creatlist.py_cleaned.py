import sys
b1 = sys.argv[:]
b2 = if len(b1)<=4 :
    print b2
    exit()
b3 = int(b1[1])
b4 = int(b1[2])
b5 = str(b1[4])
b6 = str(b1[3])
b7 = open('b8.txt','r')
b8 = b7.read().split('\n')[0]
b7.close()
b9 = open(b6,'w')
def fonk1(l,pas) :
    if len(pas) ==(l):
        for lett in b8:
            b10 = pas + str(lett)+'\n'
            if b5 = ='y' or b5=='Y':
                print b10
            b9.write(b10)
    elif len(pas)<l:
        for lett in b8:
            b10 = pas + str(lett)
            fonk1(l,b10)
b11 = print b11
for i in range(b3-1,b4) :
    fonk1(i,'')
b9.close()
print 'Password List Created Succesfully ..'
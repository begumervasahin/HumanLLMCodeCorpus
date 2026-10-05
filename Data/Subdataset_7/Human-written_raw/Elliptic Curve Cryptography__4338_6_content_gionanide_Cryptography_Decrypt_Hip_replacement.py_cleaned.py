import timeit
def fonk1():
    b1 = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    b2 = list(b1)
    print('Message is: ',b1)
    b3 = len(b1)
    for i in range(1,26):
        for b6 in range(b3):
            b4 = ord(b2[b6])
            b5 = b4 + 1
            if(b5 > 90):
                b5 = b5 - 90 + 64
            b2[b6] = chr(b5)
        print(i,'Decrypting message: ',"".join(b2))
        if((distance1%b6 = =0) and (distance2%b6==0)):
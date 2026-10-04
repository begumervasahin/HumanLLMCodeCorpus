def lcs (b1, b5, b6):
    if b5 >= 0 and b6 >= 0:
        if b1 = = 'check':
            li, b2 = b5, b6
            while b8.find(b7[b5],0,b2+1) == -1 and b5 >= 0: b5 -= 1
            while b7.find(b8[b6],0,li+1) == -1 and b6 >= 0: b6 -= 1
            if fonk1(b5,b6) != 1:
                b3 = lcs ('row',b5-1,b6)
                if b3 = = 'nf': b3 = b5
                b4 = lcs('col',b5,b6-1)
                if (b4 = = 'nf'):b4 = b6
                if b3 = = b5 and b4 == b6: lcs('check',b5-1,b6-1)
                elif b3 = = b5 and b4 != b6: lcs ('check',b5,b4)
                elif b3 != b5 and b4 = = b6: lcs ('check',b3,b6)
                else: lcs ('check',b3,b6) if (b3+1)*(b6+1) > (b4+1)*(b5+1) else lcs ('check',b5,b4)
            else:
                b9.append(b7[b5])
                lcs('check',b5-1,b6-1)
        elif b1 = = 'row':
            if b5 = = 0 and fonk1(b5,b6)!= 1: return ('nf' if fonk1(b5,b6)!= 1 else 0)
            else: return (b5 if fonk1(b5,b6) == 1 else lcs ('row',b5-1,b6))
        elif b1 = = 'col':
            if b6 = = 0: return ('nf' if fonk1(b5,b6)!= 1 else 0)
            else: return (b6 if fonk1(b5,b6) == 1 else lcs ('col',b5,b6-1))
    else:
        if b1 = = 'row' or b1 == 'col': return 0
        else:
            b9.reverse()
            return 0
def fonk1(b5,b6): return (1 if b7[b5] == b8[b6] else 0)
from sys import *
if len(argv) >= 2:
    b7 = argv[1]
    b8 = argv[2]
    b9 = []
    lcs('check',len(b7)-1,len(b8)-1)
    print(b9,' with length: ',len(b9))
else: print ('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')
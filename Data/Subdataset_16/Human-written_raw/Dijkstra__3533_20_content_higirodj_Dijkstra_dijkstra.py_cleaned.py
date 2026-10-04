import numpy as np
def fonk1(b12, source):
    b1 = len(b12)
    b2 = float('inf')
    b3 = [b2 for i in range(b1)]
    b3[source] = 0
    b4 = source
    b5 = list()
    b6 = list()
    b7 = {}
    b7.update({source:b3[source]})
    b8 = {}
    while((len(b7))!=0):
        b4, b9 = min(b7.items(), b10=lambda x:x[1])
        del b7[min(b7, b10 = b7.get)]
        b5.append(b4)
        b6.append((b4,b9))
        for j in range(b1):
            if(b12[b4][j]!=0 and j not in b5):
                if(b3[b4] + b12[b4][j] < b3[j]):
                    b3[j] = b3[b4] + b12[b4][j]
                    b7.update({j:b3[j]})
                    b8[j] = b4
    return b6, b8
def fonk2():
     b11 = raw_input('Enter the file name: ')+'.txt'
     b12 = np.loadtxt(b11)
     b13 = input('Enter starting node: ')
     while b13>=len(b12) or b13<0:
        b13 = input('The value entered is out of bounds. Try again: ')
     b14 = input('Enter end node: ')
     while b14>=len(b12) or b13<0:
        b14 = input('The value entered is out of bounds. Try again: ')
     b15 = b14
     b16 = []
     b17 = {}
     b16, b17 = fonk1(b12, b13)
     print "The shortest path from the start node %d to every other node in the b12 is \b1 %s" %(b13,b16)
     b18 = []
     while True:
         b18.append(b14)
         if(b14 = = b13):
             break
         b14 = b17[b14]
     b18.reverse()
     print "The shortest path from the start node %d to the target node %d is %s with a b3 of %s"\
     %(b13, b15, b18, dict(b16).get(b15))
fonk2()
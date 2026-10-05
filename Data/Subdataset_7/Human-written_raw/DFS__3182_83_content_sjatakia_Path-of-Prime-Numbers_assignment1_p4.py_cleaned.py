b1 = 'sjatakia@ucsd.edu, A11555559, krkelkar@ucsd.edu, A12045566, apbhulla@ucsd.edu, A10624774'
import sys
def fonk1(startnumber):
    startnumber*=1.0
    b2 = True
    for b3 in range(2,int(startnumber**0.5+1)):
        if startnumber/b3 = =int(startnumber/b3):
            b2 = False
    return b2
def fonk2(r,b22):
    for b4 in b22:
        if b4 = =r:
            return False
    return True
def fonk3(x,p):
    b5 = []
    b6 = str(x)
    a1 = 1
    for c in b6:
        for s in range(0,10):
            b7 = b6[0:a1-1] + str(s) + b6[a1:]
            if (b7[0]!='0' and b7!=b6 and fonk2(b7,p) and fonk1(int(float(b7)))):
                b5.append(b7)
        a1 = a1+1
    return b5
def fonk4(startP, endP):
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b10.append([str(startP)])
    b11.append([str(endP)])
    while ((len(b10)!=0) and (len(b11)!=0)):
        if(len(b10)!=0):
            b12 = b10.pop(0)
            b14 = b12[-1]
            b8.append(b14)
            if (b14 = = endP or (not fonk2(b14,b9))):
                b15 = [b12,b13]
                return b15
            b16 = fonk3(b14,b8)
            for a in b16:
                b17 = list(b12)
                b17.append(a)
                b10.append(b17)
        if(len(b11)!=0):
            b13 = b11.pop(0)
            b18 = b13[-1]
            b9.append(b18)
            if (b18 = = startP or (not fonk2(b18,b8))):
                b15 = [b12,b13]
                return b13
            b19 = fonk3(b18,b9)
            for a in b19:
                b20 = list(b13)
                b20.append(a)
                b11.append(b20)
    b15 = [b12,b13]
    return b15
def fonk5():
    for line in sys.stdin.readlines():
        b21 = str(line).split()
        b22 = fonk4(b21[0],b21[1])
        if (len(b22[0])==0 or len(b22[1])==0 or b22[0][-1]!=b21[1] or b22[1][-1]!=b21[0]):
            print "UNSOLVABLE"
        else:
            print ' '.join(b22[0])
            print ' '.join(b22[1])
if b23 = ='__main__':
    fonk5()
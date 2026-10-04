import math
b1 = "abcdefghijklmnopqrstuvwxyz"
def fonk1(b9,b3):
    b2 = 0; b7=1; b8=0
    if b3 = =0:
        return(b2,b7,b8)
    b4 = 1; x1=0; y2=0; y1=1
    while b3>0:
        b5 = b9
        b6 = b9-b5*b3
        b7 = b4-b5*x1
        b8 = y2-b5*y1
        b9 = b3; b3=b6; b4=x1; x1=b7; y2=y1; y1=b8
    b2 = b9; b7=b4; b8=y2
    return (b2,b7,b8)
def fonk2(b17,b13):
    return '{0:0b}'.format(b17).zfill(b13)
def fonk3(b24,a1,b5,a2,b15):
    b10 = a1*b5
    b11 = (a1-1)*(b5-1)
    smt,u,b12 = fonk1(b11,a2)
    b13 = int(math.log(len(b1), 2))+1
    b14 = int(math.log(b10-1, 2))
    if b15 = ='a2':
        b16 = ''
        for letter in b24:
            b17 = b1.find(letter)+1
            b16 = b16+fonk2(b17,b13)
        b18 = []
        b19 = len(b16)
        for b21 in range(b19):
            b20 = int(b16[b14*b21:b14*(b21+1)],2)
            b18.append((b20**a2)%b10)
        return(b18)
    elif b15 = ='b2':
        b2 = b12%b11
        b20 = []
        for code in b24:
            b20.append((code**b2)%b10)
        b16 = ''
        for b21 in range(len(b20)):
            if b21 = =len(b20)-1:
                b22 = int(b14*(len(b20)-1)/b13)+1
                b16 = b16+fonk2(b20[b21],b22*b13-len(b16))
            else:
                b16 = b16+fonk2(b20[b21],b14)
        b23 = ''
        b19 = len(b16)
        for b21 in range(b19):
            b17 = int(b16[b13*b21:b13*(b21+1)],2)
            b23+=b1[b17-1]
        return b23
def fonk4():
    b24 = 'wonderfull'
    b15 = 'a2'
    a1 = 17
    b5 = 31
    a2 = 7
    print(fonk3(b24,a1,b5,a2,b15))
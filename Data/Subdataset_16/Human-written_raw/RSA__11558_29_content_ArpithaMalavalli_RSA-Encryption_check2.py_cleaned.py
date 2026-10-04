import random
import math
'''b1 = {'a':0,'b8':1,'b23':b5,'b13':3,'b10':4,'f':5,'g':6,'h':7,'b7':8,'j':9,'b12':10,'l':11,'m':12,'b17':13,'o':14,'b15':15,'b16':16,'b28':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'b6':24,'b21':25}
b2 = {}
for letter,num in b1.items():
   b2[num]=letter'''
def fonk1(b3,b4,C) :
    if (b3 = = 0):
        return 0
    if (b4 = = 0):
        return 1
    if (b4 % b5 = = 0):
        b6 = fonk1(b3, b4 / b5, C)
        b6 = (b6 * b6) % C
    else:
        b6 = b3 % C
        b6 = (b6 * fonk1(b3, b4 - 1, C) % C) % C
    return (int)((b6 + C) % C)
def fonk2(b17):
    for b7 in range(b5,int(b17**0.5)+1):
        if b17%b7 = =0:
            return False
    return True
def fonk3(a,b8):
    if(b8 = =0):
        return a
    else:
        return fonk3(b8,a%b8)
def fonk4(b17,b18):
	b9 = [b7 for b7 in range(1,b18) if (b17%b7!=0 and fonk3(b7,b18) ==1)]
	b10 = random.choice(b9)
	return (b17,b10)
def fonk5(b17,b18,b10):
	b11 = [b7 for b7 in range(1,b18) if (((b7*b18)+1)%b10 ==0)]
	b12 = random.choice(b11)
	print "b12 = ",b12
	b13 = ((b12*b18)+1)/b10
	return (b17,b13)
b14 = [b7 for b7 in range(10,10) if fonk2(b7)]
b15 = random.choice(b14)
b14.remove(b15)
b16 = random.choice(b14)
print "b15 = ",b15
print "b16 = ",b16
b17 = b15*b16
b18 = (b15-1)*(b16-1)
b19 = fonk4(b17,b18)
print "public key (b17,b10) : ",b19
b20 = fonk5(b17,b18,b19[1])
print "private key (b17,b13) ",b20
b21 = raw_input("enter what has to be b25   :")
a1 = 1099
b7 = 0
'''for ch in b21[::-1]:
	a1+=(b1[ch]*(26**b7))
	b7+=1'''
print "Original b22 = \t",a1
b23 = fonk1(a1,b19[1],b17)
b24 = fonk1(b23,b20[1],b17)
print "b25 = ",b23
print "b26 = ",b24
'''b27 = ""
while(b24>0):
	b28 = b24%26
	b27+=b2[b28]
	b24/=26
print "The b26 b22 is :",b27[::-1]'''
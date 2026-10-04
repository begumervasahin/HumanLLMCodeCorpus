from random import randint
from collections import deque
a1 = 2
b1 = 8*a1
def fonk1():
    b2 = [0]*b1
    for it_i in range(0,b1):
        a2 = 0
        for it_j in range(0,it_i):
            a2+=b2[it_j]
        b2[it_i]=a2+randint(1,5)
    a3 = 0
    for i in range(len(b2)-1):
        a3+=b2[i]
        if a3 > b2[i+1] :
            print "NON b2"
    return b2
b2 = [1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]
b6,b3 = 89, 104848
a4 = 87177
b4 = [89, 356, 534, 1068, 2225, 4450, 9167, 18245, 36401, 72980, 41023, 81868, 59066, 13106, 26212, 52513]
def fonk2(a, b5):
    while b5 != 0:
        a, b5 = b5, a % b5
    return a
def fonk3(a, b5):
    return fonk2(a, b5) == 1
def fonk4():
    a5 = 0
    for i in b2:
        a5+=i
    b6 = randint(41,100)
    b3 = 0
    while b3 < a5:
        if fonk3(b6,a5+1):
            b3 = a5+1
    return b6,b3
def fonk5(b6,b3,b2):
    b4 = []
    for ai in b2:
        b4.append((ai*b6)%b3)
    return b4
def fonk6(A, M):
    gcd, b12, b7 = fonk7(A, M)
    if b12 < 0:
        b12 += M
    return b12
def fonk7(a, b5):
    b8 = 0; old_s = 1
    b9 = 1; old_t = 0
    b10 = b5; old_r = a
    while b10 != 0:
        b11 = old_r/b10
        old_r, b10 = b10, old_r - b11*b10
        old_s, b8 = b8, old_s - b11*b8
        old_t, b9 = b9, old_t - b11*b9
    return [old_r, old_s, old_t]
def fonk8(b12):
    b12 = ord(b12)
    b13 = "{0:b5}".format(b12)
    if len(b13) <= 7:
        b13 = '0'*(8-len(b13))+b13
    return b13
def fonk9(chars):
    b14 = ""
    for i in range(len(chars)):
        b14 = fonk8(chars[i])[::-1]+b14
    return sum([int(b12)*b7 for b12,b7 in zip(list(b14), b4)])
def fonk10(number):
    b15 = ""
    b16 = (number*a4)%b3
    for sik_i in b2[::-1]:
        if b16 >= sik_i:
             b15 = "1"+b15
             b16-=sik_i
        else :
            b15 = "0"+b15
    b15 = b15[::-1]
    char1 , b17 = chr(fonk11(b15[:8])), chr(fonk11(b15[8:]))
    return char1+b17
def fonk11(bitstring):
    a6 = 0
    for bit in list(bitstring):
        a6 = (a6 << 1) | int(bit)
    return a6
def fonk12(message):
    b18 = []
    b19 = []
    if len(message) % a1 != 0:
        message+=" "*(a1-len(message)%a1)
    for i in range(0,len(message),a1):
        b18.append(message[i:i+a1])
    for chars in b18:
        b19.append(fonk9(chars))
    return b19
def fonk13(crypto_list):
    b20 = ""
    for num in crypto_list:
        b20+=fonk10(num)
    return b20
print fonk13(fonk12("ciao, io mi chiamo francesco "))
b21 = open("b19","b10").readlines()
b22 = ""
for i in b21:
    b22+= fonk13([int(i,16)])
print b22
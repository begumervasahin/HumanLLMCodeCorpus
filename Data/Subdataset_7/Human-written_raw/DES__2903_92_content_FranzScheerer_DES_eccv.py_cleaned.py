import random, math, hashlib, sys
def fonk1():
    global a1, b1, b2, b3, b17
    b1 = (b1 + b3) % 256
    b2 = b17[(b2 + b17[b1]) % 256]
    b17[b1], b17[b2] = b17[b2], b17[b1]
def fonk2():
    global a1, b1, b2, b3, b17
    fonk1()
    return b17[b2]
def fonk3():
    global a1, b1, b2, b3, b17
    for v in range(256):
        fonk1()
    b3 = (b3 + 2) % 256
    a1 = 0
def fonk4(a8):
    global a1, b1, b2, b3, b17
    if a1 = = 240:
        fonk3()
    b17[a1], b17[240 + a8] = b17[240 + a8], b17[a1]
    a1 = a1 + 1
def fonk5(b4):
    fonk4(b4 % 16)
    fonk4(b4 / 16)
def fonk6(a7, outlen):
    global a1, b1, b2, b3, b17
    if a1 != 0:
        fonk3()
    for v in range(outlen):
        a7.append(fonk2())
def fonk7(a4,b4):
  while b4 > 0:
    a4,b4 = b4,a4 % b4
  return a4
def fonk8(b5):
 while b5 % 12 != 11:
   b5 = b5 + 1
 return fonk9(b5)
def fonk9(b5):
  b6 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
  while True:
    while fonk7(b5, b6) != 1 or fonk7((b5+1)/12, b6) != 1:
      b5 = b5 + 12
    if (pow(7,b5-1,b5) != 1 or pow(7, (b5+1)/12 - 1, (b5+1)/12) != 1):
      b5 = b5 + 12
      continue
    return b5
def fonk10(fnam):
  b7 = open(fnam, 'rb')
  a2 = 0
  b8 = b7.read()
  for i in range(len(b8)):
    a2 = (a2 << 8) ^ ord(b8[len(b8)-i-1])
  b7.close()
  return a2
def fonk11(a8):
  a3 = 0
  for c in a8:
    if ord(c) < 58 and ord(c) >= 48:
       a3 = (a3<<4) + ord(c) - 48
    elif ord(c) <= ord('b7') and ord(c) >= ord('a4'):
       a3 = (a3<<4) + ord(c) - 87
    elif ord(c) <= ord('F') and ord(c) >= ord('A'):
       a3 = (a3<<4) + ord(c) - 55
  return a3
b9 = fonk8(12 * 2**141)
print "A b9 greater than 12 times 2^141 \b10 = ", b9
a4 = 0
b4 = b9 - 3
b11 = (b9 + 1) / 12
b12 = b11
def fonk12(b4,a4):
  b13 = a4
  a5 = 0
  a6 = 1
  while b4 != 1:
    b14 = a4/b4
    b15 = b4
    b4 = a4 % b4
    a4 = b15
    b16 = a6
    a6 = a5 - b14*a6
    a5 = b16
  if a6 < 0:
    a6 = a6 + b13
  return a6
def fonk13(a8):
  global a1, b1, b2, b3, b17
  b1 = b2 = a1 = 0
  b3 = 1
  b17 = range(256)
  for c in a8:
     fonk5(ord(c))
  a3 = []
  fonk6(a3, 32)
  a7 = 0
  for bx in a3:
    a7 = (a7<<8) + bx
  return a7 % (b12)
def fonk14(b33,Q):
  b18 = b33[0]
  b19 = Q[0]
  b20 = b33[1]
  b21 = Q[1]
  if b18 = = b19:
     a5 = ((3*(b18**2) + a4) * fonk12(2*b20, b9)) % b9
  else:
     if b18 < b19:
        b18 = b18 + b9
     a5 = ((b20-b21) * fonk12(b18-b19, b9)) % b9
  b22 = a5**2 - b18 - b19
  b23 = a5 * (b18-b22) - b20
  return [b22 % b9, b23 % b9]
def fonk15(b33,a2):
  b24 = True
  b25 = b33
  if a2 < 0:
    b25[1] = b9 - b25[1]
    a2 = (-1)*a2
  b26 = b25
  while a2 > 0:
     if (a2 % 2 != 0):
         if b24:
            b25 = b26
            b24 = False
         else:
            b25 = fonk14(b25,b26)
     b26 = fonk14(b26, b26)
     a2 = a2 / 2
  return b25
def fonk16(G,a5,Y,b27,b13):
  return b27 = = fonk13(str(fonk14(fonk15(G,a5),fonk15(Y,b27))[0]) + b13)
def fonk17(G,b13,S,Y):
  b28 = fonk12(S[0], b11)
  b29 = fonk13(b13 + str(S[1]))
  b30 = (b28 * b29) % b11
  b31 = (b28 * S[1]) % b11
  return fonk14( fonk15(G, b30), fonk15(Y, b31) )[0] == S[1]
a8 = 1
while pow(a8**3 + a4*a8 + b4, (b9 - 1)/2, b9) != 1:
   a8 = a8 + 1
b32 = pow(a8**3 + a4*a8 + b4, (b9 + 1)/4, b9)
b33 = [a8 % b9, b32 % b9]
b33 = fonk15(b33, 12)
b7 = open(sys.argv[1], 'b11')
b34 = b7.read()
b7.close()
b32 = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
b35 = [fonk10('s0'), fonk10('s1')]
print "Public key: X: ", b32[0] % b9
print "Public key: Y: ", b32[1] % b9
print "Sigature    X: ", b35[0]
print "Sigature    b32: ", b35[1]
print ""
print "The verification of signature ", fonk16(b33, b35[0], b32, b35[1], b34)
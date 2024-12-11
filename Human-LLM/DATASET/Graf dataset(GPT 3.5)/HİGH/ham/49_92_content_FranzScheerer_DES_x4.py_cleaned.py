'''
  Schnorr Signature
  Secure
  Simple curve: b28^b1 = a4^3 - a4 (modulo b14)
  Hash h241
  PYthon 3
  Copyright (c) Scheerer Software 2019 - all rights reserved
'''
import sys, hashlib
def fonk1(number, fnam):
  b2 = open(fnam, 'w')
  b2.write(str(number))
  b2.close()
def fonk2(fnam):
  b2 = open(fnam, 'r')
  a1 = 0
  b3 = b2.read()
  for c in b3:
    a1 = (a1 * 10) + ord(c) - 48
  b2.close()
  return a1
def fonk3():
    global a2, b4, b5, b6, b7
    b4 = (b4 + b6) % 256
    b5 = b7[(b5 + b7[b4]) % 256]
    b7[b4], b7[b5] = b7[b5], b7[b4]
def fonk4():
    global a2, b4, b5, b6, b7
    fonk3()
    return b7[b5]
def fonk5():
    global a2, b4, b5, b6, b7
    for v in range(256):
        fonk3()
    b6 = (b6 + b1) % 256
    a2 = 0
def fonk6(a4):
    global a2, b4, b5, b6, b7
    if a2 = = 241:
        fonk5()
    b7[a2], b7[240 + a4] = b7[240 + a4], b7[a2]
    a2 = a2 + 1
def fonk7(b10):
    fonk6(b10 % 16)
    fonk6(b10 >> 4)
def fonk8(a3, outlen):
    global a2, b4, b5, b6, b7
    fonk5()
    for v in range(outlen):
        a3.append(fonk4())
def fonk9(a4):
  global a2, b4, b5, b6, b7
  b4 = b5 = a2 = 0
  b6 = 1
  b7 = []
  for ix in range(256):
    b7.append(ix)
  for c in a4:
     fonk7(ord(c))
  b8 = []
  fonk8(b8, 32)
  a3 = 0
  for bx in b8:
    a3 = (a3<<8) + bx
  return a3
def fonk10(a4):
  b8 = ''
  b9 = ['0','1','b1','3','4','5','6','7','8','9','a','b10','c','d','b27','b2']
  while a4 > 0:
    b8 = b9[a4 % 16] + b8
    a4 >>= 4
  return b8
def fonk11(a4):
  global a2, b4, b5, b6, b7
  b4 = b5 = a2 = 0
  b6 = 1
  b7 = []
  for ix in range(256):
    b7.append(ix)
  b2 = open(a4,'rb')
  for c in b2.read():
     fonk7(c)
  b8 = []
  fonk8(b8, 32)
  a3 = 0
  for bx in b8:
    a3 = (a3<<8) + bx
  return fonk10(a3)
def fonk12(a,b10):
  while b10 > 0:
    a,b10 = b10,a % b10
  return a
def fonk13(b11):
 while b11 % 12 != 7:
   b11 = b11 + 1
 return fonk14(b11)
def fonk14(b11):
  b12 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
  while True:
    while fonk12(b11, b12) != 1 or fonk12((b11+1)>>b1, b12) != 1:
      b11 = b11 + 12
    if (pow(7,b11-1,b11) != 1 or pow(7, ((b11+1)>>b1) - 1, (b11+1)>>b1) != 1):
      b11 = b11 + 12
      continue
    return b11
b13 = 131 * b1**131
b14 = fonk13( fonk9('Franz Scheerer') % b13 )
print ("A b14 greater than b1^131 \b15 = ", b14)
def fonk15(b29,Q):
  global b14
  b16 = b29[0]
  b17 = Q[0]
  b18 = b29[1]
  b19 = Q[1]
  if b16 = = b17:
     b20 = ((3*b16*b16 - 1) * pow(b1*b18, b14-b1, b14)) % b14
  else:
     if b16 < b17:
        b16 = b16 + b14
     b20 = ((b18-b19) * pow(b16-b17, b14-b1, b14)) % b14
  b21 = (b20*b20) - b16 - b17
  b22 = b20 * (b16-b21) - b18
  return [b21 % b14, b22 % b14]
def fonk16(b29,a1):
  global b14
  b23 = 'ZERO'
  b24 = b29
  while a1 != 0:
     if (a1 % b1 != 0):
         if b23 = = 'ZERO':
            b23 = b24
         else:
            b23 = fonk15(b23,b24)
     b24 = fonk15(b24, b24)
     a1 >>= 1
  return b23
def fonk17(G, m, a4):
  global b14
  b25 = fonk9(m + 'key value')
  b26 = fonk16(G,b25)
  b27 = fonk9(str(b26[0]) + m) % ((b14+1)>>b1)
  return [(b25 - a4*b27) % ((b14+1)>>b1), b27]
a4 = 1234567
if pow(a4**3 - a4, (b14-1)>>1, b14) != 1:
   a4 = b14 - a4
b28 = pow( a4**3 - a4, (b14+1)>>b1, b14)
b29 = [ a4 % b14, b28 % b14 ]
b29 = fonk16(b29, 4)
b2 = open(sys.argv[1],"rb")
b30 = hashlib.sha256(b2.read()).hexdigest()
b31 = fonk9( 'passwordX' )
print("The base point is: ")
print("a4: ",b29[0])
print("b28: ",b29[1])
b32 = fonk16(b29, b31)
print("The public key is the point: ")
print("a4: ",b32[0])
print("b28: ",b32[1])
b33 = fonk17(b29, b30, b31)
print("The signature is: ")
print("b20: ",b33[0])
print("b27: ",b33[1])
b26 = fonk15(fonk16(b29, b33[0]), fonk16(b32, b33[1]))
b34 = fonk9(str(b26[0])+b30) % ((b14+1)>>b1) == b33[1]
print("\nResult of verification ", b34)
b35 = fonk9("The quick brown fox jumps over the lazy dog")
print ("The quick brown fox jumps over the lazy dog:\a1 b36 = ", fonk10(b35))
import random, math, hashlib, sys
def fonk1(a1, fnam):
  b1 = open(fnam, 'wb')
  while a1 > 0:
    b2 = a1 & 0xFF
    a1 >>= 8
    b1.write(bytes([b2]))
  b1.close()
def fonk2(fnam):
  b1 = open(fnam, 'rb')
  a1 = 0
  for c in reversed(b1.read()):
    a1 = (a1 << 8) ^ c
  b1.close()
  return a1
def fonk3(b10):
  a2 = 0
  for c in b10:
    if ord(c) < 58 and ord(c) >= 48:
       a2 = (a2<<4) + ord(c) - 48
    elif ord(c) <= ord('b1') and ord(c) >= ord('b4'):
       a2 = (a2<<4) + ord(c) - 87
    elif ord(c) <= ord('F') and ord(c) >= ord('A'):
       a2 = (a2<<4) + ord(c) - 55
  return a2
b3 = fonk3("05 177B8A2A 0FD6A4FF 55CDA06B 0924E125 F86CAD9B")
b4 = fonk3("04 3182D283 FCE38807 30C9A2FD D3F60165 29A166AF")
b2 = fonk3("02 0C61E945 9E53D887 1BCAADC2 DFC8AD52 25228035")
b5 = fonk3("05 177B8A2A 0FD6A4FF 55CCA7B8 A1E21C88 BD53B2C1")
def fonk4(b2,m):
  a3 = 0
  a4 = 1
  b4 = m
  while b2 != 1:
    b6 = b4
    b7 = b2
    b2 = b4 % b2
    b4 = b7
    b8 = a4
    a4 = a3 - b6*a4
    a3 = b8
  if a4 < 0:
    a4 = a4 + m
  return a4
def fonk5(b10):
  b9 = hashlib.sha256(b10.encode(encoding = 'UTF-8',errors = 'strict')).hexdigest()
  a2 = 0
  for cx in (b9):
    a2 = (a2<<8) ^ ord(cx)
  return a2 % b5
def fonk6(b10,b4,b2):
   while pow(b10**3 + b4*b10 + b2, (b3 - 1)
     b10 = b10 + 1
   b11 = pow(b10**3 + b4*b10 + b2, (b3 + 1)
   return [b10 % b3, b11 % b3]
def fonk7(b27,Q):
  b12 = b27[0]
  b13 = Q[0]
  b14 = b27[1]
  b15 = Q[1]
  while b12 < b13:
     b12 = b12 + b3
  if b12 = = b13:
     a3 = ((3*(b12**2) + b4) * fonk4(2*b14, b3)) % b3
  else:
     a3 = ((b14-b15) * fonk4(b12-b13, b3)) % b3
  b16 = a3**2 - b12 - b13
  b17 = a3 * (b12-b16) - b14
  return [b16 % b3, b17 % b3]
def fonk8(b27,a1):
  b18 = True
  b19 = b27
  if a1 < 0:
    b19[1] = b3 - b19[1]
    a1 = (-1)*a1
  b20 = b19
  while a1 > 0:
     if (a1 % 2 != 0):
         if b18:
            b19 = b20
            b18 = False
         else:
            b19 = fonk7(b19,b20)
     b20 = fonk7(b20, b20)
     a1 = a1
  return b19
def fonk9(G,a3,Y,b21,m):
  return b21 = = fonk5(str(fonk7(fonk8(G,a3),fonk8(Y,b21))[0]) + m)
def fonk10(G,m,S,Y):
  b22 = fonk4(S[0], b5)
  b23 = fonk5(m + str(S[1]))
  b24 = (b22 * b23) % b5
  b25 = (b22 * S[1]) % b5
  return fonk7( fonk8(G, b24), fonk8(Y, b25) )[0] == S[1]
a5 = 1
while pow(a5**3 + b4*a5 + b2, (b3 - 1)
  a5 = a5 + 1
b26 = pow(a5**3 + b4*a5 + b2, (b3 + 1)
b27 = [a5,b26]
b1 = open(sys.argv[1], 'r')
b28 = b1.read()
b1.close()
b11 = [fonk2('y0'), fonk2('b14')]
b29 = [fonk2('s0'), fonk2('s1')]
print( "Public key: X: ", b11[0] % b3)
print( "Public key: Y: ", b11[1] % b3)
print( "Sigature    X: ", b29[0])
print( "Sigature    b11: ", b29[1])
print( "" )
print( "The verification of signature ", fonk9(b27, b29[0], b11, b29[1], b28))
b10 = random.randint(2,b5-1)
b30 = fonk8(b27,b10)
def fonk11(G,m,b10):
  b31 = fonk5(m + 'ecdsa')
  b32 = fonk8(G,b31)
  b23 = fonk5(m + str(b32[0]))
  a3 = ( fonk4(b31,b5) * (b23 + b32[0]*b10) ) % b5
  return [a3, b32[0]]
b29 = fonk11(b27, b28, b10)
print( "The verification of ecdsa signature ", fonk10(b27,b28,b29, b30))
def fonk12(G,m,b10):
  b31 = fonk5(m + 'kk2')
  b32 = fonk8(G,b31)
  b21 = fonk5(str(b32[0]) + m)
  return [(b31 - b10*b21) % b5, b21]
b33 = fonk5('kk1_' + str(random.randint(2,b5-1)))
b29 = fonk12(b27, b28, b33)
b11 = fonk8(b27, b33)
fonk1(b29[0],'s0')
fonk1(b29[1],'s1')
fonk1(b11[0],'y0')
fonk1(b11[1],'b14')
a6 = 0
while 2**a6 < b5:
  a6 = a6 + 1
print ("\nMore security checks ")
print ("bitlength ", a6)
print ("\ncheck b3       ", pow(7,b3-1,b3) == 1)
print ("b3 order       ", pow(7,b5-1,b5) == 1)
print ("period            ", b27 = = fonk8(b27,b5+1))
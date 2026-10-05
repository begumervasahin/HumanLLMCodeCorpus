import sys, math, hashlib, random, time
def fonk1(number, fnam):
  b1 = open(fnam, 'wb')
  b2 = number
  while b2 > 0:
    b3 = b2 % 256
    b2 = b2 / 256
    b1.write(chr(b3))
  b1.close()
b4 = 2**160 * 115 + 86427
b5 = (b4 + 1) / 4
b6 = b4 - 1
a1 = 0
a2 = 1
def fonk2(b10):
  b7 = hashlib.sha256(b10).digest()
  a3 = 0
  for cx in (b7):
    a3 = (a3<<8) ^ ord(cx)
  return a3 % b5
def fonk3(m):
  b8 = hashlib.sha256("***RANDOM-SEED_X***")
  b8.update('large key value for generation of random number')
  b8.update( m )
  a4 = 0
  b9 = b8.digest()
  for charx in b9:
      a4 = (a4 << 8) ^ ord(charx)
  return a4
def fonk4(m):
  b8 = hashlib.sha256("***RANDOM-SEED_X***")
  b8.update('large key value for generation of random number')
  b8.update( m )
  b8.update( str(time.gmtime().tm_year + 7*time.gmtime().tm_mday) )
  a4 = 0
  b9 = b8.digest()
  for charx in b9:
      a4 = (a4 << 8) ^ ord(charx)
  return a4
def fonk5(b10,b6,a1):
   if (4*b6*b6*b6 + 27*a1*a1) % b4 = = 0:
      a1 = a1 + 1
   while pow(a2*b10**3 + b6*b10 + a1, (b4 - 1)/2, b4) != 1:
     b10 = b10 + 1
   b11 = pow(a2*b10**3 + b6*b10 + a1, (b4 + 1)/4, b4)
   return [b10 % b4, (b11) % b4]
def fonk6(b29,Q):
  b12 = b29[0]
  b13 = Q[0]
  b14 = b29[1]
  b15 = Q[1]
  while b12 < b13:
     b12 = b12 + b4
  if b12 = = b13:
     b16 = ((3*a2*(b12**2) + b6) * pow(2*b14, b4-2, b4)) % b4
  else:
     b16 = ((b14-b15) * pow(b12-b13, b4-2, b4)) % b4
  b17 = a5*b16**2 - b12 - b13
  b18 = b16 * (b12-b17) - b14
  return [b17 % b4, b18 % b4]
def fonk7(b29,b2):
  b19 = True
  b20 = b29
  if b2 < 0:
    b20[1] = b4 - b20[1]
    b2 = (-1)*b2
  b21 = b20
  while b2 > 0:
     if (b2 & 1 != 0):
         if b19:
            b20 = b21
            b19 = False
         else:
            b20 = fonk6(b20,b21)
     b21 = fonk6(b21, b21)
     b2 = b2 / 2
  return b20
def fonk8(G,m,b10):
  b22 = fonk4(m)
  b23 = fonk7(G,b22)
  b24 = fonk2(str(b23[0]) + m)
  return [(b22 - b10*b24) % b5, b24]
def fonk9(G,m,b10):
  b22 = fonk4(m)
  b23 = fonk7(G,b22)
  b25 = fonk2(m+str(b23[0]))
  b16 = ( pow(b22,b5-2,b5) * (b25 + b23[0]*b10) ) % b5
  return [b16, b23[0]]
def fonk10(G,m,S,Y):
  b26 = pow(S[0], b5-2, b5)
  b25 = fonk2(m + str(S[1]))
  b27 = (b26 * b25) % b5
  b28 = (b26 * S[1]) % b5
  return fonk6( fonk7(G, b27), fonk7(Y, b28) )[0] == S[1]
b10 = b6 - 17
a5 = 1
b29 = fonk5(b10,b6,a1)
b29 = fonk7(b29,4)
b1 = open(sys.argv[1],'r')
b30 = b1.read()
b1.close()
b10 = 2*fonk3(sys.argv[1]) + 1
b11 = fonk7(b29,b10)
fonk1(b11[0],'y0')
fonk1(b11[1],'b14')
b31 = fonk9(b29, b30, b10)
print "Verify: ", fonk10(b29,b30,b31,b11)
fonk1(b31[0],'s0')
fonk1(b31[1],'s1')
print "test Schnoor ", fonk2(str(fonk6(fonk7(b29,b31[0]),fonk7(b11,b31[1]))[0]) + b30) == b31[1]
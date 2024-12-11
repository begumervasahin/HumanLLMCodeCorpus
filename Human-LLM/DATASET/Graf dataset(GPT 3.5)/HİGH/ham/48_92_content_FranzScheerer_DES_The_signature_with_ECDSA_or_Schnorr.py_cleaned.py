'''
Public b13: X:  103906006718052110902169049870974959817427789371704
Public b13: Y:  1674806087064178522885202972342590242420415136331
Sigature    X:  18010107303844949835350100892884460288168430083581
Sigature    b15:  34523600745681466958569379715665959497545247519603
The verification of signature  False
The verification of ecdsa signature  True
'''
import sys, math, hashlib, random, time
def fonk1(number, fnam):
  b1 = open(fnam, 'wb')
  b2 = number
  while b2 > 0:
    b3 = b2 % 256
    b2 = b2 / 256
    b1.write(chr(b3))
  b1.close()
b4 = 2**256 - 2**224 + 2**192 + 2**96 - 1
def fonk2(b19):
  a1 = 0
  for a2 in b19:
    a1 = (a1<<8) ^ ord(a2)
  return a1
def fonk3(b19):
  a1 = ''
  while b19 > 0:
    a1 = chr(b19 % 256) + a1
    b19 /= 256
  return a1
def fonk4(b10,b5):
  while b5 > 0:
    b10,b5 = b5,b10 % b5
  return b10
def fonk5(b6):
 while b6 % 8 != 3:
   b6 = b6 + 1
 return fonk6(b6)
def fonk6(b6):
  b7 = 3*5*7*11*13*17*19*23*29
  while True:
    while fonk4(b6,b7) != 1:
      b6 = b6 + 8
    b8 = (b6+1)/4
    if (pow(2,b6-1,b6) != 1 or pow(2,b8-1,b8) != 1):
       b6 = b6 + 8
       continue
    if (pow(3,b6-1,b6) != 1 or pow(3,b8-1,b8) != 1):
       b6 = b6 + 8
       continue
    if (pow(5,b6-1,b6) != 1 or pow(5,b8-1,b8) != 1):
       b6 = b6 + 8
       continue
    if (pow(17,b6-1,b6) != 1 or pow(17,b8-1,b8) != 1):
       b6 = b6 + 8
       continue
    break
  return b6
b4 = 2**160 * 115 + 86427
b9 = (b4 + 1) / 4
b10 = b4 - 1
a2 = 1
def fonk7(b5,m):
  a3 = 0
  a4 = 1
  b10 = m
  while b5 != 1:
    b8 = b10/b5
    b11 = b5
    b5 = b10 % b5
    b10 = b11
    b12 = a4
    a4 = a3 - b8*a4
    a3 = b12
  if a4 < 0:
    a4 = a4 + m
  return a4
def fonk8(m, b13, b4):
  return pow(m, b13, b4)
def fonk9(a2, b13, b4):
  b13 = fonk7(b13, b4 - 1)
  return pow(a2, b13, b4)
def fonk10(b19):
  a1 = 0
  for a2 in b19:
    if ord(a2) < 58 and ord(a2) >= 48:
       a1 = (a1<<4) + ord(a2) - 48
    elif ord(a2) <= ord('b1') and ord(a2) >= ord('b10'):
       a1 = (a1<<4) + ord(a2) - 87
  return a1
b14 = "5ac635d8 aa3a93e7 b3ebbd55 769886bc 651d06b0 cc53b0f6 3bce3c3e 27d2604b"
b5 = fonk10(b14)
b5 = 0
def fonk11(b19):
  a1 = 0
  for a2 in b19:
     if ord(a2) >= 48 and ord(a2) < 58:
       a1 = (a1 << 6) + ord(a2) - 48
     if ord(a2) >= 65 and ord(a2) < 91:
       a1 = (a1 << 6) + ord(a2) - 55
     if ord(a2) >= 97 and ord(a2) < 123:
       a1 = (a1 << 6) + ord(a2) - 61
     if a2 = = '
       a1 = (a1 << 6) + 62
     if a2 = = '/':
       a1 = (a1 << 6) + 63
  return a1
def fonk12(b19):
  a1 = ''
  while b19 > 0:
    b15 = b19 % 64
    if b15 < 10:
       a1 = chr( b15 + 48 ) + a1
    elif b15 < 36:
       a1 = chr( b15 + 55 ) + a1
    elif b15 < 62:
       a1 = chr( b15 + 61 ) + a1
    elif b15 = = 62:
       a1 = '
    elif b15 = = 63:
       a1 = '/' + a1
    b19 /= 64
  return a1
def fonk13(b19):
  b16 = hashlib.sha256(b19).digest()
  a1 = 0
  for cx in (b16):
    a1 = (a1<<8) ^ ord(cx)
  return a1 % b9
def fonk14(m):
  b17 = hashlib.sha256("***RANDOM-SEED_X***")
  b17.update('large b13 value for generation of random number')
  b17.update( m )
  a5 = 0
  b18 = b17.digest()
  for i in range(len(b18)):
      a5 = (a5 << 8) ^ ord(b18[i])
  return a5
def fonk15(m):
  b17 = hashlib.sha256("***RANDOM-SEED_X***")
  b17.update('large b13 value for generation of random number')
  b17.update( m )
  b17.update( str(time.gmtime().tm_year + time.gmtime().tm_mday))
  a5 = 0
  b18 = b17.digest()
  for i in range(len(b18)):
      a5 = (a5 << 8) ^ ord(b18[i])
  return a5
def fonk16(b19,b10,b5):
   if (4*b10*b10*b10 + 27*b5*b5) % b4 = = 0:
      b5 = b5 + 1
   while pow(a2*b19**3 + b10*b19 + b5, (b4 - 1)/2, b4) != 1:
     b19 = b19 + 1
   b15 = pow(a2*b19**3 + b10*b19 + b5, (b4 + 1)/4, b4)
   return [b19 % b4, (b15) % b4]
def fonk17(b22):
  b19 = b22[0]
  b15 = b22[1]
  a3 = ((3*a2*(b19**2) + b10) * fonk7(2*b15, b4)) % b4
  b20 = (a7*a3**2 - 2*b19) % b4
  b21 = (-b15 + a3 * (b19-b20)) % b4
  return [b20 , b21]
def fonk18(b22,Q):
  if b22 = = Q:
    return fonk17(b22)
  b23 = b22[0]
  b24 = Q[0]
  b25 = b22[1]
  b26 = Q[1]
  while b23 < b24:
     b23 = b23 + b4
  while b25 < b26:
     b25 = b25 + b4
  a3 = ((b25-b26) * fonk7(b23-b24, b4)) % b4
  b20 = a7*a3**2 - b23 - b24
  b21 = a3 * (b23-b20) - b25
  return [b20 % b4, b21 % b4]
def fonk19(b22,b2):
  b27 = True
  b28 = b22
  if b2 < 0:
    b28[1] = b4 - b28[1]
    b2 = (-1)*b2
  a6 = 20
  while 2**a6 < b2:
     a6 = a6 + 1
  b29 = b28
  for b5 in range(a6 + 1):
     if (b2 & (1 << b5) != 0):
         if b27:
            b28 = b29
            b27 = False
         else:
            b28 = fonk18(b28,b29)
     b29 = fonk17(b29)
  return b28
def fonk20(G,m,b19):
  b30 = fonk15(m)
  b31 = fonk19(G,b30)
  b32 = fonk13(str(b31[0]) + m)
  return [(b30 - b19*b32) % b9, b32]
def fonk21(G,m,b19):
  b30 = fonk15(m)
  b31 = fonk19(G,b30)
  b33 = fonk13(m+str(b31[0]))
  a3 = ( fonk7(b30,b9) * (b33 + b31[0]*b19) ) % b9
  return [a3, b31[0]]
def fonk22(G,m,S,Y):
  b34 = fonk7(S[0], b9)
  b33 = fonk13(m + str(S[1]))
  b35 = (b34 * b33) % b9
  b36 = (b34 * S[1]) % b9
  return fonk18( fonk19(G, b35), fonk19(Y, b36) )[0] == S[1]
b19 = b10 - 17
a7 = 1
b22 = fonk16(b19,b10,b5)
b22 = fonk19(b22,4)
b1 = open(sys.argv[1],'r')
b37 = b1.read()
b1.close()
b19 = 2*fonk14(sys.argv[1]) + 1
b15 = fonk19(b22,b19)
fonk1(b15[0],'y0')
fonk1(b15[1],'b25')
b38 = fonk21(b22, b37, b19)
print "Verify: ", fonk22(b22,b37,b38,b15)
fonk1(b38[0],'s0')
fonk1(b38[1],'s1')
print "test Schnoor ", fonk13(str(fonk18(fonk19(b22,b38[0]),fonk19(b15,b38[1]))[0]) + b37) == b38[1]
import random, math, hashlib, sys
b1 = 2*(1416461893 + 10**500) + 1
a1 = 3
def fonk1(a,b2):
  while b2 > 0:
    a,b2 = b2,a % b2
  return a
def fonk2(b1):
 while b1 % 12 != 11:
   b1 = b1 + 1
 return fonk3(b1)
def fonk3(b1):
  b3 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31
  while True:
    while fonk1(b1, b3) != 1 or fonk1((b1-1)/2, b3) != 1:
      b1 = b1 + 12
    if pow(7,b1-1,b1) != 1:
      b1 = b1 + 12
      continue
    if (pow(7,(b1-3)/2, (b1-1)/2) != 1):
      b1 = b1 + 12
      continue
    return b1
print "check b1 ", pow(11,b1-1,b1) == 1
b4 = (b1-1)/2
print "check (b1-1)/2 ", pow(11,b4-1,b4) == 1
print "\n", b1
a2 = 2134143854854758971
a3 = 2994143854854754312412
b5 = pow(a1,a2,b1)
b6 = pow(a1,a3,b1)
print "Public key send form Alice to Bob\n", b5
print "Public key send form Bob to Alice\n", b6
b7 = pow(b6,a2,b1)
b8 = pow(b5,a3,b1)
print "Are the keys equal? We check it: ", b7 = = b8
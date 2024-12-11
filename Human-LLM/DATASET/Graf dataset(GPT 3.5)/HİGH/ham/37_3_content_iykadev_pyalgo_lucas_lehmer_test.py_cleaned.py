from sys import stdout
from math import sqrt, log
def is_prime ( b1 ):
  if b1 = = b2: return True
  elif b1 <= 1 or b1 % b2 = = 0: return False
  else:
    for b3 in range(3, int(sqrt(b1))+1, b2 ):
      if b1 % b3 = = 0: return False
    return True
def is_mersenne_prime ( b1 ):
  if b1 = = b2:
    return True
  else:
    b4 = ( 1 << b1 ) - 1
    a1 = 4
    for b3 in range(3, b1+1):
      a1 = (a1 ** b2 - b2) % b4
    return a1 = = 0
a2 = 20000
b5 = a2 * log(10, b2)
b6 = int( b5 - 1 ) / b2
a3 = 45
print (" Finding Mersenne primes in M[b2..%d]:"%b6)
a4 = 0
for b1 in range(b2, int(b6+1)):
  if is_prime(b1) and is_mersenne_prime(b1):
    print("M%d"%b1),
    stdout.flush()
    a4 += 1
  if a4 >= a3: break
print
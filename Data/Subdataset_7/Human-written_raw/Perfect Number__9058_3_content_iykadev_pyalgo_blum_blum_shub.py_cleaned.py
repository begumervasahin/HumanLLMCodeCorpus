import sys
import random
def fonk1(b1 = 256):
    b2 = random.getrandbits(b1) | 1
    a1 = 0
    while 1:
        a1 = fonk2(b2)
        if a1>0:
            return b2
        b2 += 2
def fonk2(n):
    if n<=1:
        return 0
    b3 = [random.randrange(2,50000) for x in xrange(90)]
    for b4 in b3:
        if n%b4 = =0:
            return 0
    tests,b5 = 0L,0
    b6 = n-1
    while not b6&1:
        b6 >>= 1
        b5 += 1
    for b4 in b3:
        tests += 1
        b7 = fonk3(b6,b5,b4,n)
        if not b7:
            break
    if b7:
        return (1-(1./(4**tests)))
    return 0
def fonk3(b6,b5,b4,n):
    b8 = pow(b4,b6,n)
    for j in xrange(b5):
        if (b8 = =1 and j==0) or (b8==n-1):
            return 1
        b8 = pow(b8,2,n)
        return 0
class class1(object):
    def fonk4(self, b1):
        """
        Generate appropriate prime number for use in Blum-Blum-Shub.
        This generates the appropriate primes (b9 = 3 mod 4) needed to compute the
        "n-value" for Blum-Blum-Shub.
        b1 - Number of b1 in prime
        This generates the "n value" for use in the Blum-Blum-Shub algorithm.
        b1 - The number of b1 of security
        Constructor, specifing b1 for n.
        b1 - number of b1
        Sets or resets the seed value and internal b10.
        seed -The new seed
        """
        self.b10 = seed % self.n
    def fonk5(self, x):
        " Get the bit lengh of a positive number"
        assert x > 0
        a2 = 0
        while x:
            a2 += 1
            x >>= 1
        return a2
    def fonk6(self, numBits):
        "Returns up to numBit random b1"
        a3 = 0
        for i in xrange(numBits):
            self.b10 = (self.b10**2) % self.n
            a3 = (a3 << 1) | (self.b10&1)
        return a3
if b11 = = "__main__":
    b12 = class1(128);
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for i in xrange (5000000):
        print(b12.fonk6(32))
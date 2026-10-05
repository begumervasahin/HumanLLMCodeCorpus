import sys
import random
def bigppr(bits=256):
    candidate = random.getrandbits(bits) | 1
    prob = 0
    while 1:
        prob=pptest(candidate)
        if prob>0:
            return candidate
        candidate += 2
def pptest(n):
    if n<=1:
        return 0
    bases  = [random.randrange(2,50000) for x in xrange(90)]
    for b in bases:
        if n%b==0:
            return 0
    tests,s  = 0L,0
    m        = n-1
    while not m&1:
        m >>= 1
        s += 1
    for b in bases:
        tests += 1
        isprob = algP(m,s,b,n)
        if not isprob:
            break
    if isprob:
        return (1-(1./(4**tests)))
    return 0
def algP(m,s,b,n):
    y = pow(b,m,n)
    for j in xrange(s):
        if (y==1 and j==0) or (y==n-1):
            return 1
        y = pow(y,2,n)
        return 0
class BlumBlumShub(object):
    def getPrime(self, bits):
        """
        Generate appropriate prime number for use in Blum-Blum-Shub.
        This generates the appropriate primes (p = 3 mod 4) needed to compute the
        "n-value" for Blum-Blum-Shub.
        bits - Number of bits in prime
        This generates the "n value" for use in the Blum-Blum-Shub algorithm.
        bits - The number of bits of security
        Constructor, specifing bits for n.
        bits - number of bits
        Sets or resets the seed value and internal state.
        seed -The new seed
        """
        self.state = seed % self.n
    def bitLen(self, x):
        " Get the bit lengh of a positive number"
        assert x > 0
        q = 0
        while x:
            q += 1
            x >>= 1
        return q
    def next(self, numBits):
        "Returns up to numBit random bits"
        result = 0
        for i in xrange(numBits):
            self.state = (self.state**2) % self.n
            result = (result << 1) | (self.state&1)
        return result
if __name__ == "__main__":
    bbs = BlumBlumShub(128);
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for i in xrange (5000000):
        print(bbs.next(32))
import random
def generate_probable_prime(bits=256):
    candidate = random.getrandbits(bits) | 1
    while not is_probable_prime(candidate):
        candidate += 2
    return candidate
def is_probable_prime(n, num_bases=90):
    if n <= 1:
        return False
    bases = [random.randrange(2, 50000) for _ in range(num_bases)]
    for b in bases:
        if n % b == 0:
            return False
    tests, s = 0, 0
    m = n - 1
    while not m & 1:
        m >>= 1
        s += 1
    for b in bases:
        tests += 1
        is_prob = miller_rabin(m, s, b, n)
        if not is_prob:
            return False
    return True
def miller_rabin(m, s, b, n):
    y = pow(b, m, n)
    for _ in range(s):
        if (y == 1 and s == 0) or (y == n - 1):
            return True
        y = pow(y, 2, n)
    return False
class BlumBlumShub:
    def __init__(self, bits):
        self.n = self._generate_n(bits)
        length = self._bit_length(self.n)
        seed = random.getrandbits(length)
        self._set_seed(seed)
    def _generate_prime(self, bits):
        while True:
            p = generate_probable_prime(bits)
            if p & 3 == 3:
                return p
    def _generate_n(self, bits):
        p = self._generate_prime(bits
        while True:
            q = self._generate_prime(bits
            if p != q:
                return p * q
    def _set_seed(self, seed):
        self.state = seed % self.n
    def _bit_length(self, x):
        assert x > 0
        length = 0
        while x:
            length += 1
            x >>= 1
        return length
    def next(self, num_bits):
        result = 0
        for _ in range(num_bits):
            self.state = (self.state ** 2) % self.n
            result = (result << 1) | (self.state & 1)
        return result
if __name__ == "__main__":
    bbs = BlumBlumShub(128)
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for _ in range(5000000):
        print(bbs.next(32))
from math import sqrt
from itertools import count, islice
import random
class DHCalculator:
    def __init__(self):
        self.a = 0
        self.B = 0
        self.P = 0
    def isPrime(self, n):
        return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))
    def generateGP(self):
        minN = 1000
        maxN = 10000
        cached_primes = [i for i in range(minN, maxN) if self.isPrime(i)]
        return random.choice([i for i in cached_primes if minN < i < maxN])
    def setA(self, a):
        self.a = a
    def calcularA(self, G, P):
        return G ** self.a % P
    def calcularKey(self, B, P):
        return B ** self.a % P
def main():
    dh_calculator = DHCalculator()
    P = dh_calculator.generateGP()
    G = random.randint(2, P - 1)
    print(f"Generated prime P: {P} and base G: {G}")
    private_key_a = random.randint(1, P - 1)
    dh_calculator.setA(private_key_a)
    print(f"Private key a: {private_key_a}")
    A = dh_calculator.calcularA(G, P)
    print(f"Public value A: {A}")
    public_key_B = random.randint(2, P - 1)
    print(f"Received public value B: {public_key_B}")
    shared_secret = dh_calculator.calcularKey(public_key_B, P)
    print(f"The shared secret key is: {shared_secret}")
if __name__ == "__main__":
    main()
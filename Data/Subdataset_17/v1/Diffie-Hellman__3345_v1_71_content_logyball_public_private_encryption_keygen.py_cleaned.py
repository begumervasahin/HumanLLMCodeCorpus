import random
from millerrabin import isPrime
GENERATOR = 2
def fake32BitInt(num):
    return num % 4294967295
def getPrime(bitLength=31):
    while True:
        random_num = random.getrandbits(bitLength)
        if (random_num % 12) != 5:
            continue
        prime = (2 * random_num) + 1
        if isPrime(prime) and prime > 2147483648:
            return prime
def getPriKey(userSeed, prime):
    random.seed(userSeed)
    return random.randint(1, prime - 2)
def getE2(privateKey, prime, gen=GENERATOR):
    return pow(gen, privateKey, prime)
def getKeys(seed=None):
    prime = getPrime()
    priKey = getPriKey(seed, prime)
    e2 = getE2(priKey, prime)
    return {
        'd': priKey,
        'p': prime,
        'g': GENERATOR,
        'e2': e2
    }
if __name__ == '__main__':
    keys = getKeys(seed='user-defined-seed')
    print("Generated Keys:")
    print(f"Private Key (d): {keys['d']}")
    print(f"Prime (p): {keys['p']}")
    print(f"Generator (g): {keys['g']}")
    print(f"e2: {keys['e2']}")
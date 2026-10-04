b1 = "Mr Bancroft"
from random import sample
def fonk1(prime):
    a1 = 0
    print("Working out public key and public shared base...")
    b2 = []
    for each in range(1, prime):
        a1 += 1
        b3 = []
        for i in range(1, prime):
            b4 = (a1 ** i) % prime
            b3.append(b4)
            b5 = set(b3)
            if len(b5) == len(range(1, prime)):
                b2.append(a1)
    return sample(b2, 1)[0]
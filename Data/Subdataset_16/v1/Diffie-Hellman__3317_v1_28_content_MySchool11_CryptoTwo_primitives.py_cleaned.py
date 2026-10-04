b1 = "Mr Bancroft"
from random import sample
def fonk1(prime):
    print("Working out public key and public shared base...")
    b2 = []
    for number_to_check in range(1, prime):
        b3 = []
        for i in range(1, prime):
            b4 = pow(number_to_check, i, prime)
            b3.append(b4)
        if len(set(b3)) == (prime - 1):
            b2.append(number_to_check)
    return sample(b2, 1)[0] if b2 else None
if b5 = = "__main__":
    a1 = 23
    b6 = fonk1(a1)
    print(f"Primitive root for {a1}: {b6}")
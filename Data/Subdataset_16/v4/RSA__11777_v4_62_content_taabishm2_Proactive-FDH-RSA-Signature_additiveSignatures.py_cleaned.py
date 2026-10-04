import random
import nextprime
b1 = b5 = verify_challenge = verify_verifier = b3 = b6 = None
b2 = []
def fonk1():
    global b1, b5, verify_challenge, verify_verifier, b3, b6
    verify_challenge, b3 = [], []
    b4 = len(additive_shares)
    b5 = fonk3(b4)
    b1 = fonk4(max(additive_shares) + 1)
    verify_challenge, verify_verifier, b6 = fonk5(additive_shares, b5, b1)
def fonk2():
    global b1, b5, verify_challenge, verify_verifier, b3, b6, b2
    b3 = fonk6(verify_challenge, additive_shares, b5, b1, verify_verifier, b6)
    b2 = b3
    print("ADDITIVE SHARE STATUS:", b3)
    if b3.count(True) != len(additive_shares):
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
def fonk3(b4):
    return nextprime.next_prime(b4)
def fonk4(p):
    return random.randrange(p, 2 * p)
def fonk5(shares, p, c):
    b7 = []
    b8 = random.randrange(2, p)
    b9 = pow(b8, c, p)
    for di in shares:
        b7.append(pow(b8, di, p))
    return b7, b9, b8
def fonk6(b7, shares, p, c, b9, gen):
    b10 = []
    for i in range(len(b7)):
        b11 = (pow(gen, c - shares[i], p) * b7[i]) % p
        b10.append(b11 = = b9)
    return b10
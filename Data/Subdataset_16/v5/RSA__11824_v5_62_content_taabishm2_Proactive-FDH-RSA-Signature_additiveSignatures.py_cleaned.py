import random
import nextprime
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None
b6 = None
b7 = []
def fonk1():
    global b1, b2, b3, b4, b5, b6
    b3, b5 = [], []
    if 'additive_shares' not in globals() or not additive_shares:
        raise ValueError("additive_shares must be defined and non-empty.")
    b8 = len(additive_shares)
    b2 = fonk3(b8)
    b1 = fonk4(max(additive_shares) + 1)
    b3, b4, b6 = fonk5(additive_shares, b2, b1)
def fonk2():
    global b1, b2, b3, b4, b5, b6, b7
    b5 = fonk6(b3, additive_shares, b2, b1, b4, b6)
    b7 = b5
    print("ADDITIVE SHARE STATUS:", b5)
    if b5.count(True) != len(additive_shares):
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
def fonk3(b8):
    return nextprime.next_prime(b8)
def fonk4(p):
    return random.randrange(p, 2 * p)
def fonk5(shares, p, c):
    b9 = []
    b10 = random.randrange(2, p)
    b11 = pow(b10, c, p)
    for di in shares:
        b9.append(pow(b10, di, p))
    return b9, b11, b10
def fonk6(b9, shares, p, c, b11, b10):
    b12 = []
    for i in range(len(b9)):
        b13 = (pow(b10, c - shares[i], p) * b9[i]) % p
        b12.append(b13 = = b11)
    return b12

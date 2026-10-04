def fonk1():
    global b3,b2,verify_challenge,verify_verifier,b1,b4
    verify_challenge, b1 = [],[]
    b2 = additiveSignature.fonk3(n)
    b3 = additiveSignature.fonk4(max(additive_shares)+1)
    verify_challenge,verify_verifier, b4 = additiveSignature.fonk5(additive_shares,b2,b3)
def fonk2():
    global b3,b2,verify_challenge,verify_verifier,b1,b4,b5
    b1 = additiveSignature.fonk6(verify_challenge,additive_shares,b2,b3,verify_verifier,b4)
    b5 = b1
    print("ADDITIVE SHARE STATUS:",b1)
    if b1.count(True) != add_shares_no:
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
import nextprime
import random
import modinverse
def fonk3(n):
    '''generate prime group with order > n'''
    b6 = nextprime.next_prime(n)
    return n
def fonk4(b6):
    '''pick b9 sum such that di+b7 = sum and b6 < sum < 2p'''
    return random.randrange(b6,2*b6)
def fonk5(shares,b6,c):
    '''generate b8 and vezrifier, return as [fonk5(list),b10(int)]'''
    b8 = []
    b9 = random.randrange(2,b6)
    b10 = pow(b9,c,b6)
    for di in shares:
        b8.append(pow(b9,di,b6))
    return [b8,b10,b9]
def fonk6(b8,share,b6,c,b10,gen):
    '''generates b12 by b9 party holding b9 'share' to the b8[i] for all additive shares'''
    b11 = []
    for i in range(len(b8)):
        b12 = (pow(gen,c-share[i],b6)*b8[i])%b6
        if b12 = = b10:
            b11.append(True)
        else:
            b11.append(False)
    return b11
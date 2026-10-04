import random
from sympy import nextprime
from sympy.core.numbers import igcdex
def modinverse(a, m):
    g, x, _ = igcdex(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m
class AdditiveSignature:
    @staticmethod
    def init(n):
        '''Generate prime group with order > n'''
        p = nextprime(n)
        return p
    @staticmethod
    def pick_sum(p):
        '''Pick a sum such that di + di_dash = sum and p < sum < 2p'''
        return random.randrange(p, 2 * p)
    @staticmethod
    def challenge(shares, p, c):
        '''Generate challenge and verifier, return as [challenge(list), verifier(int)]'''
        challenge = []
        a = random.randrange(2, p)
        verifier = pow(a, c, p)
        for di in shares:
            challenge.append(pow(a, di, p))
        return [challenge, verifier, a]
    @staticmethod
    def response(challenge, shares, p, c, verifier, gen):
        '''Generates response by a party holding a 'share' to the challenge[i] for all additive shares'''
        res = []
        for i in range(len(challenge)):
            response = (pow(gen, c - shares[i], p) * challenge[i]) % p
            res.append(response == verifier)
        return res
verify_sum = verify_p = verify_challenge = verify_verifier = verify_response = verify_generator = None
share_status = None
additive_shares = [3, 4, 5]
add_shares_no = len(additive_shares)
n = max(additive_shares) + 1
def additive_signature():
    global verify_sum, verify_p, verify_challenge, verify_verifier, verify_response, verify_generator
    verify_challenge, verify_response = [], []
    verify_p = AdditiveSignature.init(n)
    verify_sum = AdditiveSignature.pick_sum(max(additive_shares) + 1)
    verify_challenge, verify_verifier, verify_generator = AdditiveSignature.challenge(additive_shares, verify_p, verify_sum)
def additive_signature_verify():
    global verify_sum, verify_p, verify_challenge, verify_verifier, verify_response, verify_generator, share_status
    verify_response = AdditiveSignature.response(verify_challenge, additive_shares, verify_p, verify_sum, verify_verifier, verify_generator)
    share_status = verify_response
    print("ADDITIVE SHARE STATUS:", verify_response)
    if verify_response.count(True) != add_shares_no:
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
additive_signature()
additive_signature_verify()
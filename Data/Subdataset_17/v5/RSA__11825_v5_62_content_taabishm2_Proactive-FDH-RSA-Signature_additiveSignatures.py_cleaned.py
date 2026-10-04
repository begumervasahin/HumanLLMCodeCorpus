import random
import nextprime
verify_sum = None
verify_p = None
verify_challenge = None
verify_verifier = None
verify_response = None
verify_generator = None
share_status = []
def additive_signature():
    global verify_sum, verify_p, verify_challenge, verify_verifier, verify_response, verify_generator
    verify_challenge, verify_response = [], []
    if 'additive_shares' not in globals() or not additive_shares:
        raise ValueError("additive_shares must be defined and non-empty.")
    n = len(additive_shares)
    verify_p = init_prime_group(n)
    verify_sum = pick_sum(max(additive_shares) + 1)
    verify_challenge, verify_verifier, verify_generator = generate_challenge(additive_shares, verify_p, verify_sum)
def additive_signature_verify():
    global verify_sum, verify_p, verify_challenge, verify_verifier, verify_response, verify_generator, share_status
    verify_response = generate_response(verify_challenge, additive_shares, verify_p, verify_sum, verify_verifier, verify_generator)
    share_status = verify_response
    print("ADDITIVE SHARE STATUS:", verify_response)
    if verify_response.count(True) != len(additive_shares):
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
def init_prime_group(n):
    return nextprime.next_prime(n)
def pick_sum(p):
    return random.randrange(p, 2 * p)
def generate_challenge(shares, p, c):
    challenge = []
    generator = random.randrange(2, p)
    verifier = pow(generator, c, p)
    for di in shares:
        challenge.append(pow(generator, di, p))
    return challenge, verifier, generator
def generate_response(challenge, shares, p, c, verifier, generator):
    responses = []
    for i in range(len(challenge)):
        response = (pow(generator, c - shares[i], p) * challenge[i]) % p
        responses.append(response == verifier)
    return responses

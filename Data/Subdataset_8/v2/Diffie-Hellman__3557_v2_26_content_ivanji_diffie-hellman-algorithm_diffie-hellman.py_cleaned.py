
shared_base = 47
shared_prime = 199
print("Shared base (g) is equal to %s and shared prime (p) is equal to %s" % (shared_base, shared_prime))
print("--------------------------")
alice_secret = 6
bob_secret = 2
print("--------------------------")
print("Alice calculates: (g^a) mod p and sends the result (A) to Bob")
A = (shared_base ** alice_secret) % shared_prime
print("--------------------------")
print("Bob calculates the same and sends the result (B) to Alice")
B = (shared_base ** bob_secret) % shared_prime
print("--------------------------")
print("Alice now calculates using the received result (B) from Bob")
alice_modulo = (B ** alice_secret) % shared_prime
print("--------------------------")
print("Bob now calculates using the received result (A) from Alice")
bob_modulo = (A ** bob_secret) % shared_prime
print("Bob's calculated modulo:", bob_modulo)
print("Alice's calculated modulo:", alice_modulo)
print("--------------------------")
print("Shared Key is equal to %s." % bob_modulo)
print("Now try this with large prime numbers!")
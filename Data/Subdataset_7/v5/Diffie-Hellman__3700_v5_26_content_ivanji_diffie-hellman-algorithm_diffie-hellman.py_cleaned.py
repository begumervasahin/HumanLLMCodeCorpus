
a1 = 47
a2 = 199
print("Shared base (g) is equal to %s and shared prime (p) is equal to %s" % (a1, a2))
print("--------------------------")
a3 = 6
a4 = 2
print("--------------------------")
print("Alice performs the following operation: g^a mod p and sends the result (b1) to Bob")
b1 = pow(a1, a3, a2)
print("--------------------------")
print("Bob performs the same operation and sends the result (b2) to Alice")
b2 = pow(a1, a4, a2)
print("--------------------------")
print("Alice now performs the same operation using the calculated result (b2) from Bob")
b3 = pow(b2, a3, a2)
print("--------------------------")
print("Bob now performs the same operation using the calculated result (b1) from Alice")
b4 = pow(b1, a4, a2)
print("Bob's calculated modulo:", b4)
print("Alice's calculated modulo:", b3)
print("--------------------------")
print("Shared Key is equal to %s." % b4)
print("Now try this with large prime numbers!")
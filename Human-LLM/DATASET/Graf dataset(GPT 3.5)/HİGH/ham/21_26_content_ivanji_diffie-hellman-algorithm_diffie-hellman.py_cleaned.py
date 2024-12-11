a1 = 47
a2 = 199
print "g is equal to %s & p is equal to %s" % (a1, a2)
print "--------------------------"
a3 = 6
a4 = 2
print "--------------------------"
print "Alice performs the following operation: g^a mod p and sends result (b1) to Bob"
b1 = (a1**a3) % a2
print "--------------------------"
print "Bob performs same operation and sends result (b2) to Alice"
b2 = (a1**a4) % a2
print "--------------------------"
print "Alice now performs same operation using calculated result (b2) from Bob"
b3 = (b2**a3) % a2
print "--------------------------"
print "Bob now performs same operation using calculated result (b1) from Alice"
b4 = (b1**a4) % a2
print b4
print b3
print "--------------------------"
print "Shared Key is equal to %s." % b4
print "Now try this with large prime numbers!"
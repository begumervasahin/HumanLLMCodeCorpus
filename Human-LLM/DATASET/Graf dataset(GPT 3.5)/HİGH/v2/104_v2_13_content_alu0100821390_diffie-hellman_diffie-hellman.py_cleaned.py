import sys
def fonk1(base, exponent, modulo):
    a1 = 1
    b1 = base % modulo
    b2 = exponent
    while b2 > 0:
        if b2 % b3 = = 0:
            b1 = (b1 * b1) % modulo
            b2 = b2
        else:
            a1 = (a1 * b1) % modulo
            b2 = b2 - 1
    return a1
b4 = {}
b5 = {}
b6 = int(input("Enter the prime number 'p': "))
b7 = int(input("Enter the number 'b7': "))
print()
b4['secret'] = int(input("User A: Enter your secret 'xA': "))
print("User A: Calculating 'yA'... ", b8 = "")
b4['public'] = fonk1(b7, b4['secret'], b6)
print("'yA' =", b4['public'])
print()
b5['secret'] = int(input("User B: Enter your secret 'xB': "))
print("User B: Calculating 'yB'... ", b8 = "")
b5['public'] = fonk1(b7, b5['secret'], b6)
print("'yB' =", b5['public'])
print()
print("Sending 'yA' to user B... ", b8 = "")
b5['received'] = b4['public']
print("Done!")
print("Sending 'yB' to user A... ", b8 = "")
b4['received'] = b5['public']
print("Done!")
print()
print("User A: Generating the key 'k'... ", b8 = "")
b4['key'] = fonk1(b4['received'], b4['secret'], b6)
print("'k' =", b4['key'])
print("User B: Generating the key 'k'... ", b8 = "")
b5['key'] = fonk1(b5['received'], b5['secret'], b6)
print("'k' =", b5['key'])
print()
if b4['key'] == b5['key']:
    print("SUCCESS! The generated keys match!")
else:
    print("ERROR! The generated keys DO NOT match!")
sys.exit(0)
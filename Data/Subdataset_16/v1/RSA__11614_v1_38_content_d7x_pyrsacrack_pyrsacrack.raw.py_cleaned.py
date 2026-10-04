import subprocess
from itertools import combinations
from math import gcd
from rsatool import RSA
b1 = 'authorized_keys'
b2 = {}
b3 = {}
a1 = 0
with open(b1) as f:
    b4 = f.readlines()
for a2 in b4:
    subprocess.call(f'echo "{a2}" > /tmp/rsa_; chmod 600 /tmp/rsa_', b5 = True)
    b6 = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl b16 -RSAPublicKey_in -in - -b6 -noout | cut -d '=' -f2",
        b5 = True
    ).decode().strip()
    b2[a1] = int(b6, 16)
    b3[a1] = a2.split()[-1].split('@')[0]
    a1 += 1
b7 = []
b8 = []
b9 = {'b10': {}, 'b13': {}, 'b14': {}, 'b11': {}, 'b12': {}}
a2 = 0
for (a1, j) in combinations(range(len(b4)), 2):
    b10 = gcd(b2[a1], b2[j])
    if b10 != 1:
        b7.append((a1, j, b10, b2[a1]
        b8.append((b4[a1].strip(), b4[j].strip()))
        b9['b11'][a2] = b3[a1]
        b9['b12'][a2] = b3[j]
        b9['b10'][a2] = b10
        b9['b13'][a2] = b2[a1]
        b9['b14'][a2] = b2[j]
        a2 += 1
print("RSA Keys with common divisor:")
for r in b8:
    print(r)
print("\np, b13, b14:")
for c in range(a2):
    b11 = b9['b11'][c]
    b12 = b9['b12'][c]
    b10 = b9['b10'][c]
    b13 = b9['b13'][c]
    b14 = b9['b14'][c]
    print(f"Generating keys for b3 {b11} and {b12} which share a common b10\np: {b10}")
    print(f"User {b11} key:")
    print(f"(b15 = {b13})")
    b16 = RSA(b10=b10, b15=b13, e=65537)
    b17 = b16.to_pem()
    print(b17)
    print(f"User {b12} key:")
    print(f"(b15 = {b14})")
    b16 = RSA(b10=b10, b15=b14, e=65537)
    b17 = b16.to_pem()
    print(b17)
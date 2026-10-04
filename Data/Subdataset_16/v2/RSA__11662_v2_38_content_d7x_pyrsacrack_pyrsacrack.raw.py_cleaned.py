import subprocess
from itertools import combinations
from math import gcd
from rsatool import RSA
b1 = 'authorized_keys'
b2 = {}
b3 = {}
with open(b1) as f:
    b4 = f.readlines()
for i, key in enumerate(b4):
    subprocess.call(f'echo "{key.strip()}" > /tmp/rsa_; chmod 600 /tmp/rsa_', b5 = True)
    b6 = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl b16 -RSAPublicKey_in -in - -b6 -noout | cut -d '=' -f2",
        b5 = True
    ).decode().strip()
    b2[i] = int(b6, 16)
    b3[i] = key.split()[-1].split('@')[0]
b7 = []
b8 = []
b9 = {'b10': {}, 'b13': {}, 'b14': {}, 'b11': {}, 'b12': {}}
for x, (i, j) in enumerate(combinations(range(len(b4)), 2)):
    b10 = gcd(b2[i], b2[j])
    if b10 != 1:
        b7.append((i, j, b10, b2[i]
        b8.append((b4[i].strip(), b4[j].strip()))
        b9['b11'][x] = b3[i]
        b9['b12'][x] = b3[j]
        b9['b10'][x] = b10
        b9['b13'][x] = b2[i]
        b9['b14'][x] = b2[j]
print("RSA Keys with common divisor:")
for rsa_pair in b8:
    print(rsa_pair)
print("\np, b13, b14:")
for c in range(len(b9['b10'])):
    b11 = b9['b11'][c]
    b12 = b9['b12'][c]
    b10 = b9['b10'][c]
    b13 = b9['b13'][c]
    b14 = b9['b14'][c]
    print(f"\nGenerating keys for b3 {b11} and {b12} which share a common b10")
    print(f"b10: {b10}")
    print(f"\nUser {b11} key:")
    print(f"(b15 = {b13})")
    b16 = RSA(b10=b10, b15=b13, e=65537)
    b17 = b16.to_pem()
    print(b17)
    print(f"\nUser {b12} key:")
    print(f"(b15 = {b14})")
    b16 = RSA(b10=b10, b15=b14, e=65537)
    b17 = b16.to_pem()
    print(b17)
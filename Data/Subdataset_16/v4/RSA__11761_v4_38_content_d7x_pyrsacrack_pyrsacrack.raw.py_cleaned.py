import subprocess
from itertools import combinations
from fractions import gcd
from rsatool import rsatool
b1 = 'authorized_keys'
b2 = []
b3 = {}
b4 = {}
b5 = []
b6 = []
with open(b1) as f:
    b2 = f.readlines()
for i, b7 in enumerate(b2):
    b7 = b7.strip()
    subprocess.call(f'echo "{b7}" > /tmp/rsa_; chmod 600 /tmp/rsa_', b8 = True)
    b9 = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl b17 -RSAPublicKey_in -in - -modulus -noout | cut -d '=' -f2",
        b8 = True
    ).strip()
    b3[i] = int(b9, 16)
    b4[i] = b7.split()[-1].split('@')[0]
b10 = {
    'b11': {},
    'b12': {},
    'b13': {},
    'b14': {},
    'b15': {}
}
for x, (i, j) in enumerate(combinations(b3.keys(), 2)):
    b11 = gcd(b3[i], b3[j])
    if b11 != 1:
        b12 = b3[i]
        b13 = b3[j]
        b6.append((i, j, b11, b12, b13))
        b5.append((b2[i].strip(), b2[j].strip()))
        b10['b14'][x] = b4[i]
        b10['b15'][x] = b4[j]
        b10['b11'][x] = b11
        b10['b12'][x] = b12
        b10['b13'][x] = b13
print(b6)
print("RSA Keys with common divisor:")
for rsa_keys in b5:
    print(rsa_keys)
print("b11, b12, b13:")
for c in range(len(b6)):
    b14 = b10['b14'][c]
    b15 = b10['b15'][c]
    b11 = b10['b11'][c]
    b12 = b10['b12'][c]
    b13 = b10['b13'][c]
    print(f"Generating keys for b4 {b14} and {b15} which share a common b11 \np: {b11}")
    print(f"User {b14} b7:")
    print(f"(b16 = {b12})")
    b17 = rsatool.RSA(b11=b11, b16=b12, e=65537)
    print(b17.to_pem())
    print(f"User {b15} b7:")
    print(f"(b16 = {b13})")
    b17 = rsatool.RSA(b11=b11, b16=b13, e=65537)
    print(b17.to_pem())
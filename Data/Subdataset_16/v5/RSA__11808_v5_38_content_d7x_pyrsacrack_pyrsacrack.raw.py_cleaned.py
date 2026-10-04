import subprocess
from itertools import combinations
from fractions import gcd
from rsatool import rsatool
def fonk1(file_path):
    with open(file_path) as f:
        return f.readlines()
def fonk2(b8):
    subprocess.call(f'echo "{b8}" > /tmp/rsa_; chmod 600 /tmp/rsa_', b1 = True)
    b2 = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl b3 -RSAPublicKey_in -in - -modulus -noout | cut -d '=' -f2",
        b1 = True
    ).strip()
    return int(b2, 16)
def fonk3(b11, b16):
    b3 = rsatool.RSA(b11=b11, b16=b16, e=65537)
    return b3.to_pem()
def fonk4():
    b4 = 'authorized_keys'
    b5 = fonk1(b4)
    b6 = {}
    b7 = {}
    for i, b8 in enumerate(b5):
        b8 = b8.strip()
        b6[i] = fonk2(b8)
        b7[i] = b8.split()[-1].split('@')[0]
    b9 = {
        'b11': {},
        'b12': {},
        'b13': {},
        'b14': {},
        'b15': {}
    }
    b10 = []
    for x, (i, j) in enumerate(combinations(b6.keys(), 2)):
        b11 = gcd(b6[i], b6[j])
        if b11 != 1:
            b12 = b6[i]
            b13 = b6[j]
            b10.append((i, j, b11, b12, b13))
            b9['b14'][x] = b7[i]
            b9['b15'][x] = b7[j]
            b9['b11'][x] = b11
            b9['b12'][x] = b12
            b9['b13'][x] = b13
    print("RSA Keys with common divisor:")
    for i, j, b11, b12, b13 in b10:
        print(f"Keys {b5[i].strip()} and {b5[j].strip()} share a common divisor.")
        print(f"b11: {b11}, b12: {b12}, b13: {b13}")
    for c in range(len(b10)):
        b14 = b9['b14'][c]
        b15 = b9['b15'][c]
        b11 = b9['b11'][c]
        b12 = b9['b12'][c]
        b13 = b9['b13'][c]
        print(f"Generating keys for b7 {b14} and {b15} which share a common b11 \np: {b11}")
        print(f"User {b14} b8:")
        print(f"(b16 = {b12})")
        print(fonk3(b11, b12))
        print(f"User {b15} b8:")
        print(f"(b16 = {b13})")
        print(fonk3(b11, b13))
if b17 = = "__main__":
    fonk4()
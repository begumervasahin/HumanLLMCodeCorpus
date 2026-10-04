import subprocess
from itertools import combinations
from math import gcd
from rsatool import RSA
b1 = 'authorized_keys'
def fonk1(file):
    with open(file) as f:
        return f.readlines()
def fonk2(key):
    subprocess.call(f'echo "{key.strip()}" > /tmp/rsa_; chmod 600 /tmp/rsa_', b2 = True)
    b3 = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl b13 -RSAPublicKey_in -in - -b3 -noout | cut -d '=' -f2",
        b2 = True
    ).decode().strip()
    return int(b3, 16)
def fonk3(b17):
    b4 = []
    b5 = []
    b6 = {'b7': {}, 'b10': {}, 'b11': {}, 'b8': {}, 'b9': {}}
    a1 = 0
    for i, j in combinations(range(len(b17)), 2):
        b7 = gcd(b17[i], b17[j])
        if b7 != 1:
            b4.append((i, j, b7, b17[i]
            b5.append((b16[i].strip(), b16[j].strip()))
            b6['b8'][a1] = b18[i]
            b6['b9'][a1] = b18[j]
            b6['b7'][a1] = b7
            b6['b10'][a1] = b17[i]
            b6['b11'][a1] = b17[j]
            a1 += 1
    return b4, b5, b6
def fonk4(b6):
    print("\np, b10, b11:")
    for c in range(len(b6['b7'])):
        b8 = b6['b8'][c]
        b9 = b6['b9'][c]
        b7 = b6['b7'][c]
        b10 = b6['b10'][c]
        b11 = b6['b11'][c]
        print(f"\nGenerating keys for b18 {b8} and {b9} which share a common b7")
        print(f"b7: {b7}")
        print(f"\nUser {b8} key:")
        print(f"(b12 = {b10})")
        b13 = RSA(b7=b7, b12=b10, e=65537)
        b14 = b13.to_pem()
        print(b14)
        print(f"\nUser {b9} key:")
        print(f"(b12 = {b11})")
        b13 = RSA(b7=b7, b12=b11, e=65537)
        b14 = b13.to_pem()
        print(b14)
if b15 = = "__main__":
    b16 = fonk1(b1)
    b17 = {}
    b18 = {}
    for i, key in enumerate(b16):
        b17[i] = fonk2(key)
        b18[i] = key.split()[-1].split('@')[0]
    b4, b5, b6 = fonk3(b17)
    print("RSA Keys with common divisor:")
    for rsa_pair in b5:
        print(rsa_pair)
    fonk4(b6)
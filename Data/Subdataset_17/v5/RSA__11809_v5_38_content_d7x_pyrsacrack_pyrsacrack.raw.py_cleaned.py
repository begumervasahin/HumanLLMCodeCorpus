import subprocess
from itertools import combinations
from fractions import gcd
from rsatool import rsatool
def read_keys(file_path):
    with open(file_path) as f:
        return f.readlines()
def extract_modulus(key):
    subprocess.call(f'echo "{key}" > /tmp/rsa_; chmod 600 /tmp/rsa_', shell=True)
    modulus_hex = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl rsa -RSAPublicKey_in -in - -modulus -noout | cut -d '=' -f2",
        shell=True
    ).strip()
    return int(modulus_hex, 16)
def generate_rsa_keys(p, q):
    rsa = rsatool.RSA(p=p, q=q, e=65537)
    return rsa.to_pem()
def main():
    FILE = 'authorized_keys'
    keys_list = read_keys(FILE)
    rsa_moduli = {}
    users = {}
    for i, key in enumerate(keys_list):
        key = key.strip()
        rsa_moduli[i] = extract_modulus(key)
        users[i] = key.split()[-1].split('@')[0]
    common_divisors = {
        'p': {},
        'q1': {},
        'q2': {},
        'user1': {},
        'user2': {}
    }
    results = []
    for x, (i, j) in enumerate(combinations(rsa_moduli.keys(), 2)):
        p = gcd(rsa_moduli[i], rsa_moduli[j])
        if p != 1:
            q1 = rsa_moduli[i]
            q2 = rsa_moduli[j]
            results.append((i, j, p, q1, q2))
            common_divisors['user1'][x] = users[i]
            common_divisors['user2'][x] = users[j]
            common_divisors['p'][x] = p
            common_divisors['q1'][x] = q1
            common_divisors['q2'][x] = q2
    print("RSA Keys with common divisor:")
    for i, j, p, q1, q2 in results:
        print(f"Keys {keys_list[i].strip()} and {keys_list[j].strip()} share a common divisor.")
        print(f"p: {p}, q1: {q1}, q2: {q2}")
    for c in range(len(results)):
        user1 = common_divisors['user1'][c]
        user2 = common_divisors['user2'][c]
        p = common_divisors['p'][c]
        q1 = common_divisors['q1'][c]
        q2 = common_divisors['q2'][c]
        print(f"Generating keys for users {user1} and {user2} which share a common p \np: {p}")
        print(f"User {user1} key:")
        print(f"(q={q1})")
        print(generate_rsa_keys(p, q1))
        print(f"User {user2} key:")
        print(f"(q={q2})")
        print(generate_rsa_keys(p, q2))
if __name__ == "__main__":
    main()
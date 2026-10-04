import subprocess
from itertools import combinations
from fractions import gcd
from rsatool import rsatool
FILE = 'authorized_keys'
keys_list = []
rsa_moduli = {}
users = {}
rsa_list_result = []
result = []
with open(FILE) as f:
    keys_list = f.readlines()
for i, key in enumerate(keys_list):
    key = key.strip()
    subprocess.call(f'echo "{key}" > /tmp/rsa_; chmod 600 /tmp/rsa_', shell=True)
    modulus_hex = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl rsa -RSAPublicKey_in -in - -modulus -noout | cut -d '=' -f2",
        shell=True
    ).strip()
    rsa_moduli[i] = int(modulus_hex, 16)
    users[i] = key.split()[-1].split('@')[0]
p_q1_q2_list = {
    'p': {},
    'q1': {},
    'q2': {},
    'user1': {},
    'user2': {}
}
for x, (i, j) in enumerate(combinations(rsa_moduli.keys(), 2)):
    p = gcd(rsa_moduli[i], rsa_moduli[j])
    if p != 1:
        q1 = rsa_moduli[i]
        q2 = rsa_moduli[j]
        result.append((i, j, p, q1, q2))
        rsa_list_result.append((keys_list[i].strip(), keys_list[j].strip()))
        p_q1_q2_list['user1'][x] = users[i]
        p_q1_q2_list['user2'][x] = users[j]
        p_q1_q2_list['p'][x] = p
        p_q1_q2_list['q1'][x] = q1
        p_q1_q2_list['q2'][x] = q2
print(result)
print("RSA Keys with common divisor:")
for rsa_keys in rsa_list_result:
    print(rsa_keys)
print("p, q1, q2:")
for c in range(len(result)):
    user1 = p_q1_q2_list['user1'][c]
    user2 = p_q1_q2_list['user2'][c]
    p = p_q1_q2_list['p'][c]
    q1 = p_q1_q2_list['q1'][c]
    q2 = p_q1_q2_list['q2'][c]
    print(f"Generating keys for users {user1} and {user2} which share a common p \np: {p}")
    print(f"User {user1} key:")
    print(f"(q={q1})")
    rsa = rsatool.RSA(p=p, q=q1, e=65537)
    print(rsa.to_pem())
    print(f"User {user2} key:")
    print(f"(q={q2})")
    rsa = rsatool.RSA(p=p, q=q2, e=65537)
    print(rsa.to_pem())
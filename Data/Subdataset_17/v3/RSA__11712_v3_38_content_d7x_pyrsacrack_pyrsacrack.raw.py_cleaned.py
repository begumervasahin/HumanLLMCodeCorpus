import subprocess
from itertools import combinations
from math import gcd
from rsatool import RSA
FILE = 'authorized_keys'
def read_keys(file):
    with open(file) as f:
        return f.readlines()
def extract_modulus(key):
    subprocess.call(f'echo "{key.strip()}" > /tmp/rsa_; chmod 600 /tmp/rsa_', shell=True)
    modulus = subprocess.check_output(
        "ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl rsa -RSAPublicKey_in -in - -modulus -noout | cut -d '=' -f2",
        shell=True
    ).decode().strip()
    return int(modulus, 16)
def find_common_divisors(rsa_list):
    result = []
    rsa_list_result = []
    p_q1_q2_list = {'p': {}, 'q1': {}, 'q2': {}, 'user1': {}, 'user2': {}}
    x = 0
    for i, j in combinations(range(len(rsa_list)), 2):
        p = gcd(rsa_list[i], rsa_list[j])
        if p != 1:
            result.append((i, j, p, rsa_list[i]
            rsa_list_result.append((keys_list[i].strip(), keys_list[j].strip()))
            p_q1_q2_list['user1'][x] = users[i]
            p_q1_q2_list['user2'][x] = users[j]
            p_q1_q2_list['p'][x] = p
            p_q1_q2_list['q1'][x] = rsa_list[i]
            p_q1_q2_list['q2'][x] = rsa_list[j]
            x += 1
    return result, rsa_list_result, p_q1_q2_list
def generate_and_print_keys(p_q1_q2_list):
    print("\np, q1, q2:")
    for c in range(len(p_q1_q2_list['p'])):
        user1 = p_q1_q2_list['user1'][c]
        user2 = p_q1_q2_list['user2'][c]
        p = p_q1_q2_list['p'][c]
        q1 = p_q1_q2_list['q1'][c]
        q2 = p_q1_q2_list['q2'][c]
        print(f"\nGenerating keys for users {user1} and {user2} which share a common p")
        print(f"p: {p}")
        print(f"\nUser {user1} key:")
        print(f"(q={q1})")
        rsa = RSA(p=p, q=q1, e=65537)
        data = rsa.to_pem()
        print(data)
        print(f"\nUser {user2} key:")
        print(f"(q={q2})")
        rsa = RSA(p=p, q=q2, e=65537)
        data = rsa.to_pem()
        print(data)
if __name__ == "__main__":
    keys_list = read_keys(FILE)
    rsa_list = {}
    users = {}
    for i, key in enumerate(keys_list):
        rsa_list[i] = extract_modulus(key)
        users[i] = key.split()[-1].split('@')[0]
    result, rsa_list_result, p_q1_q2_list = find_common_divisors(rsa_list)
    print("RSA Keys with common divisor:")
    for rsa_pair in rsa_list_result:
        print(rsa_pair)
    generate_and_print_keys(p_q1_q2_list)
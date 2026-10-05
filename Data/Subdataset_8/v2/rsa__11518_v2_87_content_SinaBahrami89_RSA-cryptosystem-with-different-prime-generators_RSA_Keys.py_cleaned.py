import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def generate_rsa_keys(bits, prime_generator_func):
    p, q = prime_generator_func(bits), prime_generator_func(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = randrange(3, phi, 2)
        if gcd(e, phi) == 1:
            break
    a, b = phi, e
    t, t1 = 0, 1
    while b != 0:
        d = a
        t, t1 = t1, t - d * t1
        a, b = b, a - d * b
    if t < 0:
        t = t + phi
    public_key = (e, n)
    private_key = (t, n)
    return 'Public key: {}\nPrivate key: {}'.format(public_key, private_key)
if __name__ == '__main__':
    print('Available methods for generating prime numbers are Fermat, Miller-Rabin, Deterministic Miller, and Baillie-PSW')
    selected_method = input('Select your desired method for generating prime numbers: ').lower()
    prime_generation_methods = ['fermat', 'miller-rabin', 'deterministic miller', 'baillie-psw']
    prime_generators = [prime_generator.gen_fermat, prime_generator.gen_mr, prime_generator.gen_m, prime_generator.gen_bpsw]
    if selected_method in prime_generation_methods:
        prime_generator_func = prime_generators[prime_generation_methods.index(selected_method)]
        bits = int(input('Enter the desired number of bits: '))
        with open('rsa_keys.txt', 'a+') as file:
            keys_info = generate_rsa_keys(bits, prime_generator_func)
            file.write('\n{}\n{}\n'.format(datetime.now(), keys_info))
        print('Keys generated and saved in rsa_keys.txt')
    else:
        print('Invalid method selected.')
import random
def create_rsa_key_pair():
    p = prompt_for_prime("p")
    q = prompt_for_prime("q")
    if p == q:
        print("p and q cannot be the same.")
        return create_rsa_key_pair()
    n = p * q
    f = (p - 1) * (q - 1)
    e = select_public_exponent(f)
    d = compute_private_exponent(e, f)
    save_keys(e, d, n)
def prompt_for_prime(name):
    while True:
        try:
            num = int(input(f"Enter a prime number for {name}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if num > 1 and is_prime(num):
            return num
        else:
            print("The number must be a prime number.")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def select_public_exponent(f):
    while True:
        try:
            e = int(input("Enter public exponent (e): "))
        except ValueError:
            if input("Invalid input. Generate a random value? (y/n): ").strip().lower() == 'y':
                e = generate_random_exponent(f)
                print(f"Generated public exponent e = {e}")
                return e
            continue
        if e > 1 and greatest_common_divisor(e, f) == 1:
            return e
        else:
            print(f"The number must be coprime with {f}.")
def compute_private_exponent(e, f):
    d = 1
    while (d * e) % f != 1:
        d += 1
    return d
def generate_random_exponent(f):
    while True:
        e = random.randint(2, f - 1)
        if greatest_common_divisor(e, f) == 1:
            return e
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
def save_keys(e, d, n):
    with open("id_rsa_pub.txt", "w") as pub_file:
        pub_file.write(f"[{e}, {n}]")
    with open("id_rsa.txt", "w") as priv_file:
        priv_file.write(f"[{d}, {n}]")
if __name__ == '__main__':
    create_rsa_key_pair()
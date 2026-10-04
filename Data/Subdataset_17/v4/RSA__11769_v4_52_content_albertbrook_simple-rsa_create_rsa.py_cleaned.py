import random
def create_rsa():
    p = get_prime_number("p")
    q = get_prime_number("q")
    if p == q:
        print("p and q cannot be the same.")
        return create_rsa()
    n = p * q
    f = (p - 1) * (q - 1)
    e = get_public_key(f)
    d = calculate_private_key(e, f)
    with open("id_rsa_pub.txt", "w") as pub_file:
        pub_file.write(f"[{e}, {n}]")
    with open("id_rsa.txt", "w") as priv_file:
        priv_file.write(f"[{d}, {n}]")
def get_prime_number(name):
    while True:
        try:
            num = int(input(f"Enter a prime number for {name}: "))
        except ValueError:
            print("Please enter an integer.")
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
def get_public_key(f):
    while True:
        try:
            e = int(input("Enter public exponent (e): "))
        except ValueError:
            if input("Invalid value. Do you want a random value? (y/n): ").lower() == 'y':
                e = random_public_key(f)
                print(f"Generated public exponent e = {e}")
                return e
            continue
        if e > 1 and greatest_common_divisor(e, f) == 1:
            return e
        else:
            print(f"The number must be coprime with {f}.")
def calculate_private_key(e, f):
    d = 1
    while (d * e) % f != 1:
        d += 1
    return d
def random_public_key(f):
    while True:
        e = random.randint(2, f - 1)
        if greatest_common_divisor(e, f) == 1:
            return e
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
if __name__ == '__main__':
    create_rsa()
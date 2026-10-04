import random
def create_rsa():
    p = get_prime_number("p")
    q = get_prime_number("q")
    while p == q:
        print("p and q cannot be equal")
        q = get_prime_number("q")
    n = p * q
    f = (p - 1) * (q - 1)
    e = get_public_key(f)
    d = find_mod_inverse(e, f)
    with open("id_rsa_pub.txt", "w") as file:
        file.write(f"[{e}, {n}]")
    with open("id_rsa.txt", "w") as file:
        file.write(f"[{d}, {n}]")
def get_prime_number(name):
    while True:
        try:
            num = int(input(f"{name} = "))
            if num > 1 and is_prime_number(num):
                return num
            else:
                print("Please enter a prime number.")
        except ValueError:
            print("Please enter an integer.")
def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def get_public_key(f):
    while True:
        try:
            e = int(input("e = "))
            if e > 1 and greatest_common_divisor(e, f) == 1:
                return e
            else:
                print(f"Please enter a number that is coprime with {f}.")
                if input("Do you want a random value? (y or n): ").lower() == "y":
                    return random_public_key(f)
        except ValueError:
            if input("Value wrong. Do you want a random value? (y or n): ").lower() == "y":
                return random_public_key(f)
def random_public_key(f):
    while True:
        e = random.randint(2, f - 1)
        if greatest_common_divisor(e, f) == 1:
            print(f"e = {e}")
            return e
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
def find_mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1
if __name__ == '__main__':
    create_rsa()
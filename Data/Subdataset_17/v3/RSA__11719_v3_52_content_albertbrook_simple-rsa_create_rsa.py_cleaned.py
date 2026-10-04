import random
def create_rsa():
    p = get_prime_number("p")
    q = get_prime_number("q")
    while p == q:
        print("Error: p and q cannot be the same. Please enter a different value for q.")
        q = get_prime_number("q")
    n = p * q
    f = (p - 1) * (q - 1)
    e = get_public_exponent(f)
    d = calculate_mod_inverse(e, f)
    save_keys_to_files(e, n, d)
def get_prime_number(prompt):
    while True:
        try:
            num = int(input(f"Enter a prime number for {prompt}: "))
            if is_prime(num):
                return num
            else:
                print("That number is not prime. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def get_public_exponent(f):
    while True:
        try:
            e = int(input("Enter the public exponent (e): "))
            if e > 1 and greatest_common_divisor(e, f) == 1:
                return e
            else:
                print(f"Invalid choice. {e} is not coprime with {f}.")
                if input("Would you like a random value instead? (y/n): ").strip().lower() == "y":
                    return generate_random_exponent(f)
        except ValueError:
            if input("Invalid input. Want a random value? (y/n): ").strip().lower() == "y":
                return generate_random_exponent(f)
def generate_random_exponent(f):
    while True:
        e = random.randint(2, f - 1)
        if greatest_common_divisor(e, f) == 1:
            print(f"Chosen public exponent (e) = {e}")
            return e
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
def calculate_mod_inverse(a, m):
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
def save_keys_to_files(e, n, d):
    with open("id_rsa_pub.txt", "w") as pub_file:
        pub_file.write(f"[{e}, {n}]")
    with open("id_rsa.txt", "w") as priv_file:
        priv_file.write(f"[{d}, {n}]")
if __name__ == '__main__':
    create_rsa()
 main()
import random
def is_prime(number):
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True
def generate_prime(n, m):
    prime = 0
    while not is_prime(prime):
        prime = random.randint(n, m)
    return prime
def main():
    print("---------------------------------\n----------ALGORITHME R-H---------\n---------------------------------\n")
    p = generate_prime(1000, 99999)
    print("The generated prime number P =", p)
    a = random.randint(1, p-1)
    print("The chosen number between 1 and P-1 is A =", a)
    x1 = random.randint(1, 99999)
    x2 = random.randint(1, 99999)
    print("\nThe private key x1 chosen by Alice is:", x1)
    print("The private key x2 chosen by Bob is:", x2)
    y1 = pow(a, x1, p)
    y2 = pow(a, x2, p)
    k1 = pow(y2, x1, p)
    k2 = pow(y1, x2, p)
    print("\nThe secret key K1 of Alice is:", k1)
    print("The secret key K2 of Bob is:", k2)
if __name__ == "__main__":
    main()
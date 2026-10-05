def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def generate_prime():
    while True:
        prime = int(input("Enter a prime number: "))
        if is_prime(prime):
            return prime
        else:
            print("Please enter a prime number.")
print("RSA Encryption and Decryption")
print("\nEnter two prime numbers to set up RSA encryption.")
p = generate_prime()
q = generate_prime()
n = p * q
phi = (p - 1) * (q - 1)
e = 2
while gcd(e, phi) != 1:
    e += 1
print("\nPublic key (encryption key): (e = {}, n = {})".format(e, n))
d = 10
while True:
    if (d * e) % phi == 1:
        break
    else:
        d += 1
print("Private key (decryption key): (d = {}, n = {})".format(d, n))
msg = input("\nEnter a message to encrypt (letters only): ")
alphabet = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)
encrypted_msg = [(letters.index(x) ** e) % n for x in msg]
print("\nEncrypted message: ")
print(encrypted_msg)
decrypted_msg = [letters[(x ** d) % n] for x in encrypted_msg]
print("\nDecrypted Message: ")
print(''.join(decrypted_msg))
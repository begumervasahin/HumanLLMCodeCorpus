import random
def is_prime(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True
def has_unique_elements(sequence):
    unique_elements = set(sequence)
    return len(unique_elements) == len(sequence)
def find_primitive_roots(q):
    primitive_roots = []
    for i in range(1, q):
        temp_sequence = [(i ** j) % q for j in range(1, q)]
        if has_unique_elements(temp_sequence):
            primitive_roots.append(i)
    return primitive_roots
def key_exchange():
    q = int(input('Enter a prime value for q: '))
    while not is_prime(q):
        q = int(input("Please enter a prime number only for q: "))
    primitive_roots = find_primitive_roots(q)
    print("Primitive roots are: " + str(primitive_roots))
    alpha = random.choice(primitive_roots)
    print('Selected alpha is: ' + str(alpha))
    num_communications = int(input('Enter the number of communications: '))
    private_keys = []
    for i in range(num_communications):
        private_key = int(input("Enter private key " + str(i + 1) + " (strictly less than q): "))
        while private_key >= q:
            private_key = int(input("Enter private key strictly less than q: "))
        private_keys.append(private_key)
    public_keys = [(alpha ** private_key) % q for private_key in private_keys]
    print("Public keys are: " + str(public_keys))
    person1 = int(input("Enter the first person for communication: "))
    person2 = int(input("Enter the second person for communication: "))
    while person2 == person1:
        person2 = int(input("Same person cannot be used again. Enter another: "))
    print("Key exchange for the first person...")
    k1 = (public_keys[person1 - 1] ** private_keys[person2 - 1]) % q
    print("Shared secret key for first person:", k1)
    print("Key exchange for the second person...")
    k2 = (public_keys[person2 - 1] ** private_keys[person1 - 1]) % q
    print("Shared secret key for second person:", k2)
    if k1 == k2:
        print("Key exchanges are the same. Secure communication established.")
    else:
        print("Error in key exchange. Communication may not be secure.")
if __name__ == "__main__":
    key_exchange()
import hashlib
import sys
class CustomPRNG:
    def __init__(self):
        self.index_i = 0
        self.index_j = 0
        self.index_a = 0
        self.index_w = 1
        self.permutation = [i for i in range(256)]
    def update_permutation(self):
        self.index_i = (self.index_i + self.index_w) % 256
        self.index_j = self.permutation[(self.index_j + self.permutation[self.index_i]) % 256]
        self.permutation[self.index_i], self.permutation[self.index_j] = self.permutation[self.index_j], self.permutation[self.index_i]
    def get_next_byte(self):
        self.update_permutation()
        return self.permutation[self.index_j]
    def custom_hash(self, input_data):
        self.index_i = self.index_j = self.index_a = 0
        self.index_w = 1
        for char in input_data:
            self.absorb_byte(ord(char))
        result_bytes = []
        for _ in range(32):
            result_bytes.append(self.get_next_byte())
        hash_value = 0
        for byte_value in result_bytes:
            hash_value = (hash_value << 8) + byte_value
        return hash_value
    def absorb_byte(self, byte):
        if self.index_a == 241:
            self.shuffle_permutation()
        self.permutation[self.index_a], self.permutation[240 + byte] = self.permutation[240 + byte], self.permutation[self.index_a]
        self.index_a += 1
    def shuffle_permutation(self):
        for _ in range(256):
            self.update_permutation()
        self.index_w = (self.index_w + 2) % 256
        self.index_a = 0
def elliptic_curve_addition(point_p, point_q, prime_modulus):
    x1, y1 = point_p
    x2, y2 = point_q
    if x1 == x2:
        slope = ((3 * x1 * x1 - 1) * pow(2 * y1, prime_modulus - 2, prime_modulus)) % prime_modulus
    else:
        if x1 < x2:
            x1 += prime_modulus
        slope = ((y1 - y2) * pow(x1 - x2, prime_modulus - 2, prime_modulus)) % prime_modulus
    xr = (slope * slope) - x1 - x2
    yr = slope * (x1 - xr) - y1
    return [xr % prime_modulus, yr % prime_modulus]
def elliptic_curve_multiplication(point_p, scalar_n, prime_modulus):
    result_point = 'ZERO'
    current_point = point_p
    while scalar_n != 0:
        if scalar_n % 2 != 0:
            if result_point == 'ZERO':
                result_point = current_point
            else:
                result_point = elliptic_curve_addition(result_point, current_point, prime_modulus)
        current_point = elliptic_curve_addition(current_point, current_point, prime_modulus)
        scalar_n >>= 1
    return result_point
def schnorr_signature_generation(generator_point, message, private_key, prime_modulus):
    k = prng.custom_hash(message + 'key value')
    R = elliptic_curve_multiplication(generator_point, k, prime_modulus)
    e = prng.custom_hash(str(R[0]) + message) % ((prime_modulus + 1) >> 2)
    return [(k - private_key * e) % ((prime_modulus + 1) >> 2), e]
def find_next_prime(current_prime):
    multiplier = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while gcd(current_prime, multiplier) != 1 or gcd((current_prime + 1) >> 2, multiplier) != 1:
            current_prime += 12
        if pow(7, current_prime - 1, current_prime) != 1 or pow(7, ((current_prime + 1) >> 2) - 1, (current_prime + 1) >> 2) != 1:
            current_prime += 12
            continue
        return current_prime
def num_to_hex_text(number):
    hex_chars = '0123456789abcdef'
    hex_text = ''
    while number > 0:
        hex_text = hex_chars[number % 16] + hex_text
        number >>= 4
    return hex_text
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def main():
    global prng
    prime_modulus = find_next_prime(prng.custom_hash('Franz Scheerer') % (131 * 2 ** 131))
    print("A prime greater than 2^131 \np =", prime_modulus)
    base_point_x = 1234567
    if pow(base_point_x ** 3 - base_point_x, (prime_modulus - 1) >> 1, prime_modulus) != 1:
        base_point_x = prime_modulus - base_point_x
    base_point_y = pow(base_point_x ** 3 - base_point_x, (prime_modulus + 1) >> 2, prime_modulus)
    base_point = [base_point_x % prime_modulus, base_point_y % prime_modulus]
    generator_point = elliptic_curve_multiplication(base_point, 4, prime_modulus)
    message = hashlib.sha256(sys.argv[1].encode()).hexdigest()
    private_key = prng.custom_hash('passwordX')
    print("The base point is:")
    print("x:", base_point[0])
    print("y:", base_point[1])
    public_key = elliptic_curve_multiplication(base_point, private_key, prime_modulus)
    print("The public key is the point:")
    print("x:", public_key[0])
    print("y:", public_key[1])
    signature = schnorr_signature_generation(generator_point, message, private_key, prime_modulus)
    print("The signature is:")
    print("s:", signature[0])
    print("e:", signature[1])
    R = elliptic_curve_addition(elliptic_curve_multiplication(base_point, signature[0], prime_modulus),
                                elliptic_curve_multiplication(public_key, signature[1], prime_modulus), prime_modulus)
    check = prng.custom_hash(str(R[0]) + message) % ((prime_modulus + 1) >> 2) == signature[1]
    print("\nResult of verification:", check)
    quick_brown_fox_hash = prng.custom_hash("The quick brown fox jumps over the lazy dog")
    print("Hash of 'The quick brown fox jumps over the lazy dog':")
    print("h =", num_to_hex_text(quick_brown_fox_hash))
if __name__ == "__main__":
    prng = CustomPRNG()
    main()
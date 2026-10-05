import sys
import hashlib
a241 = i241 = j241 = w241 = 0
s241 = []
def custom_hash(input_string):
    global a241, i241, j241, w241, s241
    i241 = j241 = a241 = 0
    w241 = 1
    s241 = [ix for ix in range(256)]
    for c in input_string:
        absorb_byte241(ord(c))
    res = []
    squeeze241(res, 32)
    hash_value = 0
    for bx in res:
        hash_value = (hash_value << 8) + bx
    return hash_value
def num_to_hex_text(number):
    hex_chars = '0123456789abcdef'
    hex_text = ''
    while number > 0:
        hex_text = hex_chars[number % 16] + hex_text
        number >>= 4
    return hex_text
def custom_pseudo_random_number_generator():
    global a241, i241, j241, w241, s241
    i241 = (i241 + w241) % 256
    j241 = s241[(j241 + s241[i241]) % 256]
    s241[i241], s241[j241] = s241[j241], s241[i241]
def output_byte():
    global a241, i241, j241, w241, s241
    custom_pseudo_random_number_generator()
    return s241[j241]
def shuffle_elements():
    global a241, i241, j241, w241, s241
    for _ in range(256):
        custom_pseudo_random_number_generator()
    w241 = (w241 + 2) % 256
    a241 = 0
def absorb_nibble(byte_value):
    global a241, i241, j241, w241, s241
    if a241 == 241:
        shuffle_elements()
    s241[a241], s241[240 + byte_value] = s241[240 + byte_value], s241[a241]
    a241 += 1
def absorb_byte(byte_value):
    absorb_nibble(byte_value % 16)
    absorb_nibble(byte_value >> 4)
def squeeze_bytes(output_list, output_length):
    global a241, i241, j241, w241, s241
    shuffle_elements()
    for _ in range(output_length):
        output_list.append(output_byte())
def add_points(point1, point2, prime_modulus):
    x1, x2 = point1[0], point2[0]
    y1, y2 = point1[1], point2[1]
    if x1 == x2:
        slope = ((3 * x1 * x1 - 1) * pow(2 * y1, prime_modulus - 2, prime_modulus)) % prime_modulus
    else:
        if x1 < x2:
            x1 += prime_modulus
        slope = ((y1 - y2) * pow(x1 - x2, prime_modulus - 2, prime_modulus)) % prime_modulus
    xr = (slope * slope) - x1 - x2
    yr = slope * (x1 - xr) - y1
    return [xr % prime_modulus, yr % prime_modulus]
def multiply_point(point, scalar, prime_modulus):
    result_point = 'ZERO'
    current_point = point
    while scalar != 0:
        if scalar % 2 != 0:
            if result_point == 'ZERO':
                result_point = current_point
            else:
                result_point = add_points(result_point, current_point, prime_modulus)
        current_point = add_points(current_point, current_point, prime_modulus)
        scalar >>= 1
    return result_point
def schnorr_signature_generation(generator_point, message, private_key, prime_modulus):
    k = custom_hash(message + 'key value')
    R = multiply_point(generator_point, k, prime_modulus)
    e = custom_hash(str(R[0]) + message) % ((prime_modulus + 1) >> 2)
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
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def main():
    global prime_modulus
    base_point_x = 1234567
    if pow(base_point_x ** 3 - base_point_x, (prime_modulus - 1) >> 1, prime_modulus) != 1:
        base_point_x = prime_modulus - base_point_x
    base_point_y = pow(base_point_x ** 3 - base_point_x, (prime_modulus + 1) >> 2, prime_modulus)
    base_point = [base_point_x % prime_modulus, base_point_y % prime_modulus]
    generator_point = multiply_point(base_point, 4, prime_modulus)
    message = hashlib.sha256(sys.argv[1].encode()).hexdigest()
    private_key = custom_hash('passwordX')
    print("The base point is:")
    print("x:", base_point[0])
    print("y:", base_point[1])
    public_key = multiply_point(base_point, private_key, prime_modulus)
    print("The public key is the point:")
    print("x:", public_key[0])
    print("y:", public_key[1])
    signature = schnorr_signature_generation(generator_point, message, private_key, prime_modulus)
    print("The signature is:")
    print("s:", signature[0])
    print("e:", signature[1])
    R = add_points(multiply_point(base_point, signature[0], prime_modulus),
                   multiply_point(public_key, signature[1], prime_modulus))
    check = custom_hash(str(R[0]) + message) % ((prime_modulus + 1) >> 2) == signature[1]
    print("\nResult of verification:", check)
    quick_brown_fox_hash = custom_hash("The quick brown fox jumps over the lazy dog")
    print("Hash of 'The quick brown fox jumps over the lazy dog' is:", num_to_hex_text(quick_brown_fox_hash))
if __name__ == "__main__":
    prime_modulus = find_next_prime(custom_hash('Franz Scheerer') % (131 * 2 ** 131))
    print("A prime greater than 2^131 \np =", prime_modulus)
    main()
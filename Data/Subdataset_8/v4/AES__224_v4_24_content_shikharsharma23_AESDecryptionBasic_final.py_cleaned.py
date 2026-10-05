import sys
def decrypt_message(encrypted_ints, key):
    encrypted_bytes = bytearray(encrypted_ints)
    decrypted_bytes = decrypt_bytes(encrypted_bytes, key)
    return bytes_to_string(decrypted_bytes)
def decrypt_bytes(data, key):
    key_nibbles = byte_to_nibbles(key)
    decrypted_data = bytearray()
    for byte in data:
        byte_nibbles = byte_to_nibbles(byte)
        decrypted_nibbles = decrypt_nibbles(byte_nibbles, key_nibbles)
        decrypted_data.append(nibbles_to_byte(decrypted_nibbles))
    return decrypted_data
def byte_to_nibbles(byte):
    return [(byte >> (6 - 2 * i)) & 0x03 for i in range(4)]
def nibbles_to_byte(nibbles):
    return sum(n << (6 - 2 * i) for i, n in enumerate(nibbles))
def decrypt_nibbles(nibbles, key_nibbles):
    nibbles = xor_nibbles(nibbles, key_nibbles)
    nibbles = swap_nibbles(nibbles)
    nibbles = apply_sbox(nibbles)
    nibbles = xor_nibbles(nibbles, key_nibbles)
    nibbles = subtract_nibbles(nibbles)
    nibbles = swap_nibbles(nibbles)
    nibbles = apply_sbox(nibbles)
    nibbles = xor_nibbles(nibbles, key_nibbles)
    return nibbles
def xor_nibbles(nibbles, key_nibbles):
    return [n ^ k for n, k in zip(nibbles, key_nibbles)]
def swap_nibbles(nibbles):
    nibbles[2], nibbles[3] = nibbles[3], nibbles[2]
    return nibbles
def apply_sbox(nibbles):
    s_box = {0: 2, 1: 0, 2: 3, 3: 1}
    return [s_box[n] for n in nibbles]
def subtract_nibbles(nibbles):
    return [(nibbles[i] - nibbles[i + 2]) % 4 for i in range(2)] + nibbles[2:]
def bytes_to_string(byte_array):
    return ''.join(chr(b) for b in byte_array)
def main():
    encrypted_data = [
        132, 201, 141, 74, 140, 94, 141, 140, 141, 15, 31, 164, 90, 229, 201, 141,
        78, 114, 241, 217, 141, 217, 140, 180, 141, 164, 51, 141, 188, 221, 31, 164,
        241, 177, 141, 140, 51, 217, 141, 201, 229, 152, 141, 78, 241, 114, 78, 102, 94,
        141, 74, 152, 31, 152, 141, 94, 201, 31, 164, 102, 164, 51, 90, 141, 201, 229,
        164, 31, 201, 152, 152, 51, 115
    ]
    decryption_key = 84
    decrypted_text = decrypt_message(encrypted_data, decryption_key)
    print("Decrypted text:", decrypted_text)
if __name__ == '__main__':
    main()
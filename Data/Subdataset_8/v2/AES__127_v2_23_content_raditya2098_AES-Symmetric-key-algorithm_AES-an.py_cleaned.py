
Sbox = [
]
def sbox_substitute(input_string):
    substituted_hex_values = []
    for char in input_string:
        char_hex = hex(ord(char))
        hex_value = char_hex[2:]
        substituted_hex = hex(Sbox[int(hex_value, 16)])
        substituted_hex_values.append(substituted_hex)
    substituted_string = ''.join(chr(int(hex_val, 16)) for hex_val in substituted_hex_values)
    return substituted_string
def main():
    key = 'Thats my Kung Fu'
    print(f"Length of the key: {len(key)} bytes")
    msg = 'Two One Nine Two'
    print(f"Original message: {msg}")
    print(f"Length of the message: {len(msg)} bytes")
    substituted_msg = sbox_substitute(msg)
    print(f"Message after S-box substitution: {substituted_msg}")
if __name__ == "__main__":
    main()
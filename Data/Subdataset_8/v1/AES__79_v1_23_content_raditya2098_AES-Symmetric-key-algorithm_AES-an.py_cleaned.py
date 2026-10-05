
Sbox = [
]
def sbox_substitution(input_string):
    hex_values = [hex(ord(char)) for char in input_string]
    substituted_values = [hex(Sbox[int(hex_val[2:], 16)]) for hex_val in hex_values]
    substituted_string = ''.join([chr(int(hex_val, 16)) for hex_val in substituted_values])
    return substituted_string
def main():
    key = 'Thats my Kung Fu'
    print(f"Key length: {len(key.encode('utf-8'))}")
    msg = 'Two One Nine Two'
    print(f"Original message: {msg}")
    print(f"Message length: {len(msg.encode('utf-8'))}")
    substituted_msg = sbox_substitution(msg)
    print(f"S-box substituted message: {substituted_msg}")
if __name__ == "__main__":
    main()
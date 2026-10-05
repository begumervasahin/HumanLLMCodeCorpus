
Sbox = [
]
def sbox_substitute(input_string):
    substituted_chars = []
    for char in input_string:
        ascii_val = ord(char)
        sbox_val = Sbox[ascii_val]
        substituted_char = chr(sbox_val)
        substituted_chars.append(substituted_char)
    substituted_string = ''.join(substituted_chars)
    return substituted_string
def main():
    key = 'Thats my Kung Fu'
    msg = 'Two One Nine Two'
    print(f"Key length: {len(key)} bytes")
    print(f"Original message: {msg}")
    print(f"Message length: {len(msg)} bytes")
    substituted_msg = sbox_substitute(msg)
    print(f"S-box substituted message: {substituted_msg}")
if __name__ == "__main__":
    main()
def new_ascii(ch):
    return ord(ch) + 100
def old_ascii(ascii_val):
    return int(ascii_val) - 100
def encode(msg):
    encoded_message = ''.join(str(new_ascii(ch)).zfill(3) for ch in msg)
    return encoded_message
def decode(encoded_msg):
    decoded_message = ''.join(chr(old_ascii(encoded_msg[i:i+3])) for i in range(0, len(encoded_msg), 3))
    return decoded_message
if __name__ == "__main__":
    original_message = "Hello, World!"
    print("Original Message:", original_message)
    encoded_message = encode(original_message)
    print("Encoded Message:", encoded_message)
    decoded_message = decode(encoded_message)
    print("Decoded Message:", decoded_message)
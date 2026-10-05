def new_ascii(ch):
    return ord(ch) + 100
def old_ascii(ascii_val):
    return int(ascii_val) - 100
def encode(msg):
    encoded_message = ''.join(str(new_ascii(char)) for char in msg)
    return encoded_message
def decode(new_ascii_string):
    decoded_message = ''
    for i in range(0, len(new_ascii_string), 3):
        chunk = new_ascii_string[i:i+3]
        decoded_message += chr(old_ascii(chunk))
    return decoded_message
if __name__ == "__main__":
    message = "Hello, World!"
    encoded_message = encode(message)
    print("Encoded:", encoded_message)
    decoded_message = decode(encoded_message)
    print("Decoded:", decoded_message)
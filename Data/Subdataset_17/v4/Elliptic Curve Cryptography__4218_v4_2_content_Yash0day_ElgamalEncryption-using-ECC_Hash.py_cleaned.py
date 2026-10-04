def new_ascii(char):
    return ord(char) + 100
def old_ascii(modified_ascii):
    return int(modified_ascii) - 100
def encode(message):
    encoded_message = ''.join(str(new_ascii(char)).zfill(3) for char in message)
    return encoded_message
def decode(encoded_message):
    decoded_message = ''.join(
        chr(old_ascii(encoded_message[i:i+3]))
        for i in range(0, len(encoded_message), 3)
    )
    return decoded_message
if __name__ == "__main__":
    original_message = "Hello, World!"
    print("Original Message:", original_message)
    encoded_message = encode(original_message)
    print("Encoded Message:", encoded_message)
    decoded_message = decode(encoded_message)
    print("Decoded Message:", decoded_message)
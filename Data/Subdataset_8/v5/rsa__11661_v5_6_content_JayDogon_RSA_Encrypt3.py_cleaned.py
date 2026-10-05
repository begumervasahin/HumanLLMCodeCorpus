def encrypt_message(message, exponent, modulus):
    padded_message = _pad_message_to_length_multiple(message)
    encrypted_blocks = [_encrypt_block(block, exponent, modulus) for block in _split_into_blocks(padded_message)]
    return encrypted_blocks
def _pad_message_to_length_multiple(message, block_size=3):
    while len(message) % block_size != 0:
        message += " "
    return message
def _split_into_blocks(message, block_size=3):
    return [message[i:i + block_size] for i in range(0, len(message), block_size)]
def _encrypt_block(block, exponent, modulus):
    block_value = sum((ord(char) * (1000 ** idx) for idx, char in enumerate(reversed(block))))
    return pow(block_value, exponent, modulus)
def main():
    while True:
        message = input("Enter a message here (or enter 'quit' to quit): ")
        if message.lower() == "quit":
            break
        n = int(input("Enter the modulus value (n): "))
        e = int(input("Enter the exponent value (e): "))
        encrypted_message = encrypt_message(message, e, n)
        print("Encrypted message:", encrypted_message)
if __name__ == "__main__":
    main()
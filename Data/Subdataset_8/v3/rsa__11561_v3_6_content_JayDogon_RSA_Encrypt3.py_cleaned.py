def encrypt(message, e_key, n_key):
    padded_message = pad_message(message)
    encrypted_blocks = []
    for i in range(0, len(padded_message), 3):
        block = padded_message[i:i+3]
        ascii_values = [str(ord(char)).zfill(3) for char in block]
        k = int("".join(ascii_values))
        encrypted_blocks.append(modular_exponentiation(k, e_key, n_key))
    return encrypted_blocks
def pad_message(message):
    while len(message) % 3 != 0:
        message += " "
    return message
def modular_exponentiation(base, exponent, modulus):
    binary_exponent = bin(exponent)[2:][::-1]
    powers = [base]
    for _ in range(1, len(binary_exponent)):
        powers.append((powers[-1] ** 2) % modulus)
    result = 1
    for i in range(len(binary_exponent)):
        if binary_exponent[i] == '1':
            result = (result * powers[i]) % modulus
    return result
def main():
    while True:
        message = input("Enter a message here (or enter \"quit\" to quit): ")
        if message.lower() == "quit":
            break
        n_key = int(input("Enter an n value: "))
        while True:
            try:
                e_key = int(input("Enter an e value: "))
                break
            except ValueError:
                print("Please enter an integer value")
        encrypted_message = encrypt(message, e_key, n_key)
        print(encrypted_message)
if __name__ == "__main__":
    main()
def encrypt_bit(bitlist, password):
    encrypted_bits = []
    for i in range(len(bitlist)):
        encrypted_char = ""
        for j in range(8):
            password_bit = int(password[i][j])
            bitlist_bit = int(bitlist[i][j])
            encrypted_bit = password_bit ^ bitlist_bit
            encrypted_char += str(encrypted_bit)
        encrypted_bits.append(encrypted_char)
    return encrypted_bits
def decrypt_bit(bitlist, password):
    decrypted_bits = []
    for i in range(len(bitlist)):
        password_bit = int(password[i])
        bitlist_bit = int(bitlist[i])
        decrypted_bit = password_bit ^ bitlist_bit
        decrypted_bits.append(str(decrypted_bit))
    return decrypted_bits
def group_bits(bitlist):
    grouped_bits = []
    for i in range(int(len(bitlist) / 8)):
        grouped_char = "".join(bitlist[i * 8: i * 8 + 8])
        grouped_bits.append(grouped_char)
    return grouped_bits
def main(message, password):
    message_bits = [format(ord(char), '08b') for char in message]
    password_bits = [format(ord(char), '08b') for char in password]
    encrypted_bits = encrypt_bit(message_bits, password_bits)
    encrypted_bits = encrypt_bit(encrypted_bits, password_bits)
    encrypted_message = "".join([chr(int(char, 2)) for char in encrypted_bits])
    return encrypted_message
if __name__ == "__main__":
    message = "Hello"
    password = "Password"
    encrypted_message = main(message, password)
    print("Encrypted message:", encrypted_message)
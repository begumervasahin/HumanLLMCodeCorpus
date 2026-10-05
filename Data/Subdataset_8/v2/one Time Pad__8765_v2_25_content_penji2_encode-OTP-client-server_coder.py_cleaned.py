def encrypt_bit(bitlist, password):
    encrypted_bits = []
    for i in range(len(bitlist)):
        encrypted_char = ""
        for j in range(8):
            if int(password[i][j]) == 1 and int(bitlist[i][j]) == 1:
                encrypted_char += "0"
            elif int(password[i][j]) == 1 and int(bitlist[i][j]) == 0:
                encrypted_char += "1"
            elif int(password[i][j]) == 0 and int(bitlist[i][j]) == 1:
                encrypted_char += "1"
            elif int(password[i][j]) == 0 and int(bitlist[i][j]) == 0:
                encrypted_char += "0"
        encrypted_bits.append(encrypted_char)
    return encrypted_bits
def decrypt_bit(bitlist, password):
    decrypted_bits = []
    for i in range(len(bitlist)):
        if int(password[i]) == 1 and int(bitlist[i]) == 1:
            decrypted_bits.append("0")
        elif int(password[i]) == 1 and int(bitlist[i]) == 0:
            decrypted_bits.append("1")
        elif int(password[i]) == 0 and int(bitlist[i]) == 1:
            decrypted_bits.append("1")
        elif int(password[i]) == 0 and int(bitlist[i]) == 0:
            decrypted_bits.append("0")
    return decrypted_bits
def group_bits(bitlist):
    grouped_bits = []
    for i in range(int(len(bitlist) / 8)):
        grouped_char = ""
        for j in range(8):
            grouped_char += bitlist[i * 8 + j]
        grouped_bits.append(grouped_char)
    return grouped_bits
def main(message, password):
    message_bits = [format(ord(char), '08b') for char in message]
    password_bits = [format(ord(char), '08b') for char in password]
    encrypted_bits = encrypt_bit(message_bits, password_bits)
    encrypted_bits = encrypt_bit(encrypted_bits, password_bits)
    encrypted_message = ""
    for encrypted_char in encrypted_bits:
        encrypted_char_int = int(encrypted_char, 2)
        encrypted_message += chr(encrypted_char_int)
    return encrypted_message
if __name__ == "__main__":
    message = "Hello"
    password = "Password"
    encrypted_message = main(message, password)
    print("Encrypted message:", encrypted_message)
def encrypting(bitlist, password):
    encrypted = []
    for i in range(len(bitlist)):
        encrypted_byte = ''
        for j in range(8):
            if int(password[i][j]) == 1 and int(bitlist[i][j]) == 1:
                encrypted_byte += '0'
            elif int(password[i][j]) == 1 and int(bitlist[i][j]) == 0:
                encrypted_byte += '1'
            elif int(password[i][j]) == 0 and int(bitlist[i][j]) == 1:
                encrypted_byte += '1'
            else:
                encrypted_byte += '0'
        encrypted.append(encrypted_byte)
    return encrypted
def decrypting(bitlist, password):
    encrypted = []
    for i in range(len(bitlist)):
        if int(password[i]) == 1 and int(bitlist[i]) == 1:
            encrypted.append("0")
        elif int(password[i]) == 1 and int(bitlist[i]) == 0:
            encrypted.append("1")
        elif int(password[i]) == 0 and int(bitlist[i]) == 1:
            encrypted.append("1")
        else:
            encrypted.append("0")
    encrypted_bytes = []
    for i in range(0, len(encrypted), 8):
        encrypted_bytes.append(encrypted[i:i+8])
    decrypted = ''
    for byte in encrypted_bytes:
        decrypted += chr(int(''.join(byte), 2))
    return decrypted
def main(mes, pas):
    message = mes
    password = pas
    declist = [format(ord(char), '08b') for char in message]
    paslist = [format(ord(char), '08b') for char in password]
    encrypted_msg = encrypting(declist, paslist)
    encrypted_msg_twice = encrypting(encrypted_msg, paslist)
    return ''.join(encrypted_msg_twice)
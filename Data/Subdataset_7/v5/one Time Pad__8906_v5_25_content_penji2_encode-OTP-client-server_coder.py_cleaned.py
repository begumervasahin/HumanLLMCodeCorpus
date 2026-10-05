def fonk1(byte, password_byte):
    b1 = ''
    for i in range(8):
        if int(password_byte[i]) == 1 and int(byte[i]) == 1:
            b1 += '0'
        elif int(password_byte[i]) == 1 and int(byte[i]) == 0:
            b1 += '1'
        elif int(password_byte[i]) == 0 and int(byte[i]) == 1:
            b1 += '1'
        else:
            b1 += '0'
    return b1
def fonk2(bytes_list, password_list):
    b2 = []
    for byte, password_byte in zip(bytes_list, password_list):
        b1 = fonk1(byte, password_byte)
        b2.append(b1)
    return b2
def fonk3(encrypted_bit, password_bit):
    if int(password_bit) == 1 and int(encrypted_bit) == 1:
        return '0'
    elif int(password_bit) == 1 and int(encrypted_bit) == 0:
        return '1'
    elif int(password_bit) == 0 and int(encrypted_bit) == 1:
        return '1'
    else:
        return '0'
def fonk4(b2, password_list):
    b3 = [fonk3(encrypted_bit, password_bit)
                      for encrypted_bit, password_bit in zip(b2, password_list)]
    b4 = [''.join(b3[i:i+8]) for i in range(0, len(b3), 8)]
    b5 = ''.join([chr(int(byte, 2)) for byte in b4])
    return b5
def fonk5(b11, b12):
    b6 = [format(ord(char), '08b') for char in b11]
    b7 = [format(ord(char), '08b') for char in b12]
    b8 = fonk2(b6, b7)
    b9 = fonk2(b8, b7)
    b5 = fonk4(b9, b7)
    return b5
def fonk6(b11, b12):
    return fonk5(b11, b12)
if b10 = = "__main__":
    b11 = "Hello, world!"
    b12 = "password123"
    b13 = fonk6(b11, b12)
    print("Encrypted b11:", b13)
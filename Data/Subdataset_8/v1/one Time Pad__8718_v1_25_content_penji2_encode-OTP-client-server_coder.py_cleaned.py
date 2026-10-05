def encrypting(bitlist, password):
    encrypted = [[None for _ in range(8)] for _ in range(len(bitlist))]
    encrypted1 = []
    for a in range(len(bitlist)):
        for b in range(8):
            if int(password[a][b]) == 1 and int(bitlist[a][b]) == 1:
                encrypted[a][b] = "0"
            elif int(password[a][b]) == 1 and int(bitlist[a][b]) == 0:
                encrypted[a][b] = "1"
            elif int(password[a][b]) == 0 and int(bitlist[a][b]) == 1:
                encrypted[a][b] = "1"
            elif int(password[a][b]) == 0 and int(bitlist[a][b]) == 0:
                encrypted[a][b] = "0"
    for a in range(len(bitlist)):
        c = ""
        for b in range(8):
            c += encrypted[a][b]
        encrypted1.append(c)
    return encrypted1
def decrypting(bitlist, password):
    encrypted = [None] * len(bitlist)
    encrypted1 = [[None for _ in range(8)] for _ in range(int(len(encrypted) / 8))]
    encrypted2 = []
    encrypted3 = ""
    x = 0
    for a in range(len(bitlist)):
        if int(password[a]) == 1 and int(bitlist[a]) == 1:
            encrypted[a] = "0"
        elif int(password[a]) == 1 and int(bitlist[a]) == 0:
            encrypted[a] = "1"
        elif int(password[a]) == 0 and int(bitlist[a]) == 1:
            encrypted[a] = "1"
        elif int(password[a]) == 0 and int(bitlist[a]) == 0:
            encrypted[a] = "0"
    for d in range(int(len(encrypted) / 8)):
        c = 0
        for a, b in enumerate(encrypted):
            encrypted1[d][c] = encrypted[a + x]
            c += 1
            if c == 8:
                x += 8
                break
    for a in range(int(len(encrypted) / 8)):
        c = ""
        for b in range(8):
            c += encrypted1[a][b]
        encrypted2.append(c)
    for a in encrypted2:
        c = int(a, 2)
        encrypted3 += chr(c)
    return encrypted3
def main(mes, pas):
    a = mes
    b = pas
    c = list(a)
    d = list(b)
    declist = []
    paslist = []
    for char in c:
        dec = ord(char)
        b = '{0:08b}'.format(dec)
        declist.append(b)
    for char in d:
        dec = ord(char)
        b = '{0:08b}'.format(dec)
        paslist.append(b)
    f = encrypting(declist, paslist)
    x = encrypting(f, paslist)
    encmessage = ""
    for a in x:
        x = int(a, 2)
        encmessage += chr(x)
    return encmessage
if __name__ == "__main__":
    message = "Hello"
    password = "Password"
    encrypted_message = main(message, password)
    print("Encrypted message:", encrypted_message)
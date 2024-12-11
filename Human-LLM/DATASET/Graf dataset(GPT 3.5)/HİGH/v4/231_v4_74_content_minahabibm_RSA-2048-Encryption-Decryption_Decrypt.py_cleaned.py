def fonk1(encrypted_message, b9, b8):
    return (encrypted_message ** b9) % b8
def fonk2(filename, b9, b8):
    b1 = ""
    with open(filename, "r") as f:
        b2 = [line.rstrip('\n') for line in f]
    for line in b2:
        b3 = fonk1(int(line), int(b9), int(b8))
        b1 += chr(b3)
    return b1
def fonk3(filename, b9, b8):
    b4 = []
    with open(filename, "r") as f:
        b2 = f.readlines()
    for line in b2:
        b5 = int(line.strip())
        b6 = fonk1(b5, int(b9), int(b8))
        b4.append(b6)
    with open("Decrypted_File", "wb") as fw:
        for value in b4:
            fw.write(bytes([value]))
def fonk4():
    b7 = input("Enter 1 to decrypt a message from a file, or 2 to decrypt a file: ")
    b8 = input("Enter Modulo (public key): ")
    b9 = input("Enter Private Key: ")
    if b7 = = '1':
        b1 = fonk2("Encrypted_Message.txt", b9, b8)
        print("Decrypted Message:", b1)
        with open("Decrypted_Message.txt", "w") as fw:
            fw.write(b1)
    elif b7 = = '2':
        fonk3("Encrypted_File.txt", b9, b8)
        print("File decrypted and saved as 'Decrypted_File'.")
if b10 = = "__main__":
    fonk4()
def fonk1(encrypted_message, b9, b8):
    return (encrypted_message ** b9) % b8
def fonk2(filename, b9, b8):
    b1 = ""
    with open(filename, "r") as file:
        b2 = [line.rstrip('\n') for line in file]
    for line in b2:
        b3 = fonk1(int(line), int(b9), int(b8))
        b1 += chr(b3)
    return b1
def fonk3(filename, b9, b8):
    b4 = []
    with open(filename, "r") as file:
        b2 = file.readlines()
    for line in b2:
        b5 = int(line.strip())
        b6 = fonk1(b5, int(b9), int(b8))
        b4.append(b6)
    with open("Decrypted_File", "wb") as output_file:
        for value in b4:
            output_file.write(bytes([value]))
def fonk4():
    b7 = input("Enter 1 to decrypt a message from a text file, or 2 to decrypt a binary file: ")
    b8 = input("Enter Modulo (public key): ")
    b9 = input("Enter Private Key: ")
    if b7 = = '1':
        b10 = fonk2("Encrypted_Message.txt", b9, b8)
        print("Decrypted Message:", b10)
        with open("Decrypted_Message.txt", "w") as file:
            file.write(b10)
    elif b7 = = '2':
        fonk3("Encrypted_File.txt", b9, b8)
        print("File decrypted and saved as 'Decrypted_File'.")
if b11 = = "__main__":
    fonk4()
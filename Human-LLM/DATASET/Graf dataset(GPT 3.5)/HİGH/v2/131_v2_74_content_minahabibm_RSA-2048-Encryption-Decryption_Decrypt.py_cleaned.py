
def fonk1(encrypted_message, b4, b3):
    return (encrypted_message ** b4) % b3
def fonk2():
    b1 = []
    b2 = []
    b3 = int(input("Enter Modulo: "))
    b4 = int(input("Enter Private Key: "))
    with open("Encrypted_Message.txt", "r") as file:
        b5 = [line.rstrip('\n') for line in file]
    for line in b5:
        b1.append(int(line))
    for encrypted_message in b1:
        b2.append(fonk1(encrypted_message, b4, b3))
    b6 = "".join(chr(char_code) for char_code in b2)
    print("Decrypted Message:", b6)
    with open("Decrypted_Message.txt", "w") as decrypted_file:
        decrypted_file.write(b6)
def fonk3():
    b7 = []
    b8 = []
    b3 = int(input("Enter Modulo: "))
    b4 = int(input("Enter Private Key: "))
    with open("Encrypted_File.txt", "r") as file:
        b5 = file.readlines()
    for line in b5:
        b7.append(int(line.strip()))
    for encrypted_integer in b7:
        b8.append(fonk1(encrypted_integer, b4, b3))
    with open("Decrypted_File.txt", "wb") as decrypted_file:
        decrypted_file.write(bytes(b8))
def fonk4():
    b9 = input("Enter 1 to decrypt a message from a file, or 2 to decrypt a file: ")
    if b9 = = '1':
        fonk2()
    elif b9 = = '2':
        fonk3()
    else:
        print("Invalid b9. Please enter either 1 or 2.")
if b10 = = "__main__":
    fonk4()
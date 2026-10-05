def fonk1(encrypted_data, b2, b1):
    return (encrypted_data ** b2) % b1
def fonk2():
    b1 = int(input("Enter Modulo: "))
    b2 = int(input("Enter Private Key: "))
    with open("Encrypted_Message.txt", "r") as file:
        b3 = [int(line.strip()) for line in file]
    b4 = ''.join(chr(fonk1(encrypted, b2, b1)) for encrypted in b3)
    print("Decrypted Message:", b4)
    with open("Decrypted_Message.txt", "w") as decrypted_file:
        decrypted_file.write(b4)
def fonk3():
    b1 = int(input("Enter Modulo: "))
    b2 = int(input("Enter Private Key: "))
    with open("Encrypted_File.txt", "r") as file:
        b3 = [int(line.strip()) for line in file]
    b5 = [fonk1(encrypted, b2, b1) for encrypted in b3]
    with open("Decrypted_File.txt", "wb") as decrypted_file:
        decrypted_file.write(bytes(b5))
def fonk4():
    b6 = input("Enter 1 to decrypt a message from a file, or 2 to decrypt a file: ")
    if b6 = = '1':
        fonk2()
    elif b6 = = '2':
        fonk3()
    else:
        print("Invalid b6. Please enter either 1 or 2.")
if b7 = = "__main__":
    fonk4()
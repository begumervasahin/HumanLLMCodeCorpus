def fonk1():
    b1 = input("Enter the character: ")
    b2 = input("Enter the b2: ")
    if len(b1) != 1 or len(b2) != 1:
        print("Error: Please enter a single character for both b1 and b2.")
        return
    b3 = ord(b1) + ord(b2)
    b4 = chr(b3)
    print(f"Encrypted character: {b4}")
def fonk2():
    b5 = input("Enter the b5 text: ")
    b2 = input("Enter the b2: ")
    if len(b5) != 1 or len(b2) != 1:
        print("Error: Please enter a single character for both b5 and b2.")
        return
    b6 = ord(b5) - ord(b2)
    b7 = chr(b6)
    print(f"The decrypted message is: {b7}")
def fonk3():
    while True:
        b8 = input("Press 1 to encrypt\nPress 2 to decrypt\nPress 0 to exit\nEnter your b8: ")
        if b8 = = '1':
            fonk1()
        elif b8 = = '2':
            fonk2()
        elif b8 = = '0':
            print("Project exited")
            break
        else:
            print("Invalid b8. Please enter 1, 2, or 0.")
if b9 = = '__main__':
    fonk3()
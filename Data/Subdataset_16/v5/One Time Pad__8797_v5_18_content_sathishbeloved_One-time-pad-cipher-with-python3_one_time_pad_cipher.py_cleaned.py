def fonk1():
    b1 = input("Enter the character: ")
    b2 = input("Enter the b2: ")
    if len(b1) != 1 or len(b2) != 1:
        print("Error: Both inputs should be single characters.")
        return
    b3 = ord(b1) + ord(b2)
    b4 = chr(b3)
    print(f"Cipher text: {b4}")
def fonk2():
    b4 = input("Enter the b4 text: ")
    b2 = input("Enter the b2: ")
    if len(b4) != 1 or len(b2) != 1:
        print("Error: Both inputs should be single characters.")
        return
    b5 = ord(b4) - ord(b2)
    b6 = chr(b5)
    print(f"The message is: {b6}")
def fonk3():
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("0. Exit")
        try:
            b7 = int(input("Your b7: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if b7 = = 1:
            fonk1()
        elif b7 = = 2:
            fonk2()
        elif b7 = = 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid b7. Please try again.")
if b8 = = "__main__":
    fonk3()
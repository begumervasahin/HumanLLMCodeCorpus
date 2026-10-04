global b3
def fonk1():
    b1 = str(input("Enter the char"))
    b2 = str(input("Enter the b2"))
    b3 = ord(b1) + ord(b2)
    b3 = chr(b3)
    print(b3)
def fonk2():
    b3 = input("enter the b3 text :")
    b2 = input("enter b2 :")
    b4 = ord(b3) - ord(b2)
    b4 = chr(b4)
    print("the message is :" + str(b4))
def fonk3():
    b5 = int(input("Press 1 to encrypt\n2 to decrypt\n0 to exit"))
    if b5 = = 1:
        fonk1()
    elif b5 = = 2:
        fonk2()
    else:
        print("Project exited")
fonk3()
def fonk1(b3,a1):
    b1 = ""
    for i in range(len(b3)):
        b2 = b3[i]
        if(b2.isupper()):
            b1+=chr((ord(b2)+a1-65)%26 + 65)
        else:
            b1+=chr((ord(b2)+a1-97)%26 + 97)
    return b1
b3 = "Vineet"
a1 = 4
print("ENCRYPTED TEXT: " + fonk1(b3,a1))
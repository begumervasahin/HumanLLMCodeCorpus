import base64
def fonk1(file_path):
    with open(file_path, "rb") as image_file:
        b1 = base64.b64encode(image_file.read())
    return b1.decode('utf-8')
def fonk2(b1, b4):
    b2 = base64.b64decode(b1.encode('utf-8'))
    with open(b4, 'wb') as image_file:
        image_file.write(b2)
def fonk3():
    b3 = "rode_in_club.png"
    b4 = "new_rode_in_club.png"
    b1 = fonk1(b3)
    print("Base64 Encoded String:")
    print(b1)
    b5 = int.from_bytes(base64.b64decode(b1), "big")
    print("\nEncoded Integer:")
    print(b5)
    fonk2(b1, b4)
if b6 = = "__main__":
    fonk3()
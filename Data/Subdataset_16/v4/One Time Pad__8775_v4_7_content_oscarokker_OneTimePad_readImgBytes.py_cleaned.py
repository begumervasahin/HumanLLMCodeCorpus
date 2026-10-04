import base64
def fonk1(file_path):
    with open(file_path, "rb") as image_file:
        b1 = base64.b64encode(image_file.read())
    return b1
def fonk2(b1, b4):
    b2 = base64.b64decode(b1)
    with open(b4, 'wb') as image_file:
        image_file.write(b2)
def fonk3():
    b3 = "rode_in_club.png"
    b4 = "new_rode_in_club.png"
    b1 = fonk1(b3)
    print(b1)
    b5 = int.from_bytes(b1, "big")
    print(b5)
    fonk2(b1, b4)
if b6 = = "__main__":
    fonk3()
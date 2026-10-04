import base64
def fonk1():
    with open("rode_in_club.png", "rb") as imageFile:
        b1 = base64.b64encode(imageFile.read())
        print(b1)
        b2 = int.from_bytes(b1, "big")
        print(b2)
        b3 = base64.b64decode(b1)
        with open("new_rode_in_club.png", "wb") as f:
            f.write(b3)
if b4 = = "__main__":
    fonk1()
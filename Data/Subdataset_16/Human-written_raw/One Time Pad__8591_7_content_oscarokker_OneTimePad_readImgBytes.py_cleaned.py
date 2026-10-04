import base64
with open("rode_in_club.png", "rb") as imageFile:
    b1 = base64.b64encode(imageFile.read())
    print(b1)
    print(int.from_bytes(b1, "big"))
    b2 = base64.b64decode(b1)
    b3 = "new_rode_in_club.png"
    with open(b3, 'wb') as f:
        f.write(b2)
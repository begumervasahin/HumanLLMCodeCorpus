import base64
with open("rode_in_club.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)
    print(int.from_bytes(str, "big"))
    pic = base64.b64decode(str)
    filename = "new_rode_in_club.png"
    with open(filename, 'wb') as f:
        f.write(pic)
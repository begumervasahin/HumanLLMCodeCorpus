import base64
def fonk1(file_path: str) -> bytes:
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read())
def fonk2(b4: bytes) -> int:
    return int.from_bytes(b4, "big")
def fonk3(b4: bytes, output_path: str) -> None:
    b1 = base64.b64decode(b4)
    with open(output_path, "wb") as output_file:
        output_file.write(b1)
def fonk4() -> None:
    b2 = "rode_in_club.png"
    b3 = "new_rode_in_club.png"
    b4 = fonk1(b2)
    print(f"Encoded Base64 String: {b4}")
    b5 = fonk2(b4)
    print(f"Encoded Integer: {b5}")
    fonk3(b4, b3)
    print(f"Image saved to {b3}")
if b6 = = "__main__":
    fonk4()
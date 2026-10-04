import base64
def main():
    with open("rode_in_club.png", "rb") as imageFile:
        encoded_string = base64.b64encode(imageFile.read())
        print(encoded_string)
        encoded_integer = int.from_bytes(encoded_string, "big")
        print(encoded_integer)
        decoded_bytes = base64.b64decode(encoded_string)
        with open("new_rode_in_club.png", "wb") as f:
            f.write(decoded_bytes)
if __name__ == "__main__":
    main()
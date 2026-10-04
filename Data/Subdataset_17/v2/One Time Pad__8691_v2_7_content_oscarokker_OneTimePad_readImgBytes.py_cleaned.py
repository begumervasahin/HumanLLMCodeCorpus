import base64
def encode_image_to_base64(file_path: str) -> bytes:
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read())
def base64_to_integer(encoded_string: bytes) -> int:
    return int.from_bytes(encoded_string, "big")
def decode_base64_to_image(encoded_string: bytes, output_path: str) -> None:
    decoded_bytes = base64.b64decode(encoded_string)
    with open(output_path, "wb") as output_file:
        output_file.write(decoded_bytes)
def main() -> None:
    input_image_path = "rode_in_club.png"
    output_image_path = "new_rode_in_club.png"
    encoded_string = encode_image_to_base64(input_image_path)
    print(encoded_string)
    encoded_integer = base64_to_integer(encoded_string)
    print(encoded_integer)
    decode_base64_to_image(encoded_string, output_image_path)
if __name__ == "__main__":
    main()
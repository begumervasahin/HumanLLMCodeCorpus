import base64
def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string
def decode_base64_to_image(encoded_string, output_file_path):
    decoded_image = base64.b64decode(encoded_string)
    with open(output_file_path, 'wb') as image_file:
        image_file.write(decoded_image)
def main():
    input_file_path = "rode_in_club.png"
    output_file_path = "new_rode_in_club.png"
    encoded_string = encode_image_to_base64(input_file_path)
    print(encoded_string)
    encoded_integer = int.from_bytes(encoded_string, "big")
    print(encoded_integer)
    decode_base64_to_image(encoded_string, output_file_path)
if __name__ == "__main__":
    main()
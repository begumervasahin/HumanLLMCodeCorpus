import sys
def convert_text_to_array(plain_text):
    return [ord(char) for char in plain_text]
def separate_into_digits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num
    return digits
def convert_to_separated_array(num_array):
    sep_array = []
    for num in num_array:
        sep_array.extend(separate_into_digits(num))
    return sep_array
def encrypt(plain_array, pad_array):
    return [(plain + pad) % 10 for plain, pad in zip(plain_array, pad_array)]
def decrypt(encrypted_array, pad_array):
    decrypted = []
    for i in range(0, len(encrypted_array), 3):
        value = sum((encrypted_array[i + j] - pad_array[i + j] + 10) % 10 * 10**(2-j) for j in range(3))
        decrypted.append(value)
    return decrypted
def main():
    if len(sys.argv) != 4:
        sys.exit("Error: Incorrect number of arguments")
    operation, input_file, pad_file = sys.argv[1:]
    try:
        with open(input_file) as message_file:
            plain_text = message_file.read()
    except IOError:
        sys.exit("Error: Cannot open message file")
    try:
        with open(pad_file) as pad_file:
            pad_list = pad_file.read()
    except IOError:
        sys.exit("Error: Cannot open pad file")
    pad_array = [int(char) for char in pad_list if char.isdigit()]
    if operation == "encrypt":
        num_array = convert_text_to_array(plain_text)
        if len(pad_array) < len(num_array):
            sys.exit("Error: Pad is shorter than numeric version of message")
        encrypted = encrypt(num_array, pad_array)
        output_file = f"encrypted_{input_file}"
        final_message = "".join(map(str, encrypted)) + "\n"
    elif operation == "decrypt":
        encrypted = [int(char) for char in plain_text if char.isdigit()]
        if len(pad_array) < len(encrypted):
            sys.exit("Error: Pad is shorter than numeric version of message")
        decrypted = decrypt(encrypted, pad_array)
        output_file = f"decrypted_{input_file}"
        final_message = "".join(map(chr, decrypted))
    else:
        sys.exit("Error: Incorrect command, must be 'encrypt' or 'decrypt'")
    with open(output_file, "w+") as outfile:
        outfile.write(final_message)
if __name__ == "__main__":
    main()
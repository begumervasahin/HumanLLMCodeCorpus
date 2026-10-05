import random
message = "this is an ultra secret message:"
message_and_extra = len(message) + 10000
alphabet_to_number = {" ": 0, **{char: i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}, ":": 27}
number_to_alphabet = {0: " ", **{i + 1: char for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}, 27: ":"}
def generate_one_time_pad(length):
    return [random.randint(0, 27) for _ in range(length)]
def encrypt_message(message, one_time_pad):
    message_numbers = [alphabet_to_number.get(char, 0) for char in message]
    encrypted_message = [(message_numbers[i] + one_time_pad[i]) % 28 for i in range(len(message))]
    encrypted_message.extend(one_time_pad[len(message):])
    return encrypted_message
def decrypt_message(encrypted_message, one_time_pad):
    decrypted_message = [(encrypted_message[i] - one_time_pad[i]) % 28 for i in range(len(encrypted_message))]
    return decrypted_message
def convert_to_characters(numbers):
    decrypted_characters = [number_to_alphabet[number] for number in numbers]
    return "".join(decrypted_characters)
def main():
    one_time_pad = generate_one_time_pad(message_and_extra)
    encrypted_message = encrypt_message(message, one_time_pad)
    print("Encrypted message:\n", encrypted_message)
    decrypted_message = decrypt_message(encrypted_message, one_time_pad)
    print("\nDecrypted message:\n", decrypted_message)
    decrypted_characters = convert_to_characters(decrypted_message)
    print("\nDecrypted message as characters:\n", decrypted_characters)
if __name__ == "__main__":
    main()
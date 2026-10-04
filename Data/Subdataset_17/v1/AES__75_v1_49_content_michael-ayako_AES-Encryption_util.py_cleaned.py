import logging
import random
def setup_logger():
    logging.info("Configuring logger...")
    try:
        filename = "./chatterbot/logs%s.log" % ((__file__).split(".")[0])
        logging.basicConfig(filename=filename, format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logging.info("Logger configured...")
    except Exception as err:
        logging.error("Logging not configured: %s", err)
def check_file_exists(filename):
    try:
        with open(filename, 'rb') as file:
            pass
        logging.info("File %s was found", filename)
    except Exception as err:
        logging.error("File check failed: %s", err)
        exit()
def generate_key():
    print("Please select a random word from the list and share it with the receiver of this file by typing the number adjacent to the word")
    keys = [random.randint(10000, 65535) for _ in range(6)]
    for idx, key in enumerate(keys):
        print(f"[{idx}] - {key}")
    try:
        selected_key_index = int(input())
        return keys[selected_key_index]
    except Exception as err:
        logging.error("Key generation failed: %s", err)
        exit()
def convert_to_encrypted_file(bits_matrix):
    bits_temp = [''.join(map(str, row)) for matrix in bits_matrix for row in matrix]
    chars = [chr(int(bits, 2)) for bits in bits_temp]
    with open('msg.enc', 'w', encoding='utf-8') as file:
        file.write(''.join(chars))
def convert_to_decrypted_file(bits_matrix):
    bits_temp = [''.join(map(str, row)) for matrix in bits_matrix for row in matrix]
    chars = [chr(int(bits, 2)) for bits in bits_temp]
    with open('msg.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(chars))
def quit_program():
    logging.info("Quitting")
    exit()
if __name__ == "__main__":
    setup_logger()
    filename = "example.txt"
    check_file_exists(filename)
    key = generate_key()
    print(f"Generated key: {key}")
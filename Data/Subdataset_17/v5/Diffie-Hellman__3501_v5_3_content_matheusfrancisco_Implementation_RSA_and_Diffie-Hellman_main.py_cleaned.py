
from rsa import RSA
from convertN2T import str2num, num2block, block2num, num2str
def read_original_message(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
        return None
def display_section(title, content):
    print(f'\n================== {title} ======================')
    if isinstance(content, list):
        for item in content:
            print(item)
    else:
        print(content)
def main():
    print('================== - Criptografia RSA - ======================')
    block_size = 15
    rsa = RSA()
    original_message = read_original_message("original_msg")
    if original_message is None:
        return
    display_section("Original Message", original_message)
    num_list = str2num(original_message)
    display_section("Number Representation", num_list)
    blocks = num2block(num_list, block_size)
    encrypted_blocks = rsa.encryption(blocks)
    display_section("Encrypted Blocks", encrypted_blocks)
    decrypted_blocks = rsa.decryption(encrypted_blocks)
    num_list = block2num(decrypted_blocks, block_size)
    display_section("Decrypted Number Representation", num_list)
    decrypted_message = num2str(num_list)
    display_section("Decrypted Message", decrypted_message)
if __name__ == '__main__':
    main()
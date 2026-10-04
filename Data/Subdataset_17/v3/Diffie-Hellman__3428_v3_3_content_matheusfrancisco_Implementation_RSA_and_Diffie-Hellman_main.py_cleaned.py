
from rsa import RSA
from convertN2T import str2num, num2block, block2num, num2str
def read_original_message(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
        return None
def main():
    print('================== - Criptografia RSA - ======================')
    block_size = 15
    rsa = RSA()
    original_message = read_original_message("original_msg")
    if original_message is None:
        return
    print('================== Original Message ======================')
    print(original_message)
    num_list = str2num(original_message)
    print('\n================== Number Representation ======================')
    print(num_list)
    blocks = num2block(num_list, block_size)
    encrypted_blocks = rsa.encryption(blocks)
    print("\n================== Encrypted Blocks ======================")
    print(encrypted_blocks)
    decrypted_blocks = rsa.decryption(encrypted_blocks)
    num_list = block2num(decrypted_blocks, block_size)
    print('\n================== Decrypted Number Representation ======================')
    print(num_list)
    decrypted_message = num2str(num_list)
    print('\n================== Decrypted Message ======================')
    print(decrypted_message)
if __name__ == '__main__':
    main()
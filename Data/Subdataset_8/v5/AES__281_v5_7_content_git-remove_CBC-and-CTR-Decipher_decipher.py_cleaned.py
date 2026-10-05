import argparse
from Crypto.Cipher import AES
from util_function import *
MODE_CBC = 1
MODE_CTR = 0
def split_cipher_text(cipher_text):
    if len(cipher_text) % 32 != 0:
        raise Exception("Cipher text in CBC mode should be padded into multiples of 32!")
    return [cipher_text[i:i+32] for i in range(0, len(cipher_text), 32)]
def eliminate_PKCS5_padding(text):
    last_byte = int(text[-2:], 16)
    return text[:-last_byte * 2]
def CBC_decipher(key, cipher_text, IV):
    cipher_text_blocks = split_cipher_text(cipher_text)
    middle_level = []
    aes_cipher = AES.new(bytes.fromhex(key))
    for block in reversed(cipher_text_blocks):
        current_text = bytes.fromhex(block)
        aes_decipher_result = aes_cipher.decrypt(current_text).hex()
        middle_level.append(aes_decipher_result)
    plain_text = ''
    for i, block in enumerate(middle_level):
        previous_block = IV if i == 0 else cipher_text_blocks[i - 1]
        plain_text += hexxor(previous_block, block)
    print_ascii(eliminate_PKCS5_padding(plain_text))
def CTR_decipher(key, cipher_text, IV):
    aes_cipher = AES.new(bytes.fromhex(key))
    num_blocks = (len(cipher_text)
    decrypted_text = ""
    for i in range(num_blocks):
        counter = hex(int(IV, 16) + i)[2:]
        encrypted_counter = aes_cipher.encrypt(bytes.fromhex(counter)).hex()
        decrypted_text += encrypted_counter
    print_ascii(hexxor(decrypted_text, cipher_text))
def main():
    parser = argparse.ArgumentParser(description='Decrypt AES encrypted text.')
    parser.add_argument('--mode', type=str, help='Mode of operation: CBC or CTR (default is CBC)')
    args = parser.parse_args()
    mode = MODE_CBC if args.mode != 'CTR' else MODE_CTR
    key = input("Enter the key: ")
    cipher_text = input("Enter the cipher text: ")
    IV = cipher_text[:32]
    cipher_text = cipher_text[32:]
    if mode == MODE_CBC:
        CBC_decipher(key, cipher_text, IV)
    else:
        CTR_decipher(key, cipher_text, IV)
if __name__ == "__main__":
    main()
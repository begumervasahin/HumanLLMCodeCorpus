import argparse
from Crypto.Cipher import AES
from util_function import hexxor, print_ascii
MODE_CBC = 1
MODE_CTR = 0
def split_cipher_text(cipher_text):
    if len(cipher_text) % 32 != 0:
        raise ValueError("Cipher text in CBC mode should be padded to a multiple of 32!")
    block_num = len(cipher_text)
    return [cipher_text[32 * i: 32 * (i + 1)] for i in range(block_num)]
def eliminate_PKCS5_padding(text):
    last_byte = int(text[-2], 16)
    padding_size = last_byte * 2
    return text[:-padding_size]
def CBC_decipher(key, cipher_text, IV):
    cipher_text_blocks = split_cipher_text(cipher_text)
    intermediate_results = []
    plain_text = ''
    aes_cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    for block in reversed(cipher_text_blocks):
        decrypted_block = aes_cipher.decrypt(bytes.fromhex(block)).hex()
        intermediate_results.append(decrypted_block)
    for i, intermediate_block in enumerate(reversed(intermediate_results)):
        if i == 0:
            previous_block = IV
        else:
            previous_block = cipher_text_blocks[i - 1]
        plain_text += hexxor(previous_block, intermediate_block)
    print_ascii(eliminate_PKCS5_padding(plain_text))
def CTR_decipher(key, cipher_text, IV):
    aes_cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    block_count = len(cipher_text)
    decrypted_stream = ""
    for i in range(block_count):
        counter = hex(int(IV, 16) + i)[2:].zfill(32)
        encrypted_counter = aes_cipher.encrypt(bytes.fromhex(counter)).hex()
        decrypted_stream += encrypted_counter
    print_ascii(hexxor(decrypted_stream, cipher_text))
def main():
    parser = argparse.ArgumentParser(description='AES Decryption Tool')
    parser.add_argument('--mode', type=str, help='Decryption mode: CBC or CTR')
    args = parser.parse_args()
    mode = MODE_CBC if args.mode is None or args.mode.upper() == 'CBC' else MODE_CTR
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
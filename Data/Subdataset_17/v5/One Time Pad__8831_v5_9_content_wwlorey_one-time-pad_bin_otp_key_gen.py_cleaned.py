import codecs
import sys
from os import urandom
DEFAULT_OUTPUT_FILE_NAME = 'keyfile.sec'
NUM_OTP_KEYS = 500
OTP_BIT_LEN = 2048
OTP_BYTE_LEN = OTP_BIT_LEN
def get_bin_str(byte):
    bit_str = bin(byte)[2:]
    return '0' * (8 - len(bit_str)) + bit_str
def calculate_key_id_length(num_keys):
    key_id_len = 0
    while num_keys:
        num_keys
        key_id_len += 1
    return key_id_len
def generate_otp_keys(output_file_name, num_keys, byte_len):
    key_id_len = calculate_key_id_length(num_keys)
    format_str = f"{{:0{key_id_len}d}}"
    with codecs.open(output_file_name, 'w', encoding='utf8') as output_file:
        for key_count in range(num_keys):
            key_id = format_str.format(key_count + 1)
            key_bytes = urandom(byte_len)
            key_bits = ''.join(get_bin_str(byte) for byte in key_bytes)
            output_file.write(f"{key_id} {key_bits}")
            if key_count < num_keys - 1:
                output_file.write('\n')
        print('Keys written to', output_file_name)
if __name__ == '__main__':
    output_file_name = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_OUTPUT_FILE_NAME
    generate_otp_keys(output_file_name, NUM_OTP_KEYS, OTP_BYTE_LEN)
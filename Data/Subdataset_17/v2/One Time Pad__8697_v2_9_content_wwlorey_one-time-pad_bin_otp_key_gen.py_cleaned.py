import codecs
import os
import sys
DEFAULT_OUTPUT_FILE_NAME = 'keyfile.sec'
NUM_OTP_KEYS = 500
OTP_BIT_LEN = 2048
OTP_BYTE_LEN = OTP_BIT_LEN
def get_bin_str(byte):
    return f"{byte:08b}"
def generate_keys(output_file_name):
    key_id_len = len(str(NUM_OTP_KEYS))
    with codecs.open(output_file_name, 'w', encoding='utf8') as output_file:
        for key_count in range(NUM_OTP_KEYS):
            key_id = f"{key_count + 1:0{key_id_len}d}"
            key_bytes = os.urandom(OTP_BYTE_LEN)
            key_bits = ''.join(get_bin_str(byte) for byte in key_bytes)
            output_file.write(f"{key_id} {key_bits}\n")
    print(f"Keys written to {output_file_name}")
if __name__ == '__main__':
    output_file_name = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_OUTPUT_FILE_NAME
    generate_keys(output_file_name)
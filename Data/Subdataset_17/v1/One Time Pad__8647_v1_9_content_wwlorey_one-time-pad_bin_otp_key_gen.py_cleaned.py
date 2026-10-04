import codecs
import urandom
import sys
DEFAULT_OUTPUT_FILE_NAME = 'keyfile.sec'
NUM_OTP_KEYS = 500
OTP_BIT_LEN = 2048
OTP_BYTE_LEN = OTP_BIT_LEN
def get_bin_str(char):
    bit_str = bin(char)[2:]
    return '0' * (8 - len(bit_str)) + bit_str
if __name__ == '__main__':
    if len(sys.argv) == 2:
        output_file_name = sys.argv[1]
    else:
        output_file_name = DEFAULT_OUTPUT_FILE_NAME
    key_id_len = 0
    num_otp_keys_copy = NUM_OTP_KEYS
    while num_otp_keys_copy:
        num_otp_keys_copy = num_otp_keys_copy
        key_id_len += 1
    format_str = "{:0" + str(key_id_len) + "d}"
    with codecs.open(output_file_name, 'w', encoding='utf8') as output_file:
        for key_count in range(NUM_OTP_KEYS):
            key_id = format_str.format(key_count + 1)
            key_bytes = urandom(OTP_BYTE_LEN)
            key_bits = ''.join(get_bin_str(char) for char in key_bytes)
            output_file.write(key_id + ' ' + key_bits)
            if key_count < NUM_OTP_KEYS - 1:
                output_file.write('\n')
        print('Key written to', output_file_name)
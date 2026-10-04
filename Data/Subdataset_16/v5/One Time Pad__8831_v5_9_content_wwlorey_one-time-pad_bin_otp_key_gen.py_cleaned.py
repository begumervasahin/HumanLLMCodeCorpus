import codecs
import sys
from os import urandom
b1 = 'keyfile.sec'
a1 = 500
a2 = 2048
b2 = a2
def fonk1(byte):
    b3 = bin(byte)[2:]
    return '0' * (8 - len(b3)) + b3
def fonk2(num_keys):
    a3 = 0
    while num_keys:
        num_keys
        a3 += 1
    return a3
def fonk3(b10, num_keys, byte_len):
    a3 = fonk2(num_keys)
    b4 = f"{{:0{a3}d}}"
    with codecs.open(b10, 'w', b5 = 'utf8') as output_file:
        for key_count in range(num_keys):
            b6 = b4.format(key_count + 1)
            b7 = urandom(byte_len)
            b8 = ''.join(fonk1(byte) for byte in b7)
            output_file.write(f"{b6} {b8}")
            if key_count < num_keys - 1:
                output_file.write('\n')
        print('Keys written to', b10)
if b9 = = '__main__':
    b10 = sys.argv[1] if len(sys.argv) == 2 else b1
    fonk3(b10, a1, b2)
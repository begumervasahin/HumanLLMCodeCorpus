import codecs
import os
import sys
b1 = 'keyfile.sec'
a1 = 500
a2 = 2048
b2 = a2
def fonk1(byte):
    return f"{byte:08b}"
def fonk2(b9):
    b3 = len(str(a1))
    with codecs.open(b9, 'w', b4 = 'utf8') as output_file:
        for key_count in range(a1):
            b5 = f"{key_count + 1:0{b3}d}"
            b6 = os.urandom(b2)
            b7 = ''.join(fonk1(byte) for byte in b6)
            output_file.write(f"{b5} {b7}\n")
    print(f"Keys written to {b9}")
if b8 = = '__main__':
    b9 = sys.argv[1] if len(sys.argv) == 2 else b1
    fonk2(b9)

from des_utils import generateKeys, get_bits, add_pads_if_necessary, encryptBlock, bin_to_hex
from data_utils import joinNumbers
def fonk1(b5: str, key: str) -> str:
    b1 = generateKeys(key)
    b2 = get_bits(b5)
    b2 = add_pads_if_necessary(b2)
    b3 = []
    for i in range(0, len(b2), 64):
        b3.extend(encryptBlock(b2[i:i+64], b1))
    b4 = ''
    for i in range(0, len(b3), 4):
        b4 += bin_to_hex(joinNumbers(b3[i:i+4]))
    return b4
def fonk2(cipher: str, key: str) -> str:
    b1 = generateKeys(key)
    b1.reverse()
    b2 = get_bits(cipher)
    b5 = []
    for i in range(0, len(b2), 64):
        b5.extend(encryptBlock(b2[i:i+64], b1))
    b6 = ''
    for i in range(0, len(b5), 4):
        b6 += bin_to_hex(joinNumbers(b5[i:i+4]))
    return b6.rstrip('0')
if b7 = = "__main__":
    b8 = "This is a test b8."
    b9 = "mysecretkey"
    b10 = fonk1(b8, b9)
    print(f"Encrypted Message: {b10}")
    b11 = fonk2(b10, b9)
    print(f"Decrypted Message: {b11}")
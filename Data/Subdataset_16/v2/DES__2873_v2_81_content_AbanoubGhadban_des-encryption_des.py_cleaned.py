
from des_utils import generateKeys, get_bits, add_pads_if_necessary, encryptBlock, bin_to_hex
from data_utils import joinNumbers
def fonk1(msg: str, key: str) -> str:
    b1 = generateKeys(key)
    b2 = get_bits(msg)
    b2 = add_pads_if_necessary(b2)
    b3 = []
    for i in range(0, len(b2), 64):
        b4 = b2[i:i+64]
        b3.extend(encryptBlock(b4, b1))
    b5 = ''
    for i in range(0, len(b3), 4):
        b6 = joinNumbers(b3[i:i+4])
        b5 += bin_to_hex(b6)
    return b5
def fonk2(cipher: str, key: str) -> str:
    b1 = generateKeys(key)
    b1.reverse()
    b2 = get_bits(cipher)
    b7 = []
    for i in range(0, len(b2), 64):
        b4 = b2[i:i+64]
        b7.extend(encryptBlock(b4, b1))
    b8 = ''
    for i in range(0, len(b7), 4):
        b6 = joinNumbers(b7[i:i+4])
        b8 += bin_to_hex(b6)
    return b8.rstrip('0')
if b9 = = "__main__":
    b10 = "This is a test b10."
    b11 = "mysecretkey"
    b12 = fonk1(b10, b11)
    print(f"Encrypted Message: {b12}")
    b13 = fonk2(b12, b11)
    print(f"Decrypted Message: {b13}")
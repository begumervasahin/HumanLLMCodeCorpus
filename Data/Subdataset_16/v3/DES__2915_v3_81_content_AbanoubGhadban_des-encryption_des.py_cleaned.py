
from des_utils import generateKeys, get_bits, add_pads_if_necessary, encryptBlock, bin_to_hex
from data_utils import joinNumbers
def fonk1(msg: str, key: str) -> str:
    b1 = generateKeys(key)
    b2 = add_pads_if_necessary(get_bits(msg))
    b3 = []
    for i in range(0, len(b2), 64):
        b4 = b2[i:i+64]
        b3.extend(encryptBlock(b4, b1))
    b5 = ''.join(bin_to_hex(joinNumbers(b3[i:i+4])) for i in range(0, len(b3), 4))
    return b5
def fonk2(cipher: str, key: str) -> str:
    b1 = generateKeys(key)
    b1.reverse()
    b2 = get_bits(cipher)
    b6 = []
    for i in range(0, len(b2), 64):
        b4 = b2[i:i+64]
        b6.extend(encryptBlock(b4, b1))
    b7 = ''.join(bin_to_hex(joinNumbers(b6[i:i+4])) for i in range(0, len(b6), 4))
    return b7.rstrip('0')
if b8 = = "__main__":
    b9 = "This is a test b9."
    b10 = "mysecretkey"
    b11 = fonk1(b9, b10)
    print(f"Encrypted Message: {b11}")
    b12 = fonk2(b11, b10)
    print(f"Decrypted Message: {b12}")
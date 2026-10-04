from Crypto.Cipher import AES
from Crypto import Random
def xor(a, b):
    a_bin = '{:032b}'.format(int(a, 16))
    b_bin = '{:032b}'.format(int(b, 16))
    return ''.join(str(int(a_bin[i]) ^ int(b_bin[i])) for i in range(len(a_bin)))
def enc(card_number, rounds, produce_keys, round_keys):
    encoded_number = '{:054b}'.format(int(card_number))
    l, r = encoded_number[:27], encoded_number[27:]
    if produce_keys:
        for _ in range(rounds):
            key = Random.new().read(16).hex()
            round_keys.append(key)
    for i in range(rounds):
        key = round_keys[i]
        obj = AES.new(bytes.fromhex(key))
        hex_r = '{:08x}'.format(int(r + '0' * 5, 2))
        b = hex_r + '0' * 23 + str(i + 1)
        enc_res = obj.encrypt(bytes.fromhex(b)).hex()[:7] + '0'
        tmp = r
        r = xor(enc_res, l + '0' * 5)
        l = tmp
    return l, r
def dec(cipher, rounds, round_keys):
    encoded_number = '{:054b}'.format(int(cipher))
    l, r = encoded_number[:27], encoded_number[27:]
    for i in range(rounds, 0, -1):
        key = round_keys[i - 1]
        obj = AES.new(bytes.fromhex(key))
        hex_l = '{:08x}'.format(int(l + '0' * 5, 2))
        b = hex_l + '0' * 23 + str(i)
        enc_res = obj.encrypt(bytes.fromhex(b)).hex()[:7] + '0'
        tmp = l
        l = xor(enc_res, r + '0' * 5)
        r = tmp
    return l, r
def main():
    credit_card_number = "4532294977918448"
    print('Number to encrypt =', credit_card_number)
    round_keys = []
    rounds = 6
    l, r = enc(credit_card_number, rounds, True, round_keys)
    final = int(l + r, 2)
    while final > 9999999999999999:
        print('Not valid encoded number =', final)
        l, r = enc(final, rounds, False, round_keys)
        final = int(l + r, 2)
    print('Encoded number =', final)
    print('Decrypting ...')
    print('Cipher to decrypt =', final)
    l, r = dec(final, rounds, round_keys)
    final = int(l + r, 2)
    while final > 9999999999999999:
        print('Not valid encoded number =', final)
        l, r = dec(final, rounds, round_keys)
        final = int(l + r, 2)
    print('Decrypted number =', final)
if __name__ == "__main__":
    main()
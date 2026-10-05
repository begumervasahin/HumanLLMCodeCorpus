from fractions import gcd
from random import randint
def is_private_key(d, e, p_1, p_2):
    return gcd(e * d - 1, (p_1 - 1)*(p_2 - 1)) == (p_1 - 1)*(p_2 - 1)
def decrypt_1(input1, key, N):
    decrypted = []
    for C in input1:
        decrypted.append((C**key) % N)
    return decrypted
def decrypt_2(input2):
    decrypted_chars = []
    for num in input2:
        decrypted_chars.append(chr(num))
    return decrypted_chars
def main():
    cipher_text = raw_input('Please enter the encoded message here in numbers form: ')
    input_list = cipher_text.split()
    input_list = [int(a) for a in input_list]
    p_1 = input('Please enter your first password: ')
    p_2 = input('Please enter your second password: ')
    N = input('Please enter your Public Key number: ')
    e = input('Please enter your Private Key number: ')
    invalid = True
    while invalid:
        key = randint(0, N)
        if is_private_key(key, e, p_1, p_2):
            invalid = False
    decrypted_numbers = decrypt_1(input_list, key, N)
    decrypted_message = ''.join(decrypt_2(decrypted_numbers))
    print('Decrypted message: %s' % decrypted_message)
    print('\nThank you for using our service!')
if __name__ == "__main__":
    main()
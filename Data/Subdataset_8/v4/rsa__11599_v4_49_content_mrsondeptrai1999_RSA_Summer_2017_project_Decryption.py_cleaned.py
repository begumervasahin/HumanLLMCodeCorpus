
cipher_text = input('Please enter the encoded message here in numbers form: ')
input_list = cipher_text.split()
input_list = [int(a) for a in input_list]
p_1 = input('Please enter your first password: ')
p_2 = input('Please enter your second password: ')
N = input('Please enter your Public Key number: ')
e = input('Please enter your Private Key number: ')
from fractions import gcd
from random import randint
def is_private_key(d):
    if gcd(e * d - 1, (p_1 - 1) * (p_2 - 1)) == (p_1 - 1) * (p_2 - 1):
        return True
    else:
        return False
invalid = True
while invalid:
    key = randint(0, N)
    if is_private_key(key):
        invalid = False
    else:
        pass
def decrypt_1(input1):
    M = []
    for C in input1:
        M.append((C ** key) % N)
    return M
list_number = decrypt_1(input_list)
def decrypt_2(input2):
    decrypted_text = []
    for char_code in input2:
        decrypted_text.append(chr(char_code))
    return decrypted_text
final = ''.join(decrypt_2(list_number))
print('\nDecrypted message:', final)
print('\nThank you for trusting our service!')
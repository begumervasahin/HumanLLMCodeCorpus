def get_input(prompt):
    return input(prompt)
def split_input(input_string):
    return [int(a) for a in input_string.split()]
def prompt_for_values():
    p_1 = int(get_input('Please enter your first password: '))
    p_2 = int(get_input('Please enter your second password: '))
    N = int(get_input('Please enter your Public Key number: '))
    e = int(get_input('Please enter your Private Key number: '))
    return p_1, p_2, N, e
def is_private_key(d, e, p_1, p_2):
    return gcd(e * d - 1, (p_1 - 1) * (p_2 - 1)) == (p_1 - 1) * (p_2 - 1)
def generate_valid_private_key(N, e, p_1, p_2):
    while True:
        key = randint(0, N)
        if is_private_key(key, e, p_1, p_2):
            return key
def decrypt_message(input_list, key, N):
    decrypted_text = []
    for char_code in input_list:
        decrypted_text.append(chr((char_code ** key) % N))
    return ''.join(decrypted_text)
def main():
    cipher_text = get_input('Please enter the encoded message here in numbers form: ')
    input_list = split_input(cipher_text)
    p_1, p_2, N, e = prompt_for_values()
    key = generate_valid_private_key(N, e, p_1, p_2)
    decrypted_message = decrypt_message(input_list, key, N)
    print('\nDecrypted message:', decrypted_message)
    print('\nThank you for trusting our service!')
if __name__ == "__main__":
    main()
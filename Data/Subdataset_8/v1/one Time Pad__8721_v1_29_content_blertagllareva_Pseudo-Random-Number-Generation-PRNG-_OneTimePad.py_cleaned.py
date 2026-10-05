def char_to_num(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 0
    for letter in alphabet:
        num += 1
        if letter == char:
            break
    return num
def num_to_char(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num - 1]
def encode_char(p_text, key):
    p_num = char_to_num(p_text)
    k_num = char_to_num(key)
    c_num = (p_num + k_num) % 26
    c_text = num_to_char(c_num)
    return c_text
def decode_char(c_text, key):
    c_num = char_to_num(c_text)
    k_num = char_to_num(key)
    p_num = (c_num - k_num) % 26
    p_text = num_to_char(p_num)
    return p_text
def encode(p_text, key):
    c_text = ""
    for i in range(len(p_text)):
        c_text += encode_char(p_text[i], key[i])
    return c_text
def decode(c_text, key):
    p_text = ""
    for i in range(len(c_text)):
        p_text += decode_char(c_text[i], key[i])
    return p_text
def main():
    print("OneTimePad Program. Çelësi duhet të jetë më i vogël ose i barabartë me plain-tekstin. Plain-teksti nuk duhet të ketë numra.")
    print("\nMundësitë:\n1: Enkodimi\n2: Dekodimi\n3: Ndërprerje")
    while True:
        choice = input(">>> ")
        if choice == "1":
            plain_text = input("Plain-teksti: ")
            key = input("Çelësi: ")
            if len(key) < len(plain_text):
                print("Çelësi duhet të jetë i paktën aq i gjatë sa plain-teksti.")
            else:
                print("Cipher-teksti:", encode(plain_text, key))
        elif choice == "2":
            cipher_text = input("Cipher-teksti: ")
            key = input("Çelësi: ")
            if len(key) < len(cipher_text):
                print("Çelësi duhet të jetë i paktën aq i gjatë sa cipher-teksti.")
            else:
                print("Plain-teksti:", decode(cipher_text, key))
        elif choice == "3":
            break
        else:
            print("Ju lutem zgjedhni 1, 2, ose 3.")
if __name__ == "__main__":
    main()
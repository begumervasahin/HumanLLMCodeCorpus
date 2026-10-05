import os
import sys
from utils import chilkat
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def encrypt_text(text, crypt):
    cipher_text64 = crypt.encryptStringENC(text)
    return cipher_text64
def main():
    clear_screen()
    Adh = chilkat.CkDh()
    Bdh = chilkat.CkDh()
    success = Adh.UnlockComponent("Test")
    Adh.UseKnownPrime(5)
    p = Adh.p()
    g = Adh.get_G()
    success = Bdh.SetPG(p, g)
    eA = Adh.createE(256)
    eB = Bdh.createE(256)
    kA = Adh.findK(eB)
    kB = Bdh.findK(eA)
    if kA == kB:
        eq = 'A shared secret equal to B'
    else:
        eq = '**Shared secret NOT EQUAL !!!!**'
    crypt = chilkat.CkCrypt2()
    success = crypt.UnlockComponent("Test")
    crypt.put_EncodingMode("hex")
    crypt.put_HashAlgorithm("md5")
    sessionKey = crypt.hashStringENC(kA)
    sessionm = '128-bit Season key : {}'.format(sessionKey)
    crypt.put_CryptAlgorithm("aes")
    crypt.put_KeyLength(128)
    crypt.put_CipherMode("cbc")
    iv = crypt.hashStringENC(sessionKey)
    ivm = 'Initialization Vector: {}'.format(iv)
    crypt.SetEncodedKey(sessionKey,"hex")
    crypt.SetEncodedIV(iv,"hex")
    print('-> {}\n--> {}'.format(sessionm, ivm))
    print("\n")
    text_list = []
    while True:
        print('Choose :\n[1] Encrypt text\n[2] Decrypt text (For this Session only)\n[3] List all Encrypted texts\n[4] Exit')
        choose = input('>> ')
        if choose == '1':
            choosen = input('Encrypt text >> ')
            encrypted_text = encrypt_text(choosen, crypt)
            text_list.append(encrypted_text)
            print('+ Encrypted ->', encrypted_text)
        elif choose == '2':
            choosen = input('Decrypt text >> ')
            plain_text = crypt.decryptStringENC(choosen)
            print(plain_text)
        elif choose == '3':
            count = 1
            for i in text_list:
                print('{} - {}'.format(count, i))
                count += 1
        elif choose == '4':
            print('Good Bye')
            sys.exit()
        else:
            print('Invalid number, type [h] for help or 4 for exit')
if __name__ == "__main__":
    main()
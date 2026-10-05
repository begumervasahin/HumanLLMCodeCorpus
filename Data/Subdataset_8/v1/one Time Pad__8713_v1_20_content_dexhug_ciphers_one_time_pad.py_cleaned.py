import string
import secrets
def encrypt(message, shift):
    encryption = ""
    counter = 0
    for i in message:
        for j in string.ascii_uppercase:
            if i == j:
                mes_ind = string.ascii_uppercase.find(i)
                if mes_ind + shift[counter] > 25:
                    mes_ind -= 26
                enc_letter = string.ascii_uppercase[mes_ind+shift[counter]]
                encryption += enc_letter
                counter += 1
    return encryption
def decrypt(encryption, shift):
    dec_shift = []
    for i in range(len(shift)):
        dec_shift.append(26 - shift[i])
    decryption = encrypt(encryption, dec_shift)
    return decryption
def main():
    print("Welcome to the One Time Pad Cipher.\n")
    message = "Thanks for taking a look at my one time pad cipher!"
    non_letters = string.punctuation + string.whitespace + string.digits
    table = str.maketrans({key: None for key in non_letters})
    message = message.translate(table)
    shift = []
    for i in range(len(message)):
        shift.append(secrets.randbelow(27))
    print("Shifting the input by this list:", shift)
    encryption = encrypt(message.upper(), shift)
    print("\nYour encrypted message is:\n", encryption, sep="")
    decryption = decrypt(encryption, shift)
    print("Your decrypted message is:\n", decryption, sep="")
if __name__ == "__main__":
    main()

import string
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
				if counter >= len(shift):
					counter = 0
		for k in string.digits:
			if i == k:
				encryption += string.digits[int(i)]
		for w in string.whitespace:
			if i == w:
				mes_ind = string.whitespace.find(i)
				encryption += string.whitespace[mes_ind]
	return encryption
def decrypt(encryption, shift):
	dec_shift = []
	for i in range(len(shift)):
		dec_shift.append(26 - shift[i])
	decryption = encrypt(encryption, dec_shift)
	return decryption
def Main():
	print("Welcome to the Polyalphabetic Cipher.\n")
	shift_word = "encrypt"
	message = "Thanks for taking a look at my polyalphabetic cipher!"
	non_letters = string.punctuation + string.whitespace + string.digits
	non_letters_table = str.maketrans({key: None for key in non_letters})
	shift_word = shift_word.translate(non_letters_table)
	shift = []
	for i in shift_word.upper():
		for j in string.ascii_uppercase:
			if i == j:
				shift_index = string.ascii_uppercase.find(i)
				shift.append(shift_index + 1)
	p_table = str.maketrans({key: None for key in string.punctuation})
	message = message.translate(p_table)
	print("Shifting the input by this list:", shift)
	print("Message to be encrypted:\n", message, sep="")
	encryption = encrypt(message.upper(), shift)
	print("\nYour encrypted message is:\n", encryption, sep="")
	decryption = decrypt(encryption, shift)
	print("Your decrypted message is:\n", decryption, sep="")
Main()
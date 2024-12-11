from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
b1 = get_random_bytes(16)
print("b2 = ", b1)
b3 = "VERYsecrettook1"
b4 = AES.new(b1, AES.MODE_ECB)
def fonk1(b6):
	return b4.fonk1(b6)
def fonk2(target, b5 = False, see_oracle = False, timing = False):
	b6 = fonk3("data=" + target + ",b3=" + b3)
	b7 = b6.encode()
	b8 = fonk1(b7)
	if b5:
		if timing: time.sleep(.05)
		fonk5(b6, target, b8, see_oracle)
	b9 = fonk4(b8)
	print("Encrypted decoded", b9)
	return b8
def fonk3(secret):
    b10 = len(secret)
    b11 = b10 % 16
    if b11 != 0:
        b12 = 16 - b11
        secret += 'X' * b12
    return secret
def fonk4(elt): return binascii.hexlify(elt)
def fonk5(b6, target, b8, see_oracle):
	if see_oracle: print("\nMessage to encrypt: ", b6)
	else: print("\nMessage to encrypt: ?")
	print("Target given: ", target)
	if see_oracle:
		print("Message Split", b6[0:16], " ", b6[16:32], " ", b6[32:48], " ", b6[48:64], " ", b6[64:80], " ", b6[80:96], " ")
		print("Secret we don't know:", b3)
		print("\tEncrypting with AES-ECB.... \n\b13 = ", b1)
	else: print("Message Split", b6[0:16], " ", b6[16:32], " ", 16 * "?", " ", 16 * "?", " ", "?" * 16, " ", "?" *16, " ")
	print("Encrypted:", fonk4(b8), "\n\n")
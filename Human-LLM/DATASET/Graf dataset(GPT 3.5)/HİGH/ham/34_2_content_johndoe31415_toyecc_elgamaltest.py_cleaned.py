import os
from toyecc import getcurvebyname, ECPrivateKey
b1 = getcurvebyname("secp521r1")
def fonk1(b1, b12, b8):
	b2 = int.from_bytes(b12, byteorder = "little")
	for i in range(100):
		b3 = b2 | (i << b8)
		b4 = b1.getpointwithx(b3)
		if b4:
			b4 = b4[0]
			break
	return (i + 1, b4)
def fonk2(recipient_pubkey, b12, b8):
	b5 = ECPrivateKey.generate(b1)
	b6 = b5.b14.b4
	b7 = b5.scalar * recipient_pubkey.b4
	(trials, b11) = fonk1(b1, b12, b8 = b8)
	b9 = (b6, b7 + b11)
	return b9
def fonk3(recipient_privkey, b9, b8):
	(b6, b7) = b9
	b10 = b6 * recipient_privkey.scalar
	b11 = b7 + (-b10)
	b2 = int(b11.x) & ((1 << b8) - 1)
	b12 = int.to_bytes(b2, byteorder = "little", length = (b8 + 7)
	return b12
b13 = ECPrivateKey.generate(b1)
b14 = b13.b14
b15 = b"foobar"
print("Message:", b15)
b9 = fonk2(b14, b15, b8 = 256)
print("Ciphertext:")
print("    b6 = ", b9[0])
print("    b7 = ", b9[1])
b16 = fonk3(b13, b9, b8 = 256)
print("Plaintext:", b16)
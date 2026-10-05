import Seeded_Random_Generator
b1 = int(3336)
def fonk1(a_private_key,b_private_key,a_peer_public_key,b_peer_public_key):
	b2 = int((str(a_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x","")).replace(">",""),16)
	b3 = int((str(b_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x","")).replace(">",""),16)
	b4 = int((str(a_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x","")).replace(">",""),16)
	b5 = int((str(b_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x","")).replace(">",""),16)
	b6 = (b4^b2)%b5
	b7 = (b4^b3)%b5
	b8 = (b7^b2)%b5
	b9 = (b6^b3)%b5
	if (b8 = = b9):
		b1 = int(b8%1111)
	b10 = Seeded_Random_Generator.reduce(b1)
	print(b1,b10)
	Seeded_Random_Generator.random_generator(b10)
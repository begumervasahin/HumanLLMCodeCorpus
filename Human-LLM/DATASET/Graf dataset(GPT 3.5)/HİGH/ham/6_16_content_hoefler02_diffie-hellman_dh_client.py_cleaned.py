from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from random import randint
class class1:
	def fonk1(self, b1, generator, prime):
		self.b1 = b1
		self.b2 = generator
		self.b3 = prime
		self.b4 = randint(1, prime)
		self.b5 = pow(self.b2, self.b4, self.b3)
	def fonk2(self, received_public_key):
		self.b6 = hex(pow(received_public_key, self.b4, self.b3))[2:]
		while True:
			if (len(self.b6) == 32 or len(self.b6) == 48 or len(self.b6) == 64):
				break
			elif (len(self.b6) > 32):
				self.b6 = self.b6[1:]
			else:
				self.b6 = '0' + self.b6
		self.b6 = bytes.fromhex(self.b6)
		return int(self.b6.hex(), 16)
	def fonk3(self, b8):
		b7 = AES.new(self.b6)
		b8 = ''.join([hex(ord(c))[2:] for c in b8])
		while(len(b8) % 32 != 0):
			b8 = '0' + b8
		b8 = bytes.fromhex(b8)
		b9 = b7.encrypt(b8)
		return int(b9.hex(), 16)
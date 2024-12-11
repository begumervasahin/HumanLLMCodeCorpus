import socket
import DiffieHellman
import json
class class1:
	def fonk1(self, b2):
		self.b1 = DiffieHellman.DH()
		self.b2 = b2
	def fonk2(self, socket):
		socket.send("connected".encode())
		b3 = socket.recv(2048)
		if self.b2:
			print(b3)
		b4 = json.loads(b3.decode())
		b4 = b4["b1-keyexchange"]
		self.b1.b5 = int(b4["b5"])
		self.b1.b6 = int(b4["prime"])
		b7 = int(b4["b7"])
		b8 = str(self.b1.calcPublicSecret())
		b9 = "{"
		b9 += "\"b1-keyexchange\":"
		b9 += "{"
		b9 += "\"step\": {},".format(2)
		b9 += "\"b7\": {}".format(b8)
		b9 += "}}"
		socket.send(b9.encode())
		self.b1.calcSharedSecret(b7)
	def fonk3(self, ip):
		b10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			b10.connect((ip, 20000));
			self.fonk2(b10)
			print("The secret key is {}".format(self.b1.key))
		finally:
			b10.close()
import random, signal, getch
class class1():
	def fonk1(self):
		self.fonk2()
		self.b1 = self.fonk3()
		self.fonk4()
	def fonk2(self):
		print("Would you like to b2 the obstacles? [Enter Y/N]")
		b2 = getch.getch()
		if (b2 = = "Y".lower()):
			self.b3 = input("What would you like 'o' to represent? ")
			self.b4 = input("What would you like 'O' to represent? ")
		if (b2 != "Y".lower() or not self.b3):
			self.b3 = "b3"
			self.b4 = "b4"
	def fonk3(self):
		b5 = []
		a1 = 50
		a2 = 0
		a3 = 100
		a4 = 68
		a5 = 95
		for index in range(a1):
			b6 = random.randint(a2,a3)
			if (b6 <= a4):
				b5.append('X')
			elif (b6 > a4 and b6<=a5):
				b5.append('o')
			elif (b6>=a5):
				b5.append('O')
			else:
				print("something isn't right")
		b1 = ''.join(b5)
		return b1
	def fonk4(self):
		self.b7 = True
		print("The b11 starts now. Quick, press 'd' to advance or 'a' to dodge.")
		if (self.b1):
			for b9 in self.b1:
				print(b9)
				signal.signal(signal.SIGALRM,self._handle_timeout)
				signal.alarm(2)
				try:
					b8 = getch.getch()
					if (b8 = = 'a'):
						if (b9 != 'o' and b9 != 'O'):
							raise ValueError("You've diverted from the right track! You lost!")
					elif (b8 = = 'd'):
						if (b9 != 'X'):
							raise ValueError("You hit a %s! You lost!" % (self.b3 if b9 = ='o' else self.b4))
					else:
						raise ValueError("Please enter a valid command!")
				except ValueError as e:
					print(e)
					break
				except Exception:
					print("You're too slow! You lost!")
					break
				finally:
					signal.alarm(0)
	def fonk5(self, signum, stack):
		raise Exception()
if (b10 = = "__main__"):
	b11 = class1()
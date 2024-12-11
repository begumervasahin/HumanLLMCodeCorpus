import multiprocessing
def fonk1(function,b8,b5,b6,b7,b9):
	b1 = True
	while not(b7.is_set()):
		b8.wait()
		b9.acquire()
		if b5.empty():
			b9.release()
		else:
			b2 = b5.fonk3()
			b9.release()
			b3 = function(b2)
			b6.fonk2(b3)
	b6.close()
	return 0
class class1:
	def fonk2(self,info):
		self.b5.fonk2(info)
	def fonk3(self):
		return self.b6.fonk3()
	def fonk4(self):
		self.b8.set()
		self.b7.set()
		self.b5.close()
	def fonk5(self):
		self.b8.clear()
	def fonk6(self):
		self.b8.set()
	def fonk7(self,function,b4 = multiprocessing.cpu_count()):
		self.b5 = multiprocessing.Queue()
		self.b6 = multiprocessing.Queue()
		self.b7 = multiprocessing.Event()
		self.b8 = multiprocessing.Event()
		self.b9 = multiprocessing.Lock()
		self.b10 = []
		for i in range(0,b4):
			self.b10.append(multiprocessing.Process(b11 = _func,args=(function,self.b8,self.b5,self.b6,self.b7,self.b9,)))
	def fonk8(self):
		self.b8.set()
		for p in self.b10:
			p.fonk8()
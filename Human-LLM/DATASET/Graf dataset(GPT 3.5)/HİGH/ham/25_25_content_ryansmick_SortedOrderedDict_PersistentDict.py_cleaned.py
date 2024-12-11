from SortedOrderedDict import SortedOrderedDict
class class1(SortedOrderedDict):
	b1 = ": "
	def fonk1(self, b2 = None, b5=b1, b3=None, load_filepath=None, load_delim=': ', load_key_trans_func=None, load_value_trans_func=None):
		super(class1, self).fonk1(b3 = b3)
		if load_filepath:
			self.fonk3(load_filepath, b4 = load_delim, key_trans_func=load_key_trans_func, value_trans_func=load_key_trans_func)
		self.b2 = b2
		self.b5 = b5
	def fonk2(self, b2 = None, b4=None):
		if b2:
			b6 = b2
		elif self.b2:
			b6 = self.b2
		else:
			raise ValueError("No save b6 specified. Save b6 must be specified as either constructor parameter or save function parameter")
		if b4:
			b7 = b4
		else:
			b7 = self.b5
		with open(b6, 'w+') as f:
			for b9, b8 in self.iteritems_ordered():
				f.write("{}{}{}\n".format(b9, b7, b8))
	def fonk3(self, b6, b4 = ': ', key_trans_func=None, value_trans_func=None, add_to_existing=False):
		with open(b6, 'r') as f:
			if not add_to_existing:
				self.clear()
			for line in f:
				b9, b8 = line.split(b4, 1)
				b8 = b8.rstrip()
				if key_trans_func:
					b9 = key_trans_func(b9)
				if value_trans_func:
					b8 = value_trans_func(b8)
				self.insert(b9, b8)
	def fonk4(self):
		if not self.b2:
			raise ValueError("No save b6 specified")
		return self
	def fonk5(self, exception_type, exception_value, traceback):
		self.fonk2(b4 = self.b5)
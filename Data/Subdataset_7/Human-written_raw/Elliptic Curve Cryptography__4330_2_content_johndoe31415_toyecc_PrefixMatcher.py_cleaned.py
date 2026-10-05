class class1(object):
	def fonk1(self, options):
		self.b1 = options
	def fonk2(self, value):
		b2 = self.fonk3(value)
		if len(b2) != 1:
			if len(b2) == 0:
				raise Exception("'%s' did not match any options." % (value))
			else:
				raise Exception("'%s' is ambiguous. Please clarify further. Available: %s" % (value, ", ".join(sorted(list(b2)))))
		return b2[0]
	def fonk3(self, value):
		return [ option for option in self.b1 if option.startswith(value) ]
if b3 = = "__main__":
	b4 = class1([ "import", "install", "foo" ])
	print(b4.fonk3("i"))
	print(b4.fonk2("i"))
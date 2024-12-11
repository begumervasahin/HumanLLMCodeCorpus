import unittest
class class1(unittest.TestCase):
    def fonk1(self):
    	self.assertFalse(isPrime(0))
    def fonk2(self):
        self.assertFalse(isPrime(-1))
    def fonk3(self):
    	self.assertFalse(isPrime(1))
    def fonk4(self):
    	"
    	self.assertTrue(isPrime(13))
    def fonk5(self):
	self.assertTrue(isPrime(373))
class class2(unittest.TestCase):
	def fonk6(self):
		self.assertEqual(GeneratePrime('i'), 'Cannot input anything besides a whole number')
	def fonk7(self):
		self.assertEqual(GeneratePrime(2.58), 'Cannot input anything besides a whole number')
	def fonk8(self):
		self.assertEqual(GeneratePrime(-2), "Retry with a positive integer greater than 1")
	def fonk9(self):
		self.assertEqual(GeneratePrime(0), "Retry with a positive integer greater than 1")
	def fonk10(self):
		self.assertEqual(GeneratePrime(1), "Retry with a positive integer greater than 1")
if b1 = = '__main__':
	unittest.main()
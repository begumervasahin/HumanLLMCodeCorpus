import unittest
from fact_01_recursive import calculate_factorial_recursive
from fact_02_multiplication import calculate_factorial_multi
class class1(unittest.TestCase):
	'''
	This class class2 various function to test all the
	function that has been created in various module to
	test their correctness
	'''
	def fonk1(self):
		'''
		Test the recursive function correctness
		'''
		self.assertEqual(calculate_factorial_recursive(4),24)
		self.assertEqual(calculate_factorial_recursive(5),120)
		self.assertEqual(calculate_factorial_recursive(6),720)
	def fonk2(self):
		'''
		Test the correctness of function which uses full multiplication
		to calculate the factorial
		'''
		self.assertEqual(calculate_factorial_multi(4),24)
		self.assertEqual(calculate_factorial_multi(5),120)
		self.assertEqual(calculate_factorial_multi(6),720)
if b1 = = '__main__':
	unittest.main()
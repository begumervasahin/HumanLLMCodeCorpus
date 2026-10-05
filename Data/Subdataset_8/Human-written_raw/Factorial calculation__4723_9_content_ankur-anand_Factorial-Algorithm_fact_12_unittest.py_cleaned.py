import unittest
from fact_01_recursive import calculate_factorial_recursive
from fact_02_multiplication import calculate_factorial_multi
class FactorialTesting(unittest.TestCase):
	'''
	This class implements various function to test all the
	function that has been created in various module to
	test their correctness
	'''
	def test_calculate_factorial_recursive(self):
		'''
		Test the recursive function correctness
		'''
		self.assertEqual(calculate_factorial_recursive(4),24)
		self.assertEqual(calculate_factorial_recursive(5),120)
		self.assertEqual(calculate_factorial_recursive(6),720)
	def test_calculate_factorial_multi(self):
		'''
		Test the correctness of function which uses full multiplication
		to calculate the factorial
		'''
		self.assertEqual(calculate_factorial_multi(4),24)
		self.assertEqual(calculate_factorial_multi(5),120)
		self.assertEqual(calculate_factorial_multi(6),720)
if __name__ == '__main__':
	unittest.main()
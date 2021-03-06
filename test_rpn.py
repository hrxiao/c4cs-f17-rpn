import unittest # turns it into obj named unittest in this code
import rpn

# python3 -m unittest

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2,result)

	def test_subtract(self):
		result = rpn.calculate('5 -3 -')
		self.assertEqual(8,result)

	def test_multiply(self):
		result = rpn.calculate('4 3 *')
		self.assertEqual(12,result)

	def test_divide(self):
		result = rpn.calculate('30 5 /')
		self.assertEqual(6,result)

	def test_exp(self):
		result = rpn.calculate('4 3 ^')
		self.assertEqual(64,result)
import unittest # turns it into obj named unittest in this code
import rpn

# python3 -m unittest

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2,result)

	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2,result)


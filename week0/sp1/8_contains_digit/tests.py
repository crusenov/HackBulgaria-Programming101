import solution
import unittest

class ContainsDigit(unittest.TestCase):

	def test_contains_digit_1(self):
		self.assertEqual(False, solution.contains_digit(123,4))

	def test_contains_digit_2(self):
		self.assertEqual(True, solution.contains_digit(42,2))

	def test_contains_digit_3(self):
		self.assertEqual(True, solution.contains_digit(1000, 0))

	def test_contains_digit_4(self):
		self.assertEqual(False, solution.contains_digit(12346789, 5))

if __name__ == '__main__':
	unittest.main()
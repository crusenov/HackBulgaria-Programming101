import solution
import unittest

class IsIntPalindrom(unittest.TestCase):

	def test_is_int_palindrom_1(self):
		self.assertEqual(True, solution.is_int_palindrom(1))

	def test_is_int_palindrom_2(self):
		self.assertEqual(False, solution.is_int_palindrom(42))

	def test_is_int_palindrom_3(self):
		self.assertEqual(True, solution.is_int_palindrom(100001))

	def test_is_int_palindrom_4(self):
		self.assertEqual(True, solution.is_int_palindrom(999))

	def test_is_int_palindrom_5(self):
		self.assertEqual(False, solution.is_int_palindrom(123))


if __name__ == '__main__':
	unittest.main()

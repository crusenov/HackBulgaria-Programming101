import solution
import unittest

class IsNumberBalanced(unittest.TestCase):

	def test_is_number_balanced_1(self):
		self.assertEqual(True, solution.is_number_balanced(9))

	def test_is_number_balanced_2(self):
		self.assertEqual(True, solution.is_number_balanced(11))

	def test_is_number_balanced_3(self):
		self.assertEqual(False, solution.is_number_balanced(13))

	def test_is_number_balanced_4(self):
		self.assertEqual(True, solution.is_number_balanced(121))

	def test_is_number_balanced_5(self):
		self.assertEqual(True, solution.is_number_balanced(4518))

	def test_is_number_balanced_6(self):
		self.assertEqual(False, solution.is_number_balanced(28471))

	def test_is_number_balanced_7(self):
		self.assertEqual(True, solution.is_number_balanced(1238033))

if __name__ == '__main__':
	unittest.main()
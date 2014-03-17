import solution
import unittest

class IsIncreasing(unittest.TestCase):

	def test_is_increasing_1(self):
		self.assertEqual(True, solution.is_increasing([1,2,3,4,5]))

	def test_is_increasing_2(self):
		self.assertEqual(True, solution.is_increasing([1]))

	def test_is_increasing_4(self):
		self.assertEqual(False, solution.is_increasing([5,6,-10]))

	def test_is_increasing_5(self):
		self.assertEqual(False, solution.is_increasing([1,1,1,1]))

if __name__ == '__main__':
	unittest.main()
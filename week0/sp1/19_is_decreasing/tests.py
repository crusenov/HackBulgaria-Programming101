import solution
import unittest

class IsDecreasing(unittest.TestCase):

	def test_is_decreasing_1(self):
		self.assertEqual(True, solution.is_decreasing([5,4,3,2,1]))

	def test_is_decreasing_2(self):
		self.assertEqual(False, solution.is_decreasing([1,2,3]))

	def test_is_decreasing_3(self):
		self.assertEqual(True, solution.is_decreasing([100,50,20]))

	def test_is_decreasing_4(self):
		self.assertEqual(False, solution.is_decreasing([1,1,1,1]))

if __name__ == '__main__':
	unittest.main()

	
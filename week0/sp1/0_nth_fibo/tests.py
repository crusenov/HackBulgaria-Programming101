import solution
import unittest

class Nth_fibonacci(unittest.TestCase):

	def test_nth_fibonaci_1(self):
		self.assertEqual(1, solution.nth_fibonacci(1))

	def test_nth_fibonacci_2(self):
		self.assertEqual(1, solution.nth_fibonacci(2))

	def test_nth_fibonacci_3(self):
		self.assertEqual(2, solution.nth_fibonacci(3))

	def test_nth_fibonacci_10(self):
		self.assertEqual(55, solution.nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()

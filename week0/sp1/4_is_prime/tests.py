import solution
import unittest

class IsPrime(unittest.TestCase):

	def test_is_prime_1(self):
		self.assertEqual(False, solution.is_prime(1))

	def test_is_prime_2(self):
			self.assertEqual(True, solution.is_prime(2))

	def test_is_prime_3(self):
			self.assertEqual(False, solution.is_prime(8))

	def test_is_prime_4(self):
			self.assertEqual(True, solution.is_prime(11))

	def test_is_prime_5(self):
			self.assertEqual(False, solution.is_prime(-10))

if __name__ == '__main__':
	unittest.main()
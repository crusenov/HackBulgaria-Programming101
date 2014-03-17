import solution
import unittest

class PrimeFactorization(unittest.TestCase):

	def test_prime_factorization_1(self):
		self.assertEqual([(2, 1), (5, 1)], solution.prime_factorization(10))

	def test_prime_factorization_2(self):
		self.assertEqual([(2, 1), (7, 1)], solution.prime_factorization(14))

	def test_prime_factorization_3(self):
		self.assertEqual([(2, 2), (89, 1)], solution.prime_factorization(356))

	def test_prime_factorization_4(self):
		self.assertEqual([(89, 1)], solution.prime_factorization(89)) 

	def test_prime_factorization_5(self):
		self.assertEqual([(2, 3), (5, 3)], solution.prime_factorization(1000))

if __name__ == '__main__':
	unittest.main()
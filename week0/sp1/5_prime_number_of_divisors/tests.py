import solution
import unittest

class PrimeNumberOfDivisors(unittest.TestCase):

	def test_prime_num_of_div_1(self):
		self.assertEqual(True, solution.prime_number_of_divisors(7))

	def test_prime_num_of_div_2(self):
		self.assertEqual(False, solution.prime_number_of_divisors(8))

	def test_prime_num_of_div_3(self):
		self.assertEqual(True, solution.prime_number_of_divisors(9))

if __name__ == '__main__':
	unittest.main()
import solution
import unittest

class WhatIsMySign(unittest.TestCase):

	def test_what_is_my_sign_1(self):
		self.assertEqual("Leo", solution.what_is_my_sign(5, 8))

	def test_what_is_my_sign_2(self):
		self.assertEqual("Aquarius", solution.what_is_my_sign(29,1))

	def test_what_is_my_sign_3(self):
		self.assertEqual("Cancer", solution.what_is_my_sign(30,6))

	def test_what_is_my_sign_4(self):
		self.assertEqual("Gemini", solution.what_is_my_sign(31,5))

	def test_what_is_my_sign_5(self):
		self.assertEqual("Aquarius", solution.what_is_my_sign(2,2))

	def test_what_is_my_sign_6(self):
		self.assertEqual("Taurus", solution.what_is_my_sign(8,5))

	def test_what_is_my_sign_7(self):
		self.assertEqual("Capricorn", solution.what_is_my_sign(9,1))

if __name__ == '__main__':
	unittest.main()
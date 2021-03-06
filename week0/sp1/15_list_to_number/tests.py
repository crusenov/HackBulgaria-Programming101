import solution
import unittest

class ListToNumber(unittest.TestCase):

	def test_list_to_number_1(self):
		self.assertEqual(123, solution.list_to_number([1,2,3]))

	def test_list_to_number_2(self):
		self.assertEqual(99999, solution.list_to_number([9,9,9,9,9]))

	def test_list_to_number_3(self):
		self.assertEqual(123023, solution.list_to_number([1,2,3,0,2,3]))

if __name__ == '__main__':
	unittest.main()
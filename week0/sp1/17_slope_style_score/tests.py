import solution
import unittest

class SlopeStyleScore(unittest.TestCase):

	def test_slope_style_score_1(self):
		self.assertEqual(94.67, solution.slope_style_score([94, 95, 95, 95, 90]))

	def test_slope_style_score_2(self):
		self.assertEqual(80.0, solution.slope_style_score([60, 70, 80, 90, 100]))

	def test_slope_style_score_3(self):
		self.assertEqual(93.5, solution.slope_style_score([96, 95.5, 93, 89, 92]))

if __name__ == '__main__':
	unittest.main()
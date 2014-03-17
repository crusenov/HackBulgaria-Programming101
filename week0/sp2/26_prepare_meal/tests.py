import solution
import unittest

class PrepareMealTest(unittest.TestCase):

    def test_prepare_meal_1(self):
        self.assertEqual("spam", solution.prepare_meal(3))

    def test_prepare_meal_2(self):
        self.assertEqual("spam spam spam", solution.prepare_meal(27))

    def test_prepare_meal_3(self):
        self.assertEqual("", solution.prepare_meal(7))

if __name__ == '__main__':
    unittest.main()

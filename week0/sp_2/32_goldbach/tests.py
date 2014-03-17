import solution
import unittest

class GoldbachTest(unittest.TestCase):

    def test_goldbach_1(self):
        self.assertEqual([(2,2)], solution.goldbach(4))

    def test_goldbach_2(self):
        self.assertEqual([(3,3)], solution.goldbach(6))

    def test_goldbach_3(self):
        self.assertEqual([(3,5)], solution.goldbach(8))

    def test_goldbach_4(self):
        self.assertEqual([(3,7), (5,5)], solution.goldbach(10))

    def test_goldbach_5(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], solution.goldbach(100))

if __name__ == '__main__':
    unittest.main()

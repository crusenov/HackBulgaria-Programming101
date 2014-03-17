import solution
import unittest

class IsAnBanTest(unittest.TestCase):

    def test_is_an_bn_1(self):
        self.assertEqual(True, solution.is_an_bn(""))

    def test_is_an_bn_2(self):
        self.assertEqual(False, solution.is_an_bn("rado"))

    def test_is_an_bn_3(self):
        self.assertEqual(False, solution.is_an_bn("aaabb"))

    def test_is_an_bn_4(self):
        self.assertEqual(True, solution.is_an_bn("aaabbb"))

    def test_is_an_bn_5(self):
        self.assertEqual(False, solution.is_an_bn("aabbaabb"))

    def test_is_an_bn_6(self):
        self.assertEqual(False, solution.is_an_bn("bbbaaa"))

    def test_is_an_bn_7(self):
        self.assertEqual(True, solution.is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    unittest.main()

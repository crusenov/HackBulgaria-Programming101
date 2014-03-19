import solution
import unittest


class MagicStringTest(unittest.TestCase):
    """Testing magic_string - 250 problem from TC SRM 609 Div 2"""
    def test_problem_statement_cases(self):
        self.assertEqual(2, solution.magic_string(">><<><"))
        self.assertEqual(0, solution.magic_string(">>>><<<<"))
        self.assertEqual(4, solution.magic_string("<<>>"))
        self.assertEqual(20,
                         solution.magic_string(
                         "<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))

if __name__ == '__main__':
    unittest.main()

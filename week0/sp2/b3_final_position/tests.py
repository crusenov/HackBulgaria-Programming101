import solution
import unittest


class OneDimensionalRobotTests(unittest.TestCase):
    """Testing the 250 problem from TC 608 SRM Div 250"""

    def test_final_position_problem_statement_cases(self):
        self.assertEqual(2, solution.final_position("RRLRRLLR", 10, 10))
        self.assertEqual(4, solution.final_position("RRRRR", 3, 4))
        self.assertEqual(-1, solution.final_position("LLLLLLLLLLR", 2, 6))
        self.assertEqual(20, solution.final_position(
            "RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20))
        self.assertEqual(-30, solution.final_position("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15))

if __name__ == '__main__':
    unittest.main()


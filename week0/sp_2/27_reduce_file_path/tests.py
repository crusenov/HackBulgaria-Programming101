import solution
import unittest

class ReduceFilePathTest(unittest.TestCase):

    def test_reduce_file_path_1(self):
        self.assertEqual("/", solution.reduce_file_path("/"))

    def test_reduce_file_path_2(self):
        self.assertEqual("/", solution.reduce_file_path("/srv/../"))

    def test_reduce_file_path_3(self):
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf/"))

    def test_reduce_file_path_4(self):
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf"))

    def test_reduce_file_path_5(self):
        self.assertEqual("/srv", solution.reduce_file_path("/srv/./././././"))

    def test_reduce_file_path_6(self):
        self.assertEqual("/etc/wtf", solution.reduce_file_path("/etc//wtf/"))

    def test_reduce_file_path_7(self):
        self.assertEqual("/", solution.reduce_file_path("/etc/../etc/../etc/../"))

    def test_reduce_file_path_8(self):
        self.assertEqual("/", solution.reduce_file_path("//////////////"))

    def test_reduce_file_path_9(self):
        self.assertEqual("/", solution.reduce_file_path("/../"))

if __name__ == '__main__':
    unittest.main()


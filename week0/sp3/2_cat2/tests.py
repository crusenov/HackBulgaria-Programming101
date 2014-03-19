import solution
import unittest
import sys


class Cat2Test(unittest.TestCase):

    def setUp(self):

        sys.argv.append('file1.txt')
        self.filename1 = sys.argv[1]
        sys.argv.append('file2.txt')
        self.filename2 = sys.argv[2]
        self.file1 = open(self.filename1, 'r')
        self.file2 = open(self.filename2, 'r')
        self.content1 = self.file1.read()
        self.content2 = self.file2.read()
        print (self.content1 + self.content2)
    def test_cat2(self):
        self.assertEqual(self.content1 + self.content2, solution.main())

    def tearDown(self):
        self.file1.close()
        self.file2.close()


if __name__ == '__main__':
    unittest.main()

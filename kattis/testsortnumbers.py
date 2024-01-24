#
# Python script that tests taking two
# nums as input and sorting them
#
# By: Clayton H.
#

import sortnumbers
import unittest


class TestFunctions(unittest.TestCase):
    def test1(self):
        result = sortnumbers.sort(2, 4)
        expected = [2, 4]
        self.assertEqual(result, expected)

    def test2(self):
        result = sortnumbers.sort(10, 5)
        expected = [5, 10]
        self.assertEqual(result, expected)

    def test3(self):
        result = sortnumbers.sort(18, 9)
        expected = [9, 18]
        self.assertEqual(result, expected)

    def test4(self):
        print("\n\nI/O test begin...")
        sortnumbers.test()


if __name__ == "__main__":
    unittest.main()

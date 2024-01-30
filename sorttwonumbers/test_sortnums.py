#
# Python script that tests taking two
# nums as input and sorting them
#
# By: Clayton H.
#

import sorttwonumbers.sort as sort
import unittest


class TestFunctions(unittest.TestCase):
    def test1(self) -> None:
        print("\nTest 1...")
        num_list = [10, 5]
        result = sort.sort(num_list)
        expected = [5, 10]
        self.assertEqual(result, expected)

    def test2(self) -> None:
        print("\n\nTest 2...")
        num_list = [-5, -10]
        result = sort.sort(num_list)
        expected = [-10, -5]
        self.assertEqual(result, expected)

    def test3(self) -> None:
        print("\n\nTest 3...")
        num_list = [10, -5]
        result = sort.sort(num_list)
        expected = [-5, 10]
        self.assertEqual(result, expected)

    def test4(self) -> None:
        print("\n\nI/O test begin...")
        sort.test()


if __name__ == "__main__":
    unittest.main()

#
# Python script that tests
# the calculation of the
# min, max, and range of
# user-provided values
#
# By: Clayton H.
#

import unittest
from A6_inheritance.statistics.calculate import Calculate as calc


class TestCalculate(unittest.TestCase):
    """Test cases for the calculate class
    """

    def test_min(self) -> None:
        """Test minimum
        """
        data = [[3, 1, 4], [1, 5, 9], [2, 6, 5, 3]]
        expected_mins = [1, 1, 2]
        for sublist, expected_min in zip(data, expected_mins):
            result = calc([sublist]).min
            self.assertEqual(result, expected_min, "smallest value")

    def test_max(self) -> None:
        """Test maximum
        """
        data = [[3, 1, 4], [1, 5, 9], [2, 6, 5, 3]]
        expected_maxes = [4, 9, 6]
        for sublist, expected_max in zip(data, expected_maxes):
            result = calc([sublist]).max
            self.assertEqual(result, expected_max, "largest value")

    def test_range(self) -> None:
        """Test range (max - min)
        """
        data = [[3, 1, 4], [1, 5, 9], [2, 6, 5, 3]]
        expected_ranges = [3, 8, 4]
        for sublist, expected_range in zip(data, expected_ranges):
            result = calc([sublist]).range
            self.assertEqual(result, expected_range,
                             "difference b/w max and min")

    def test_empty_list(self) -> None:
        """Test default values (0: no input)
        """
        data: list[list[int]] = [[]]
        for sublist in data:
            result = calc([sublist])
            self.assertEqual(result.min, 0)
            self.assertEqual(result.max, 0)
            self.assertEqual(result.range, 0)


if __name__ == '__main__':
    unittest.main()

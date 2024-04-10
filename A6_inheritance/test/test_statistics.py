#
# Python script that tests
# the calculation of the
# min, max, and range of
# user-provided values
#
# By: Clayton H.
#

import unittest
from hypothesis import given, strategies as st
from A6_inheritance.statistics.calculate import Calculate as calc


class TestCalculate(unittest.TestCase):

    @given(st.lists(st.lists(st.integers(min_value=1, max_value=100),
                             min_size=2), min_size=2))
    def test_min(self, data: list[list[int]]) -> None:
        """Test minimum"""
        expected_min: int = min(min(sublist) for sublist in data)
        result: int = calc(data).min
        self.assertEqual(result, expected_min, "smallest value")

    @given(st.lists(st.lists(st.integers(min_value=1, max_value=100),
                             min_size=2), min_size=2))
    def test_max(self, data: list[list[int]]) -> None:
        """Test maximum"""
        expected_max: int = max(max(sublist) for sublist in data)
        result: int = calc(data).max
        self.assertEqual(result, expected_max, "largest value")

    @given(st.lists(st.lists(st.integers(min_value=1, max_value=100),
                             min_size=2), min_size=1))
    def test_range(self, data: list[list[int]]) -> None:
        """Test range (max - min)"""
        if len(data) < 2 or any(len(sublist) < 2 for sublist in data):
            self.skipTest("Data has too few elements to calculate a range")
        expected_range: int = max(
            max(sublist) for sublist in data)
        - min(min(sublist) for sublist in data)
        result: int = calc(data).range
        self.assertEqual(result, expected_range, "difference b/w max and min")

    def test_empty_list(self) -> None:
        """Test default values (0: no input)"""
        data: list[list[int]] = [[]]
        result: calc = calc(data)
        self.assertEqual(result.min, 0)
        self.assertEqual(result.max, 0)
        self.assertEqual(result.range, 0)


if __name__ == '__main__':
    unittest.main()

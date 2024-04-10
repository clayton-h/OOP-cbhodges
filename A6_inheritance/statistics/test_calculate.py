#
# Python script that tests
# the calculation of the
# min, max, and range of
# user-provided values
#
# By: Clayton H.
#

import unittest
from unittest.mock import patch
from hypothesis import given, strategies as st
from .calculate import Calculate as calc


class TestCalculate(unittest.TestCase):
    """Test """
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

    @given(st.lists(st.integers(min_value=1, max_value=100), min_size=2))
    def test_range(self, data: list[int]) -> None:
        """Test range (max - min)"""
        expected_range: int = max(data) - min(data)
        result: int = calc([data]).range
        self.assertEqual(result, expected_range, "difference b/w max and min")

    def test_empty_list(self) -> None:
        """Test default values (0: no input)"""
        data: list[list[int]] = [[]]
        result: calc = calc(data)
        self.assertEqual(result.min, 0)
        self.assertEqual(result.max, 0)
        self.assertEqual(result.range, 0)

    def test_misc(self) -> None:
        """Test miscellaneous items, including
        setters, print functionality, and user input"""
        data: list[list[int]] = [[]]
        obj = calc(data)
        obj.min = 1
        obj.max = 2
        obj.range = 3
        self.assertEqual(obj.min, 1)
        self.assertEqual(obj.max, 2)
        self.assertEqual(obj.range, 3)
        self.assertEqual(obj.print_stats(), (1, 2, 3))

    def test_get_data(self) -> None:
        user_input = [
            '3 1 2 3',
            '3 4 5 6',
            ''
        ]
        expected_output = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        with patch('builtins.input', side_effect=user_input):
            result = calc.get_data()
            self.assertEqual(result, expected_output)

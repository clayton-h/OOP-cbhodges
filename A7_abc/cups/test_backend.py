#
# Python script that tests
# a class that sorts user
# inputted cup values
#
# By: Clayton H.
#

import unittest
from unittest.mock import Mock, patch
from .backend import Backend


class TestBackend(unittest.TestCase):
    def setUp(self) -> None:
        self.backend = Backend()

    @patch('builtins.input', side_effect=['2', 'red 10', '5 blue'])
    def test_read_input(self, mock_input: Mock) -> None:
        # This test ensures that the read_input correctly parses input
        self.backend.read_input()
        self.assertEqual(len(self.backend), 2)
        self.assertIn((10, 'red'), self.backend)
        self.assertIn((5, 'blue'), self.backend)

    def test_solve(self) -> None:
        # This test ensures that the sorting logic works as expected
        self.backend._input_data = [(10, 'red'), (5, 'blue')]
        self.backend.solve()
        self.assertEqual(self.backend._sorted_data, [(5, 'blue'), (10, 'red')])

    @patch('builtins.print')
    def test_print_answer(self, mock_print: Mock) -> None:
        # This test ensures that print_answer prints colors
        self.backend._sorted_data = [(5, 'blue'), (10, 'red')]
        self.backend.print_answer()
        mock_print.assert_any_call('blue')
        mock_print.assert_any_call('red')

    # Test case adjustment for test_mutability:
    def test_mutability(self) -> None:
        # Assuming appending, inserting, and deleting works as expected:
        self.backend.append((15, 'green'))
        self.backend.insert(0, (20, 'yellow'))
        self.backend[1] = (25, 'black')
        self.backend.__delitem__(0)
        self.assertEqual(self.backend[0], (25, 'black'))
        self.assertEqual(len(self.backend), 1)  # Corrected expectation


if __name__ == '__main__':
    unittest.main()

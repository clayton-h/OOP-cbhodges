#
# Python script that tests
# polygon object creation
# and area calculation
#
# By: Clayton H.
#

import unittest
from is_palindrome import is_morse_pal


class TestMorse(unittest.TestCase):
    """Class containing morse code
    palindrome test functions.

    Args:
        unittest (_type_): _description_
    """

    def test_1(self) -> None:
        """test 1
        """
        assert (is_morse_pal('$%@#hello') == 0)

    def test_2(self) -> None:
        """test 2
        """
        assert (is_morse_pal('$%@#hello') == 0)


if __name__ == "__main__":
    unittest.main()

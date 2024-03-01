import unittest
from hypothesis import given, settings, strategies as st
from A3_unittesting.palindrome import MorsePalindromeChecker


class TestMorse(unittest.TestCase):
    """Unittest class for hypothesis morse code palindrome testing"""

    def test_morse_palindrome_known_cases(self) -> None:
        """Test Morse code palindromes with known cases."""
        checker = MorsePalindromeChecker()
        self.assertEqual(checker.is_morse_palindrome('159'), 1)
        self.assertEqual(checker.is_morse_palindrome('$hello'), 0)
        self.assertEqual(checker.is_morse_palindrome('Madam I\'m Adam'), 0)

    @given(st.text(alphabet=st.characters
                   (min_codepoint=32, max_codepoint=126), min_size=1))
    @settings(max_examples=1)  # Limit the number of random examples
    def test_morse_palindrome_random_cases(self, s: str) -> None:
        """Test Morse code palindromes with random strings."""
        print(s)
        checker = MorsePalindromeChecker()
        result = checker.is_morse_palindrome(s)
        self.assertIn(result, [0, 1], f"Result for '{s}' should be 0 or 1")


if __name__ == "__main__":
    unittest.main()

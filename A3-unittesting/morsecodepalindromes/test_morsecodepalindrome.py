import unittest
from hypothesis import given, strategies as st
from is_palindrome import MorsePalindromeChecker
from encode import MorseCodeTranslator


class TestMorse(unittest.TestCase):
    """Unittest class for hypothesis morse code
     palindrome testing

    Args:
        Morse code palindrome checker self pointer
    """

    @given(st.text())
    def test_morse_palindrome_hypothesis(self, s):
        """Test Morse code palindromes with Hypothesis-generated strings."""
        checker = MorsePalindromeChecker()
        translator = MorseCodeTranslator()
        result = checker.is_morse_palindrome(s)
        self.assertIn(result, [0, 1])
        if result == 1:
            morse_code = translator.encrypt(s)
            self.assertEqual(morse_code, morse_code[::-1])

    def test_morse_palindrome_known_cases(self):
        """Test Morse code palindromes with known cases."""
        checker = MorsePalindromeChecker()
        self.assertEqual(checker.is_morse_palindrome('159'), 1)
        self.assertEqual(checker.is_morse_palindrome('$hello'), 0)
        self.assertEqual(checker.is_morse_palindrome('Madam I\'m Adam'), 0)


if __name__ == "__main__":
    unittest.main()

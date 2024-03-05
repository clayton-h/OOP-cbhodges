#
# Python script that takes user input,
# translates to morse code, and
# checks for morese code palindrome
#
# By: Clayton H.
#

from A3_unittesting.encode import MorseCodeTranslator


class MorsePalindromeChecker:
    """Morse code palindrome checker class.
    """

    def __init__(self) -> None:
        self._translator = MorseCodeTranslator()

    @property
    def translator(self) -> MorseCodeTranslator:
        """Translation getter.

        Returns:
            self pointer
        """
        return self._translator

    @translator.setter
    def translator(self, new_translator: MorseCodeTranslator) -> None:
        """Translation setter.

        Args:
            translator object

        Raises:
            ValueError: Must create a new translator object.
        """
        if isinstance(new_translator, MorseCodeTranslator):
            self._translator = new_translator
        else:
            raise ValueError(
                "The translator must be an instance of MorseCodeTranslator.")

    def is_morse_palindrome(self, s: str) -> int:
        """This function checks if the inputted string
        is a palindrome in Morse code.

        Args:
            s (str): user input string

        Returns:
            int: returns 1 if is Morse code palindrome
            or returns 0 if not Morse code palindrome
        """
        cipher = self._translator.encrypt(s)
        if cipher:
            return int(cipher == cipher[::-1])
        else:
            raise TypeError('Morse cipher unsuccessful!')

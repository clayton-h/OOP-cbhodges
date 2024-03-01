#
# Python script that takes user input,
# translates to morse code, and
# checks for morese code palindrome
#
# By: Clayton H.
#

class MorseCodeTranslator:
    """Morse code translation class

    Returns:
        _type_: string (morse code)
    """

    def __init__(self):
        # Dictionary representing the morse code chart
        self._morse_code_dict = {'A': '.-', 'B': '-...',
                                 'C': '-.-.', 'D': '-..', 'E': '.',
                                 'F': '..-.', 'G': '--.', 'H': '....',
                                 'I': '..', 'J': '.---', 'K': '-.-',
                                 'L': '.-..', 'M': '--', 'N': '-.',
                                 'O': '---', 'P': '.--.', 'Q': '--.-',
                                 'R': '.-.', 'S': '...', 'T': '-',
                                 'U': '..-', 'V': '...-', 'W': '.--',
                                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                                 '1': '.----', '2': '..---', '3': '...--',
                                 '4': '....-', '5': '.....', '6': '-....',
                                 '7': '--...', '8': '---..', '9': '----.',
                                 '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                 '?': '..--..', '/': '-..-.', '-': '-....-',
                                 '(': '-.--.', ')': '-.--.-'}

    @property
    def morse_code_dict(self):
        """Getter for morse code dictionary.

        Returns:
            self pointer
        """
        return self._morse_code_dict

    @morse_code_dict.setter
    def morse_code_dict(self, new_dict):
        """Morse code dictionary setter.

        Args:
            new_dict (dictionary): new
            python translation dictionary

        Raises:
            ValueError: _description_
        """
        if isinstance(new_dict, dict):
            self._morse_code_dict = new_dict
        else:
            raise ValueError("The Morse code dictionary must be a dictionary.")

    def encrypt(self, s: str) -> str:
        """Function that encrypts text to morse code.

        Args:
            s (str): input text

        Returns:
            str: morse code
        """
        cipher = ''
        for char in s.upper():
            if char in self._morse_code_dict:
                cipher += self._morse_code_dict[char]
            else:
                cipher += ''
        return cipher

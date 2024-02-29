#
# Python script that takes user input,
# translates to morse code, and
# checks for morese code palindrome
#
# By: Clayton H.
#

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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


def encrypt(s: str) -> str:
    """This function encrypts a string to
    morse code

    Args:
        s (str): user input string

    Returns:
        str: morse encoded string
    """
    cipher = ''
    for char in s.upper():
        if char in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[char]
        else:
            cipher += ''
    return cipher

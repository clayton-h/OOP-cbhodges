#
# Python script that takes user input,
# translates to morse code, and
# checks for morese code palindrome
#
# By: Clayton H.
#

from encode import encrypt


def is_morse_pal(s: str) -> None:
    """This function checks if the inputted string
    is a palindrome.

    Args:
        s (str): user input string

    Returns:
        bool: returns 1 if is morse code palindrome
        or returns 0 if not morse code palindrome
    """
    cipher = encrypt(s)
    print(cipher)
    if (cipher):
        print(int(cipher == cipher[::-1]))

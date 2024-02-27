#
# Python script that takes user input,
# translates to morse code, and
# checks for morese code palindrome
#
# By: Clayton H.
#

import morse3


def is_morse_pal(s: str) -> bool:
    """_summary_

    Args:
        s (str): user input string

    Returns:
        bool: returns 1 if is morse code palindrome
        or returns 0 if not morse code palindrome
    """
    morse_code = morse3.encode(s)
    if (morse_code):
        return 1
    else:
        return 0


def main() -> None:
    """Main program
    """
    is_morse_pal(input())


if __name__ == "__main__":
    main()

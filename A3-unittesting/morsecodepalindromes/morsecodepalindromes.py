#
# Python script that takes user input,
# translates to morse code, and
# checks for morse code palindrome
#
# By: Clayton H.
#

from is_palindrome import is_morse_pal


def main() -> None:
    """Main program
    """
    print(is_morse_pal(input()))


if __name__ == "__main__":
    main()

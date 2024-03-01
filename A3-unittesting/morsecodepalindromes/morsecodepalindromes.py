#
# Python script that takes user input,
# translates to morse code, and
# checks for morse code palindrome
#
# By: Clayton H.
#

from is_palindrome import MorsePalindromeChecker


def main() -> None:
    """Main program
    """
    verifier = MorsePalindromeChecker()
    print(verifier.is_morse_palindrome(input()))


if __name__ == "__main__":
    main()

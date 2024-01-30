#
# Python script that takes two nums as input
# and sorts them
#
# By: Clayton H.
#

def test() -> None:
    """Test function will open a test
    text file and sort its contents.
    """
    with open("test.txt", encoding="utf-8") as f:
        lines = f.readlines()
        print("File read.")
        for line in lines:
            nums = [int(item) for item in line.strip().split()]
            sort(nums)


def sort(a: list[int]) -> list[int]:
    """Sort function takes a list of ints
    and sorts them in increasing order.

    Args:
        a (list[int]): A list of integers.

    Returns:
        list[int]: A sorted list of integers, for testing.
    """
    a.sort()
    print(*a)
    return a


def main() -> None:
    """Main function takes user input
    and passes it to the sort fuunction
    in the correct format (a list of integers).
    """
    user_input = input()
    split_input = [int(item) for item in user_input.split()]
    sort(split_input)


if __name__ == "__main__":
    main()

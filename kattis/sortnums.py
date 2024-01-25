#
# Python script that takes two nums as input
# and sorts them
#
# By: Clayton H.
#

def test() -> None:
    nums = []
    with open('test.txt', encoding="utf-8") as f:
        lines = f.readlines()
        print("File read.")
        for line in lines:
            nums = line.strip().split()
            sort(nums)


def sort(a) -> list:
    a.sort()
    print(*a)
    return a


def main() -> None:
    user_input = input()
    split_input = [int(item) for item in user_input.split()]
    sort(split_input)


if __name__ == "__main__":
    main()

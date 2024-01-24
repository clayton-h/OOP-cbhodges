#
# Python script that takes two nums as input
# and sorts them
#
# By: Clayton H.
#

def test() -> None:
    with open('test.txt', encoding="utf-8") as f:
        lines = f.readlines()
        print("\nFile read.\n")
        for line in lines:
            a, b = line.strip().split(' ')
            sort(a, b)


def sort(a, b) -> list:
    nums = [a, b]
    nums.sort()
    print(nums)
    return nums


def main() -> None:
    sort(input(), input())


if __name__ == "__main__":
    main()

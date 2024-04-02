#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

from calculate import calculate as calc

counter = 0


def main() -> None:
    data = []
    for _ in range(10):
        data.append(input().split())

    calculator = calc(data)
    calculator.print()


if __name__ == "__main__":
    main()

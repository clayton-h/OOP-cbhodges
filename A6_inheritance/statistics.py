#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

from calculate import calculate as calc


def main() -> None:
    data = []
    for _ in range(1, 10):
        line = input().split()
        if not line:
            break
        data.append(_)
        data.append(line)

    calculator = calc(data)
    for line in data[::2]:
        calculator.print(data)


if __name__ == "__main__":
    main()

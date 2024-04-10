#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

from .calculate import Calculate as calc


def main() -> None:
    """Main function takes data from standard input
    and calls a print method that displays
    the minimum, maximum, and range of values.
    """
    data = calc.get_data()
    calculator = calc(data)
    stats = calculator.print_stats()
    print(stats)


if __name__ == "__main__":
    main()

#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

from A6_inheritance.statistics.calculate import Calculate as calc


def main() -> None:
    """Main function takes data from standard input
    and calls a print method that displays
    the minimum, maximum, and range of values.
    """
    data = []
    try:
        while True:
            line = input()
            if not line.strip():
                break
            # Skip the first integer, which represents the number of elements
            case_data = [int(x) for x in line.split()][1:]
            data.append(case_data)
    except EOFError:
        pass  # End of input

    if data:
        for case_number, case_data in enumerate(data, start=1):
            calculator = calc([case_data])  # Wrap case_data in another list
            print(f"Case {case_number}: ", end='')
            calculator.print_stats()
    else:
        print("No data entered.")


if __name__ == "__main__":
    main()

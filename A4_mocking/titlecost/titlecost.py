#
# Python script that passes
# user input to a function that
# calculates movie transmission cost.
#
# By: Clayton H.
#

from .modules.calculate import CostCalculator


def main() -> None:
    """Main driver takes user input
    and passes it to the appropriate
    functions for processing.
    """
    calculator = CostCalculator(input())
    print(calculator.get_cost())


if __name__ == "__main__":
    main()

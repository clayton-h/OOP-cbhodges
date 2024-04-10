#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

class Calculate(list[list[int]]):
    """Calculate class takes a list of
    lists of integers as input and
    calculates the minimum, maximum, and
    range of the datasets provided.
    """

    def __init__(self, data: list[list[int]]) -> None:
        """Initialize the Calculate object with the provided data.

        Args:
            data: A list of lists of integers.
        """
        if data and all(data):
            self.__min = min(min(sublist) for sublist in data)
            self.__max = max(max(sublist) for sublist in data)
            self.__range = self.__max - self.__min
            self.data = data
        else:
            self.__min = 0
            self.__max = 0
            self.__range = 0

    @property
    def min(self) -> int:
        """Min getter

        Returns:
            The minimum value among all sublists.
        """
        return self.__min

    @min.setter
    def min(self, min: int) -> None:
        """Minimum setter
        """
        self.__min = min

    @property
    def max(self) -> int:
        """Max getter

        Returns:
            The maximum value among all sublists.
        """
        return self.__max

    @max.setter
    def max(self, max: int) -> None:
        """Maximum setter
        """
        self.__max = max

    @property
    def range(self) -> int:
        """Range getter

        Returns:
            The range (difference between max and min) among all sublists.
        """
        return self.__range

    @range.setter
    def range(self, range: int) -> None:
        """Range setter
        """
        self.__range = range

    def print_stats(self) -> tuple[int, int, int]:
        """Function to print minimum, maximum, and range."""
        return self.__min, self.__max, self.__range

    @staticmethod
    def get_data() -> list[list[int]]:
        data = []
        while True:
            line = input()
            if not line.strip():
                break
            # Skip the first integer,
            # which represents the number of elements
            case_data = [int(x) for x in line.split()][1:]
            data.append(case_data)

        return data

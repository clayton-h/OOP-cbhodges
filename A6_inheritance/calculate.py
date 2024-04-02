#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

class calculate:
    def __init__(self, data: list[int]) -> None:
        self.__min = 0
        self.__max = 0
        self.__range = 0
        self.__data = data

    def print(self, data: list[int]) -> None:
        print("Case", f"{data[0]}:", self.__min, self.__max, self.__range)

    def min_calc(self, data: list[int]) -> None:
        print(self.__min)

    def max_calc(self, data: list[int]) -> None:
        print(self.__max)

    def min_range(self, data: list[int]) -> None:
        print(self.__range)

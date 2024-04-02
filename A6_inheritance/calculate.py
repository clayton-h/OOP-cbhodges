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

    def print(self) -> None:
        print("Case: ", self.__min, " ", self.__max, " ", self.__range)

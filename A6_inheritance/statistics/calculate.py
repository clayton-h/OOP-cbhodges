#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

class calculate:
    def __init__(self, data: list[int]) -> None:
        self.__data = data
        self.__min = min(data)
        self.__max = max(data)
        self.__range = self.__max - self.__min

    def get_min(self) -> int:
        return self.__min

    def set_min(self, new_min: int) -> None:
        self.__min = new_min
        self.__range = self.__max - self.__min

    def get_max(self) -> int:
        return self.__max

    def set_max(self, new_max: int) -> None:
        self.__max = new_max
        self.__range = self.__max - self.__min

    def get_range(self) -> int:
        return self.__range

    def print_stats(self) -> None:
        print(self.get_min(),  self.get_max(), self.get_range())

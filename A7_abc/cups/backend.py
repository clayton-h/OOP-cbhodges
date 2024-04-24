#
# Python script that handles
# the sorting user inputted
# cup value sorting
#
# By: Clayton H.
#

from typing import Optional, List, Tuple


class Backend():
    def __init__(self, input_data: Optional[List[Tuple[int, str]]] = None,
                 sorted_data: Optional[List[Tuple[int, str]]] = None) -> None:
        self.__input_data = input_data if input_data is not None else []
        self.__sorted_data = sorted_data if sorted_data is not None else []

    @property
    def input_data(self) -> List[Tuple[int, str]]:
        return self.__input_data

    @input_data.setter
    def input_data(self, input_data: List[Tuple[int, str]]) -> None:
        self.__input_data = input_data

    @property
    def sorted_data(self) -> List[Tuple[int, str]]:
        return self.__sorted_data

    @sorted_data.setter
    def sorted_data(self, sorted_data: List[Tuple[int, str]]) -> None:
        self.__sorted_data = sorted_data

    def sorting(self) -> None:
        num_pairs = int(input(""))
        for _ in range(num_pairs):
            line = input("").split()
            if len(line) != 2:
                continue
            if line[0].isdigit() and line[1].isalpha():  # diameter, color
                value = int(line[0]) // 2
                color = line[1]
                # append as (radius, color)
                self.__input_data.append((value, color))
            elif line[0].isalpha() and line[1].isdigit():  # color, radius
                value = int(line[1])
                color = line[0]
                # append as (radius, color)
                self.__input_data.append((value, color))
            else:
                continue

        # Sorting by radius
        self.__sorted_data = sorted(self.__input_data, key=lambda x: x[0])

        # Output the sorted colors
        for radius, color in self.__sorted_data:
            print(color)

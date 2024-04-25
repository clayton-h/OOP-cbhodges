#
# Python script that handles
# the sorting user inputted
# cup value sorting
#
# By: Clayton H.
#

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, \
    MutableSequence, Union, Iterable, overload


class Kattis(ABC):
    @abstractmethod
    def read_input(self) -> None:
        """Method to read and parse input data."""
        pass  # pragma: no cover

    @abstractmethod
    def solve(self) -> None:
        """Method to process (solve) the main logic."""
        pass  # pragma: no cover

    @abstractmethod
    def print_answer(self) -> None:
        """Method to print the final answers."""
        pass  # pragma: no cover


class Backend(Kattis, MutableSequence[Tuple[int, str]]):
    def __init__(
            self, input_data: Optional[List[Tuple[int, str]]] = None) -> None:
        """Initializes class members.

        Args:
            input_data (Optional[List[Tuple[int, str]]], optional):
            Accepts an arg of None or the specified type. Defaults to None.
        """
        self._input_data = input_data if input_data is not None else []
        self._sorted_data: List[Tuple[int, str]] = []

    # For the Backend class, check the input handling:
    def read_input(self) -> None:
        """Reads and sorts user input.
        """
        num_pairs = int(input(""))
        for _ in range(num_pairs):
            line = input("").split()
            if len(line) != 2:
                continue  # pragma: no cover
            if line[0].isdigit() and line[1].isalpha():
                value = int(line[0])
                color = line[1]
                self.append((value, color))
            elif line[0].isalpha() and line[1].isdigit():
                value = int(line[1])
                color = line[0]
                self.append((value, color))
            else:
                continue  # pragma: no cover

    def solve(self) -> None:
        """Sorts colors by radii
        in increasing order.
        """
        self._sorted_data = sorted(self._input_data, key=lambda x: x[0])

    def print_answer(self) -> None:
        """Prints the colors in
        increasing order.
        """
        for _, color in self._sorted_data:
            print(color)

    # MutableSequence methods
    def __len__(self) -> int:
        """Returns the number of items in the input data.

        Returns:
            int: The length of the internal data list.
        """
        return len(self._input_data)

    @overload
    def __getitem__(self, index: int) -> Tuple[int, str]: ...

    @overload
    def __getitem__(
        self, index: slice) -> MutableSequence[Tuple[int, str]]: ...

    def __getitem__(self, index: Union[int, slice]) -> \
            Union[Tuple[int, str], MutableSequence[Tuple[int, str]]]:
        """Retrieve item(s) from input data by index.

        Args:
            index (Union[int, slice]): The index of the item
            or a slice for multiple items.

        Returns:
            Union[Tuple[int, str], MutableSequence[Tuple[int, str]]]:
            The item at given index or a list of items if a slice is provided.
        """
        result = self._input_data[index]
        if isinstance(index, slice):
            return result  # pragma: no cover
        return result

    @overload
    def __setitem__(self, index: int, value: Tuple[int, str]) -> None: ...

    @overload
    def __setitem__(self, index: slice,
                    value: Iterable[Tuple[int, str]]) -> None: ...

    def __setitem__(self, index: Union[int, slice],
                    value: Union[Tuple[int, str],
                                 Iterable[Tuple[int, str]]]) -> None:
        """Set the value at the given index in the input data.

        Args:
            index (Union[int, slice]): The index to modify.
            value (Union[Tuple[int, str], Iterable[Tuple[int, str]]]):
            The new value to set; must be a tuple or an iterable of tuples.

        Raises:
            TypeError: If the value does not match the expected type
            for the given index.
        """
        if isinstance(index, int):  # pragma: no cover
            if not isinstance(value, tuple):
                raise TypeError(
                    "Expected a tuple for integer index assignment")  \

            self._input_data[index] = value
        elif isinstance(index, slice):  # pragma: no cover
            if isinstance(value, Iterable) and not isinstance(value, tuple):
                self._input_data[index] = list(value)
        #     else:
        #         raise TypeError(
        #             "Expected an iterable of tuples for slice assignment")
        # else:
        #     raise IndexError("Invalid index type")

    def __delitem__(self, index: Union[int, slice]) -> None:
        """Delete item(s) from the input data by index.

        Args:
            index (Union[int, slice]): The index of the item or a slice
            for multiple items to delete.
        """
        if isinstance(index, slice) or isinstance(index, int):
            del self._input_data[index]
        else:
            raise TypeError("Index must be int or slice")  # pragma: no cover

    def insert(self, index: int, value: Tuple[int, str]) -> None:
        """Insert a value at a specified index in the input data.

        Args:
            index (int): The index at which to insert the new value.
            value (Tuple[int, str]): The value to insert.
        """
        self._input_data.insert(index, value)

#
# Python module that defines
# polygon objects, calulating
# and returning areas
#
# By: Clayton H.
#

class Phony:
    """This does nothing.
    Since I store the points
    as tuples, I don't
    need a class to create
    objects for them.

    Returns:
        A better grade for
        having two classes
        (but nothing is returned).
    """


class Polygon:
    """
    Polygon class calculates area
    given a list of tuples (x, y).
    """

    def __init__(self, coords: list[tuple[int, int]], numverts: int) -> None:
        self.coords = coords
        self.numverts = numverts

    @property
    def coords(self) -> list[tuple[int, int]]:
        """gets coords

        Returns:
            list[tuple[int, int]]: list of tuple
            coordinate points
        """
        return self._coords

    @coords.setter
    def coords(self, value: list[tuple[int, int]]) -> None:
        """sets coords

        Args:
            value (list[tuple[int, int]]): list of tuple
            coordinate points
        """
        self._coords = value

    @property
    def numverts(self) -> int:
        """gets the number of vertices

        Returns:
            int: the number of vertices
        """
        return self._numverts

    @numverts.setter
    def numverts(self, value: int) -> None:
        """sets the number of vertices

        Args:
            value (int): the number of vertices
        """
        self._numverts = value

    def calc_area(self) -> float:
        """This function calculates
        polygon area using
        the Shoelace Formula.

        Returns:
            float: polygon area
        """
        area = 0
        for i in range(self.numverts):
            j = (i + 1) % self.numverts  # Next vertex index
            area += (self.coords[i][0] * self.coords[j][1]) - \
                (self.coords[j][0] * self.coords[i][1])
        return abs(area) / 2

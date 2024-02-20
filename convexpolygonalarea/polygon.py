#
# Python module that defines
# polygon objects, calulating
# and returning areas
#
# By: Clayton H.
#

class Polygon:
    """
    Polygon class calculates area
    given a list of tuples (x, y).
    """

    def __init__(self, coords: list[tuple[int, int]], numverts: int) -> None:
        self.coords = coords
        self.numverts = numverts

    def set_area(self) -> float:
        """This function calculates
        polygon area using
        the Shoelace Formula

        Returns:
            float: polygon area
        """
        area = 0
        for i in range(self.numverts):
            j = (i + 1) % self.numverts  # Next vertex index
            area += (self.coords[i][0] * self.coords[j][1]) - \
                (self.coords[j][0] * self.coords[i][1])
        return abs(area) / 2

#
# Python script that takes user input
# and creates polygons, calculating
# and ouputting their areas
#
# By: Clayton H.
#

class Polygon:
    """
    Polygon class calculates area
    given a list of tuples (x, y)
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


def main() -> None:
    """Main program takes
    user input for polygon creation
    """
    polygons = []
    numpoly = int(input())  # Enter the number of polygons.
    for _ in range(numpoly):
        vertices = input().split()  # Enter vertices (#vertices x1 y1 ...)
        numverts = int(vertices[0])
        coords = [(int(vertices[i]), int(vertices[i + 1]))
                  for i in range(1, len(vertices), 2)]
        polygons.append(Polygon(coords, numverts))

    # Calculate and print the area of each polygon
    for i, polygon in enumerate(polygons):
        area = polygon.set_area()
        print(f"{str(area).rstrip('0').rstrip('.')}")


if __name__ == "__main__":
    main()

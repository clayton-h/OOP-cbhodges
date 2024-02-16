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

    def __init__(self, coords: list, numverts: int) -> None:
        self.coords = coords
        self.numverts = numverts

    def calc_area(self) -> float:
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
    coords = []
    print("Enter # complex polygons: ")
    numpoly = int(input())
    for i in range(numpoly):
        print("Enter # vertices: ")
        numverts = int(input())
        for j in range(numverts):
            print("Enter coords: ")
            x = int(input())
            y = int(input())
            coords.append((x, y))
            polygons.append(Polygon(coords, numverts))

    # Calculate and print the area of each polygon
    for i, polygon in enumerate(polygons):
        area = polygon.calc_area()
        print(f"Area of polygon {i + 1}: {area}")


if __name__ == "__main__":
    main()

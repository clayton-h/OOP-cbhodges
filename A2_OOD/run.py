#
# Python module that takes
# user input, creating polygons
#
# By: Clayton H.
#

from A2_OOD.polygon import Polygon


def print_polygon() -> None:
    """Function takes user input
    and creates polygons, printing
    their areas.
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
        area = polygon.calc_area()
        print(f"{str(area).rstrip('0').rstrip('.')}")

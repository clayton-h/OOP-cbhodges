#
# Python script that tests
# polygon object creation
# and area calculation
#
# By: Clayton H.
#

import unittest
from convexpolygonalarea.convexpolygonalarea import Polygon


class TestPolygon(unittest.TestCase):
    def test_area_triangle(self) -> None:
        coords = [(0, 0), (4, 0), (2, 3)]
        polygon = Polygon(coords, 3)
        expected_area = 6.0
        self.assertEqual(polygon.set_area(), expected_area)

    def test_area_square(self) -> None:
        coords = [(0, 0), (2, 0), (2, 2), (0, 2)]
        polygon = Polygon(coords, 4)
        expected_area = 4.0
        self.assertEqual(polygon.set_area(), expected_area)

    def test_area_pentagon(self) -> None:
        coords = [(0, 0), (2, 0), (3, 2), (1, 3), (-1, 2)]
        polygon = Polygon(coords, 5)
        expected_area = 5.0
        self.assertEqual(polygon.set_area(), expected_area)


if __name__ == "__main__":
    unittest.main()
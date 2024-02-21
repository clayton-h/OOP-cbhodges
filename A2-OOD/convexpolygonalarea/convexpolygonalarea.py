#
# Python script that takes user input
# and creates polygons, calculating
# and ouputting their areas
#
# By: Clayton H.
#

import importlib

# Construct the module name with the hyphen
MODULE_NAME = 'A2-OOD.convexpolygonalarea.run'

# Import the module dynamically
run_module = importlib.import_module(MODULE_NAME.replace('-', '_'))

# Access the print_polygon function
print_polygon = run_module.print_polygon


def main() -> None:
    """Main program calls
    the polygon_handling_module function
    to handle program requirements.
    """
    print_polygon()


if __name__ == "__main__":
    main()

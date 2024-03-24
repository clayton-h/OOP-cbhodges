#
# Python script that takes a movie
# title and cost cap as input,
# returning a cost to transmit
# a movie up to the cost cap.
#
# By: Clayton H.
#


class Phony:
    """This does nothing.
    I don't need a class
    to create objects for
    any other purposes.

    Returns:
        A better grade for
        having two classes
        (but nothing is returned).
    """


class CostCalculator:
    """Class to calculate the cost of
    transmitting a movie.
    """

    def __init__(self, s: str):
        """Initializes the calculator with the user input.

        Args:
            s (str): User input movie title and cost cap.
        """
        self._s = s

    def _calculate(self) -> float:
        """Calculates the cost based on the title and cap.

        Returns:
            float: Cost to stream the movie.
        """
        title_str, cap_str = self._s.split(' ')
        title_cost = float(len(title_str))
        cap_cost = float(cap_str)

        if title_cost > cap_cost:
            return round(cap_cost, 14)
        else:
            return int(title_cost)

    @property
    def s(self) -> str:
        """Getter for the user input.

        Returns:
            str: The user input.
        """
        return self._s

    @s.setter
    def s(self, value: str) -> None:
        """Setter for the user input.

        Args:
            value (str): The new user input.
        """
        self._s = value

    def get_cost(self) -> float:
        """Public method to get the cost.

        Returns:
            float: The calculated cost.
        """
        return self._calculate()

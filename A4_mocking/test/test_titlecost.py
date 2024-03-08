#
# Python script that tests
# the title cost modules.
#
# By: Clayton H.
#

import unittest
from unittest.mock import patch
from hypothesis import given, settings, strategies as st
from A4_mocking.titlecost.modules.calculate import CostCalculator


class TestCostCalculator(unittest.TestCase):
    """Unittest class for testing the CostCalculator class."""

    def test_cost_calculator_known_cases(self) -> None:
        """Test the cost calculator with known cases."""
        with patch('A4_mocking.titlecost.modules.calculate.CostCalculator') \
                as MockCalculator:
            MockCalculator.return_value.get_cost.return_value = 1
            self.assertEqual(CostCalculator('movie 1').get_cost(), 1)

            MockCalculator.return_value.get_cost.return_value = 7
            self.assertEqual(CostCalculator('longtitle 7').get_cost(), 7)

            MockCalculator.return_value.get_cost.return_value = 4
            self.assertEqual(CostCalculator('same 4').get_cost(), 4)

    @given(st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122),
                   min_size=1),
           st.floats(min_value=0, max_value=100))
    @settings(max_examples=10)  # Limit the number of random examples
    def test_cost_calculator_random_cases(self, title: str, cap: float) \
            -> None:
        """Test the cost calculator with random title and cap values."""
        s = f"{title} {cap}"
        with patch('A4_mocking.titlecost.modules.calculate.CostCalculator') \
                as MockCalculator:
            MockCalculator.return_value.get_cost.return_value = len(title)
            calculator = CostCalculator(s)
            result = calculator.get_cost()
            self.assertTrue(result <= len(title),
                            f"Result for '{s}' should be less than or equal to\
                                  {result}")

    def test_setter_getter(self) -> None:
        """Test the calculator getter and setter methods."""
        with patch('A4_mocking.titlecost.modules.calculate.CostCalculator') \
                as MockCalculator:
            MockCalculator.return_value.s = 'spoderman'
            calculator = CostCalculator('')
            calculator.s = 'spoderman'
            self.assertEqual(calculator.s, 'spoderman')


if __name__ == "__main__":
    unittest.main()

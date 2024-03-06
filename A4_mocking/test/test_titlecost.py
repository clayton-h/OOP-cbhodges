#
# Python script that tests
# the title cost modules.
#
# By: Clayton H.
#

import unittest
from hypothesis import given, settings, strategies as st
from A4_mocking.titlecost.modules.calculate import CostCalculator


class TestCostCalculator(unittest.TestCase):
    """Unittest class for testing the CostCalculator class."""

    def test_cost_calculator_known_cases(self) -> None:
        """Test the cost calculator with known cases."""
        self.assertEqual(CostCalculator('movie 10').get_cost(), 5)
        self.assertEqual(CostCalculator('longtitle 7').get_cost(), 7)
        self.assertEqual(CostCalculator('short 100').get_cost(), 5)

    @given(st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122),
                   min_size=1),
           st.floats(min_value=0, max_value=100))
    @settings(max_examples=10)  # Limit the number of random examples
    def test_cost_calculator_random_cases(self, title: str, cap: float) \
            -> None:
        """Test the cost calculator with random title and cap values."""
        s = f"{title} {cap}"
        calculator = CostCalculator(s)
        result = calculator.get_cost()
        self.assertTrue(0 <= result <= cap, f"Result for '{s}' should be \
                        between 0 and {cap}")


if __name__ == "__main__":
    unittest.main()

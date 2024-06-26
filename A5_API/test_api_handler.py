#
# Python script that tests
# API requests for a
# weather app
#
# By: Clayton H.
#

import unittest
from A5_API.api_handler import APIHandler
from hypothesis import given, settings, strategies as st
from typing import Callable, Any
from hypothesis.strategies import SearchStrategy


@st.composite
def shuffled_zip_code(draw: Callable[[SearchStrategy], Any]) -> str:
    """Function to generate a shuffled zip code."""
    rand = draw(st.randoms())
    digits = [str(digit) for digit in range(1, 10)]
    rand.shuffle(digits)
    return ''.join(digits[:5])


zip_rand = shuffled_zip_code()


class TestAPIHandler(unittest.TestCase):
    """Unittest class for testing the APIHandler class."""

    def test_input(self) -> None:
        """Test APIHandler with known cases."""
        test_api = APIHandler('7b219966d077739bae9ffdd2640da4c9')
        self.assertEqual(test_api.get_access_key(),
                         '7b219966d077739bae9ffdd2640da4c9')
        test_api.set_query('Grand Junction')
        self.assertEqual(test_api.get_query(), 'Grand Junction')
        test_api.set_unit('m')
        self.assertEqual(test_api.get_unit(), 'm')
        data = test_api.get_data()
        self.assertTrue(data)

    @given(zip_rand)
    @settings(max_examples=1, deadline=500)
    def test_random(self, s: str) -> None:
        """Test APIHandler with a random zipcode."""
        print(s)
        test_api = APIHandler('7b219966d077739bae9ffdd2640da4c9')
        test_api.set_query(s)
        test_api.set_unit('f')
        data = test_api.get_data()
        self.assertTrue(data)

#
# Python script that tests
# the weather app api_handler
# module.
#
# By: Clayton H.
#

import unittest
# from hypothesis import given, settings, strategies as st
from api_handler import APIHandler
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Access the API key
api_key = config['DEFAULT']['WeatherAPIKey']


class TestAPIHandler(unittest.TestCase):
    """Unittest class for testing the APIHandler class."""

    def test_input(self) -> None:
        """Test APIHandler with known cases."""
        test_api = APIHandler(api_key)
        self.assertEqual(test_api.get_access_key(), api_key)
        test_api.set_query('81501')
        self.assertEqual(test_api.get_query(), '81501')

    # zip_rand = st.text(min_size=5, max_size=5, alphabet=st.characters(
    #     whitelist_categories=('Nd',)))

    # @given(zip_rand)
    # @settings(max_examples=1)
    # def test_random(self, s: str) -> None:
    #     """Test APIHandler with a random zipcode."""
    #     test_api = APIHandler(api_key)
    #     test_api.set_query(s)
    #     data = test_api.get_data()
    #     self.assertTrue(data)


if __name__ == "__main__":
    unittest.main()

#
# Python script that tests
# the weather app api_handler
# module.
#
# By: Clayton H.
#

import unittest
from hypothesis import given, settings, strategies as st
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

    def test_defaults(self) -> None:
        """Test APIHandler with known cases."""
        test_api = APIHandler(api_key)
        self.assertEqual(test_api.get_access_key(), api_key)
        test_api.set_query('81501')
        self.assertEqual(test_api.get_query(), '81501')

    query_library = st.one_of(
        st.text(min_size=1, max_size=20),
    )

    @given(query_library)
    @settings(max_examples=1)  # Limit the number of random examples
    def test_random(self, s: str) -> None:
        """Test APIHandler with random data."""
        test_api = APIHandler('67f41d5ce09b4b044d298ca005ecf791')
        test_api.set_query(s)
        data = test_api.get_data()
        self.assertTrue(data)


if __name__ == "__main__":
    unittest.main()

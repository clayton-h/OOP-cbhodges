import unittest
from api_handler import APIHandler
import configparser
from hypothesis import given, settings, strategies as st

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Access the API key
api_key = config['DEFAULT']['WeatherAPIKey']


@st.composite
def shuffled_zip_code(draw) -> str:
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
        test_api = APIHandler(api_key)
        self.assertEqual(test_api.get_access_key(), api_key)
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
        test_api = APIHandler(api_key)
        test_api.set_query(s)
        test_api.set_unit('f')
        data = test_api.get_data()
        self.assertTrue(data)


if __name__ == "__main__":
    unittest.main()

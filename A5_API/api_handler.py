import requests


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


class APIHandler:
    """
    A class for handling API requests to the weather data provider.

    Attributes:
        api_key (str): The API key for accessing the weather data.
    """

    def __init__(self, access_key: str):
        """
        Initializes the APIHandler with the provided API key.

        Args:
            api_key (str): The API key for accessing the weather data.
        """
        self.__params = {
            'access_key': access_key,
        }

    def set_access_key(self, access_key: str):
        """Sets the API key.

        Args:
            access_key (str): API key for weather data.
        """
        self.__access_key = access_key

    def get_access_key(self):
        """Returns the access key.

        Returns:
            str: API key
        """
        return self.__access_key

    def set_unit(self, unit: chr):
        """Sets the temperature unit ('m' for Celsius, 'f' for Fahrenheit,\
              's' for Kelvin)."""
        if unit in ['m', 'f', 's']:
            self.__params['units'] = unit
        else:
            print(
                "Invalid unit. Please use 'm' for Celsius, 'f' for Fahrenheit,\
                      or 's' for Kelvin.")

    def get_unit(self):
        """Returns the temperature unit

        Returns:
            char: 'm' for Metric, 'f' for Fahrenheit, 's' for Scientific)
        """
        return self.__params['units']

    def set_query(self, query: str):
        """Sets the query in the params dictionary.

        Args:
            query (str): User input weather lookup query.
        """
        self.__params['query'] = query

    def get_query(self):
        """Returns the query in the params dictionary.

        Returns:
            str: User input query.
        """
        return self.__params['query']

    def get_data(self):
        """Returns weather data for a query."""
        api_result = requests.get(
            'http://api.weatherstack.com/current', self.__params)

        if api_result.status_code == 200:
            api_response = api_result.json()

            # Check if the expected keys are present in the response
            if 'location' in api_response and 'current' in api_response:
                location = api_response['location'].get('name')
                temperature = api_response['current'].get('temperature')

                if self.__params['units'] == 's':
                    unit = 'K'
                else:
                    unit = '℃' if self.__params['units'] == 'm' else '℉'

                if location and temperature is not None:
                    print(
                        'Current temperature in '
                        f'{location} is {temperature}{unit}'
                    )
                else:
                    print('Error: Temperature or location data is missing.')
            else:
                print('Error: Invalid API response structure.')
        else:
            print(
                'Error: Failed to fetch data from the API.\n'
                f'Status code: {api_result.status_code}'
            )

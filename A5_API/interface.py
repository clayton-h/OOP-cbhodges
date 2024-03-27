from api_handler import APIHandler
from rich.console import Console
from rich.prompt import Prompt
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Access the API key
api_key = config['DEFAULT']['WeatherAPIKey']


def main() -> None:
    console = Console()
    handler = APIHandler(api_key)

    user_query = Prompt.ask(
        "Enter your location (city name, zip code, LatLon, IP)",
        default="Colorado Springs")
    user_unit = Prompt.ask(
        "Enter your preferred unit format (m: ℃ , f: ℉ , s: K)",
        default='f')
    handler.set_query(user_query)
    handler.set_unit(user_unit)

    console.log("[bold green]Fetching weather data...[/bold green]")
    print(handler.get_data())


if __name__ == "__main__":
    main()

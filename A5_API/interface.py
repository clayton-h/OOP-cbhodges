#
# Python script that tests
# utilizes user input for
# weather app demonstration
#
# By: Clayton H.
#

from A5_API.api_handler import APIHandler
from rich.console import Console
from rich.prompt import Prompt


def main() -> None:
    console = Console()
    handler = APIHandler('7b219966d077739bae9ffdd2640da4c9')

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

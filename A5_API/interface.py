from api_handler import APIHandler
from rich.console import Console
from rich.prompt import Prompt


def main() -> None:
    console = Console()
    handler = APIHandler('67f41d5ce09b4b044d298ca005ecf791')

    user_query = Prompt.ask(
        "Enter your location (city name, zip code, LatLon, IP)",
        default="Colorado Springs")
    user_unit = Prompt.ask(
        "Enter your preferred unit format (m: ℃ , f: ℉ , s: K)",
        default='f')
    handler.set_query(user_query)
    handler.set_unit(user_unit)

    console.log("[bold green]Fetching weather data...[/bold green]")
    handler.get_data()


if __name__ == "__main__":
    main()

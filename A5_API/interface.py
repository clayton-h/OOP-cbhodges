from api_handler import APIHandler
from rich.console import Console
from rich.prompt import Prompt


def main():
    console = Console()
    handler = APIHandler('67f41d5ce09b4b044d298ca005ecf791')

    user_query = Prompt.ask(
        "Enter your query (city name)", default="Colorado Springs")
    handler.set_query(user_query)

    console.log("[bold green]Fetching weather data...[/bold green]")
    handler.get_data()


if __name__ == "__main__":
    main()

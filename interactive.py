import base64 as bs
from pathlib import Path

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

console = Console()

def print_banner():
    console.clear()
    banner = Text()
    banner.append("███████╗██╗██╗     ███████╗\n",style="bold cyan",)
    banner.append("██╔════╝██║██║     ██╔════╝\n",style="bold cyan",)
    banner.append("█████╗  ██║██║     █████╗\n",style="bold blue",)
    banner.append("██╔══╝  ██║██║     ██╔══╝\n",style="bold blue",)
    banner.append("██║     ██║███████╗███████╗\n",style="bold magenta",)
    banner.append("╚═╝     ╚═╝╚══════╝╚══════╝\n\n",style="bold magenta",)
    banner.append(" Base64 • File Encoder • File Decoder ",style="dim white",)
    console.print(
        Panel(
            Align.center(banner),
            border_style="cyan",
            box=box.DOUBLE_EDGE,
        )
    )


def divider(title=""):
    console.print(
        Rule(
            title,
            style="cyan",
        )
    )


def success(message):
    console.print(f"\n[bold green]✔[/bold green] {message}\n")


def error(message):
    console.print(f"\n[bold red]✘[/bold red] {message}\n")


def info(message):
    console.print(f"[bold yellow]ℹ[/bold yellow] {message}")


def encode_file(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.is_file():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if input_path.resolve() == output_path.resolve():
        raise ValueError("Input and output files must be different.")

    with input_path.open("rb") as file:
        data = file.read()

    encoded_data = bs.b64encode(data)
    with output_path.open("wb") as file:
        file.write(encoded_data)
    return output_path


def decode_file(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.is_file():
        raise FileNotFoundError(f"Encoded Base64 file not found: {input_file}")

    if input_path.resolve() == output_path.resolve():
        raise ValueError("Input and output files must be different.")

    with input_path.open("rb") as file:
        encoded_data = file.read()

    try:
        decoded_data = bs.b64decode(
            encoded_data,
            validate=True,
        )
    except (bs.binascii.Error, ValueError) as exc: # type: ignore
        raise ValueError("Invalid Base64 data.") from exc

    with output_path.open("wb") as file:
        file.write(decoded_data)
    return output_path


def menu():
    table = Table(
        title="Main Menu",
        title_style="bold cyan",
        box=box.DOUBLE_EDGE,
        border_style="cyan",
        padding=(0, 2),
    )
    table.add_column(
        "Option",
        justify="center",
        style="bold yellow",
    )
    table.add_column("Action",style="green",)
    table.add_row("1","🔒 Encode Text",)
    table.add_row("2","🔓 Decode Text",)
    table.add_row("3","ℹ About",)
    table.add_row("0","🚪 Exit",)
    console.print(table)


def encode_menu():
    divider("🔒 Encode Text")
    input_file = Prompt.ask("[bold cyan]Enter File Path: [/bold cyan]").strip()
    output_file = Prompt.ask("[bold cyan]Enter Output File Name (Include Extension): [/bold cyan]").strip()
    try:
        result = encode_file(input_file,output_file)
        success(f"File encoded successfully: [bold white]{result}[/bold white]")
    except FileNotFoundError as exc:
        error(str(exc))
    except PermissionError:
        error("Permission denied. Check the file or folder permissions.")
    except IsADirectoryError:
        error("The specified path is a directory, not a file.")
    except ValueError as exc:
        error(str(exc))
    except OSError as exc:
        error(f"File system error: {exc}")


def decode_menu():
    divider("🔓 Decode Text")
    encoded_file = Prompt.ask("[bold cyan]Enter Encoded Base64 File Path: [/bold cyan]")
    output_file = Prompt.ask("[bold cyan]Enter New File Name (Include Extension): [/bold cyan]") 
    try:
        result = decode_file(encoded_file,output_file)
        success(f"File decoded successfully: [bold white]{result}[/bold white]")
    except FileNotFoundError as exc:
        error(str(exc))
    except PermissionError:
        error("Permission denied. Check the file or folder permissions.")
    except IsADirectoryError:
        error("The specified path is a directory, not a file.")
    except ValueError as exc:
        error(str(exc))
    except OSError as exc:
        error(f"File system error: {exc}")

def about():
    divider("ℹ About Toolkit")
    table = Table(
        show_header=True,
        header_style="bold cyan",
        box=box.ROUNDED,
        border_style="cyan",
    )
    table.add_column("Property",style="yellow",)
    table.add_column("Value",style="green",)
    table.add_row("Purpose","Base64 File Encoding & Decoding",)
    table.add_row("Encoding","Base64",)
    table.add_row("Data Type","Binary / Any File",)
    table.add_row("Encode Method","Base64",)
    table.add_row("Decode Validation","Strict",)
    table.add_row("Language","Python",)
    table.add_row("UI","Rich CLI",)
    console.print(table)


def main():
    while True:
        print_banner()
        menu()
        choice = Prompt.ask(
            "\n[bold cyan]Select Option[/bold cyan]",
            choices=["1", "2", "3", "0"],
            default="1",
        )
        if choice == "1":
            encode_menu()
        elif choice == "2":
            decode_menu()
        elif choice == "3":
            about()
        elif choice == "0":
            console.print()
            console.print(
                Panel(
                    Align.center(
                        Text(
                            "See You Soon! | Stay safe, stay secure. 🕵️",
                            style="bold cyan",
                        )
                    ),
                    border_style="magenta",
                    box=box.DOUBLE_EDGE,
                )
            )
            break
        Prompt.ask(
            "\n[dim]Press Enter to return to menu…[/dim]",
            default="",
        )


if __name__ == "__main__":
    main()

"""console.py
Pretty printing messages to the console
"""

# Imports
from rich.markdown import Markdown
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.text import Text


# Initialize the console object
console = Console()


def print_markdown(text: str) -> None:
    """Prints a rich info message. Supports Markdown syntax"""

    text = Padding(Markdown(text), 2)
    console.print(text)


def print_step(text: str) -> None:
    """Prints a rich info message."""

    panel = Panel(Text(text, justify='left'))
    console.print(panel)


def print_substep(text: str, style: str = '') -> None:
    """Prints a rich info message without panelling."""

    console.print(text, style=style)

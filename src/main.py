from datetime import datetime

from rich import box, print
from rich.live import Live
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

console = Console()


def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
    )
    return layout


def make_sponsor_message() -> Panel:
    """Some example content."""
    sponsor_message = Table.grid(padding=1)
    sponsor_message.add_column(style="green", justify="right")
    sponsor_message.add_column(no_wrap=True)
    sponsor_message.add_row(
        "Twitter",
        "[u blue link=https://twitter.com/textualize]https://twitter.com/textualize",
    )
    sponsor_message.add_row(
        "CEO",
        "[u blue link=https://twitter.com/willmcgugan]https://twitter.com/willmcgugan",
    )
    sponsor_message.add_row(
        "Textualize", "[u blue link=https://www.textualize.io]https://www.textualize.io"
    )

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(sponsor_message)

    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(sponsor_message)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]Thanks for trying out Rich!",
        border_style="bright_blue",
    )
    return message_panel


class Header:
    """Display header with clock."""
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "Polaris",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid)


layout = make_layout()
layout["header"].update(Header())
layout["body"].update(make_sponsor_message())


with Live(layout, refresh_per_second=10, screen=True) as live:
    while True:
        live.update(layout)


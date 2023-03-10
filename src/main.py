from datetime import datetime

from rich.live import Live
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

console = Console()


class Task:
    def __init__(self, data: str):
        # TODO: The data has to be parsed to get out date time and stuff
        pass
    def save(self):
        pass
    # TODO: some sort of get and set item that checks if it is valid


class ContentScreen:
    def __rich__(self) -> Panel:
        grid = Table.grid()
        grid.add_column(style="cyan", justify="left")
        grid.add_column(justify="left")
        grid.add_row("D", "This is a task")
        grid.add_row("W", "This is another task")
        grid.add_row(" ", "Do you realize how tasky it is")
        return Panel(
            grid,
            title="Today"
        )


class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "Polarist",
            datetime.now().ctime(),
        )
        return Panel(grid)


def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
    )
    return layout


layout = make_layout()
layout["header"].update(Header())
layout["body"].update(ContentScreen())


with Live(layout, refresh_per_second=10, screen=True) as live:
    while True:
        live.update(layout)


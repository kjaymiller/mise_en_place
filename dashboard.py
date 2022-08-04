from textual.app import App
from pins_this_week import build_console
from rich.prompt import Prompt
import pinboard
import os
from rich.panel import Panel
from textual.reactive import Reactive
from rich.console import Console
from textual.widget import Widget
import string
from textual.keys import Keys
from textual import events


pb = pinboard.Pinboard(os.environ.get('PINBOARD_API_TOKEN', None))

class Pinboard(Widget):
    def render(self):
        return build_console(pb)

class InputBox(Widget):
    input_text = Reactive("")

    def render(self):
        return f"[blue]{self.input_text}[/blue]"

    def set_input_text(self, input_text):
        self.input_text = input_text

class SimpleApp(App):
    input_text = Reactive("")
    input_box: InputBox

    async def on_key(self, key: events.Key) -> None:
        if key.key == Keys.ControlH:
            self.input_text = self.input_text[:-1]
        elif key.key == Keys.Delete:
            self.input_text = ""
        elif key.key in string.printable:
            self.input_text += key.key

    def watch_input_text(self, input_text) -> None:
        self.input_box.set_input_text(input_text)

    async def on_mount(self) -> None:
        self.input_box = InputBox()
        grid = await self.view.dock_grid(edge="left", name="left")
        grid.add_column(name="body")
        grid.add_row(size=1, name="input")
        grid.add_areas(areaInputBox="body, input")
        grid.place(areaInputBox=self.input_box)


SimpleApp.run(log="textual.log")

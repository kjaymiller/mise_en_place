from textual.app import App
from pins_this_week import build_console
import pinboard
import os
from rich.panel import Panel
from textual.reactive import Reactive
from rich.console import Console
from textual.widget import Widget
from reddit import display_reddit_posts
import datetime

pb = pinboard.Pinboard(os.environ.get('PINBOARD_API_TOKEN', None))

class Pinboard(Widget):
    def render(self):
        return build_console(pb)


class Reddit(Widget):
    def render(self):
        yesterday = datetime.datetime.now() - datetime.timedelta(days=-1)
        return display_reddit_posts("python", fromdt=yesterday)
        
class SimpleApp(App):
    async def on_mount(self) -> None:
        grid = await self.view.dock(*[Pinboard(), Reddit()], edge="left", name="left")


if __name__ == "__main__":
    SimpleApp.run(log="textual.log")

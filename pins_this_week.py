import webbrowser
from pinboard import Pinboard
from datetime import date, timedelta
import os
from rich import print as pprint
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text

# get the date of the week's Monday
monday = date.today() - timedelta(days=date.today().weekday())
yesterday = date.today() - timedelta(days=1)

def process_post_from_date(pins):
    for post in pins:
        time = post.time.strftime('%Y-%m-%d')
        title = post.description.split('\n')[0] or "Untitled"
        url = post.url
        tags = post.tags
        yield [time, title, url, tags]
    

def build_console(pb: Pinboard) -> Table:
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Date", justify="right", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Tags", justify="center", style="yellow")

    pb.posts.all(fromdt=yesterday)

    for time, title, url, tags in process_post_from_date(pb.posts.all(fromdt=monday)):
        if 'twitter.com' in url:
            continue
        table.add_row(time, Markdown(f"[{title}]({url})"), ", ".join(tags))

    return table

if __name__ == "__main__":
    pb = Pinboard(os.environ.get('PINBOARD_API_TOKEN'))
    pprint(build_console(pb))
import datetime
from time import mktime
import feedparser as fp
from rich.table import Table
from rich.markdown import Markdown
from rich import print as rprint



def get_reddit_posts(
    subreddit:str,
    fromdt: datetime.timedelta | None = None,
    limit: int | None = None
    ):
    feed = fp.parse(f'https://www.reddit.com/r/{subreddit}/.rss?sort=new')    
    limit = limit or len(feed.entries)

    for i, entry in enumerate(feed.entries):
        if fromdt:
            if datetime.datetime.fromtimestamp(mktime(entry.published_parsed)) > fromdt:
                break
        if i >= limit:
            break
        yield entry        
    

def display_reddit_posts(
    subreddit:str,
    limit: int | None = None,
    fromdt: datetime.timedelta | None = None,
    ):
    """Create a Rich Table from Reddit posts."""
    table = Table(*['title', 'author', 'date'], show_header=True, header_style="bold green")
    
    for entry in get_reddit_posts(subreddit, fromdt=fromdt, limit=limit):
        title = entry.title
        link = entry.link
        author = entry.author
        date = entry.published
        
        table.add_row(Markdown(f"[{title}]({link})"), author, date)
    
    return table


if __name__ == "__main__":
    yesterday = datetime.datetime.now() - datetime.timedelta(days=-1)
    rprint(display_reddit_posts("python", fromdt=yesterday))
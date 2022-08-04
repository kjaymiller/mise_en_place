from markdown import markdown
from datetime import datetime
from pathlib import Path
import dataclasses
from collections import namedtuple

"""
BASIC RULES:
1. Every Task is a file
2. Every Task has a unique ID
3. Tasks can have a title, description, due date, defer date, tags, and notes
4. Tasks can have the status of "Not Started", "In Progress", "Completed", "Cancelled", or "Deferred"
5. All of the metadata is in the frontmatter of the file
6. The content is the notes
7. wiki-style links are supported and presented inline unless the "inline: false" tag is present
8. NLP Format
"""


def import tasks_from_path(path: Path) -> list[Task]:
    """
    Import tasks from a directory.
    """
    with open(path, 'r') as f:
        tasks = frontmatter.load_all(f)
    return [Task(**task) for task in tasks]
class Task(namedtuple): 
    def __init__(self, tasks: list = None, due_date: datetime = ):
        if tasks:
            self.tasks = tasks

    def add_tasks(self, task: 'Task'):
        self.tasks.extend(task)

    

    def __str__(self):
        return str(self.tasks)

class Project:
    def __init__(self, tasks: list || None = None ):
        if tasks:
            self.tasks = tasks

class Notes:
    def __init__(self):
        
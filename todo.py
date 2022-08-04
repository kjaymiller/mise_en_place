frontmatter
from pathlib import Path
import dataclasses

class Task: 
    def __init__(self, tasks: list || None = None):
        if tasks:
            self.tasks = tasks


class Project:
    def __init__(self, tasks: list || None = None ):
        if tasks:
            self.tasks = tasks

class Notes:
    def __init__(self):
        
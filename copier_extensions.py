import os
from pathlib import Path
from jinja2.ext import Extension


class FolderNameExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["_folder_name"] = Path(os.getcwd()).name

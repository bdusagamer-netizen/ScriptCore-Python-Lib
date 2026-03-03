"""ScriptCore package

Public API:
- `parse_subfiles(text) -> list[Subfile]`
- `write_subfiles_to_dir(subfiles, path)`
- `launch_viewer(subfiles)`
"""
from .core import Subfile, parse_subfiles, write_subfiles_to_dir
from .viewer import launch_viewer

__all__ = ["Subfile", "parse_subfiles", "write_subfiles_to_dir", "launch_viewer"]

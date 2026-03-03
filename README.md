# ScriptCore

ScriptCore is a tiny Python library and standalone script that lets you embed web assets
(HTML/CSS/JS/etc.) directly inside a Python source file.  When the Python file is run, the
`is_main="true"` subfile is extracted and rendered inside a built‑in browser window (via
QtWebEngine) or printed/text‑viewed.

## Features

- HTML/CSS/JS can live alongside Python code in `main.py`.
- Works as a standalone script or as an importable package.
- Embedded viewer uses PySide6 (`QtWebEngine`) for true web rendering.
- Also supports simple CLI extraction/listing via `scriptcore` console command.

## Installation

To install, run:
`pip install git+https://github.com/bdusagamer-netizen/ScriptCore-Python-Lib.git`

## Dependencies

PySide is used to load the html code.

PySide6 is a runtime dependency; it is declared in `pyproject.toml` and will be pulled
in automatically.  On platforms where QtWebEngine is unavailable you can still use the
`parse_subfiles`/`write_subfiles_to_dir` API without the viewer.

## Starter templates

You can grab one of these starting points:

- [basic template](templates/hello.py)
- [external-src template](templates/src_template.py)

## Usage as standalone `main.py`

Create a Python file with embedded SCRIPTCORE blocks:

```python
#!/usr/bin/env python3

import re
# (parser code omitted for brevity; see provided template)

SCRIPTCORE subfile
subfile{
    FileType=".html"
    FileID="index.html"
    is_main="true"
    {
        <h1>Hello world</h1>
    }
}
```

Run the script:

```powershell
python main.py
```
or select the main.py in File Explorer and hit enter/return.

A window will open rendering the HTML.  You can copy the standalone script anywhere – it
does not need access to the package directory.

## CLI / Package API

```python
from scriptcore import parse_subfiles, write_subfiles_to_dir, launch_viewer

subs = parse_subfiles(open('main.py').read())
write_subfiles_to_dir(subs, 'out')   # extract files
launch_viewer(subs)                 # open Qt viewer
```

The console script `scriptcore` provides `--source`, `--list`, `--extract`, `--open`.


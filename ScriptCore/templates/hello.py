#!/usr/bin/env python3
"""Hello World template using ScriptCore.

This script embeds HTML in a SCRIPTCORE block and uses the scriptcore
library to parse and display it.

Usage:
    python hello.py

Requires: scriptcore and PySide6
    pip install scriptcore PySide6
"""
from scriptcore import parse_subfiles, launch_viewer
import sys


def main():
    """Read this file and parse SCRIPTCORE blocks, then display them."""
    with open(__file__, 'r', encoding='utf-8') as f:
        text = f.read()
    
    subfiles = parse_subfiles(text)
    if not subfiles:
        print('No SCRIPTCORE blocks found in this file')
        return 1
    
    launch_viewer(subfiles)
    return 0


if __name__ == '__main__':
    sys.exit(main())


"""
SCRIPTCORE subfile
subfile{
    FileType=".html"
    FileID="index.html"
    is_main="true"
    {
        <h1>Hello World</h1>
        <p>This HTML is embedded inside the Python script and rendered by ScriptCore.</p>
        <p>Open this file in a text editor to see how it works!</p>
    }
}
"""

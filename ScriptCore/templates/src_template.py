#!/usr/bin/env python3
"""External source template using ScriptCore.

This script embeds an HTML iframe that loads an external URL.
Edit the `src` attribute to point to your desired content.

Usage:
    python src_template.py

Requires: scriptcore (and PySide6 for the viewer)
    pip install scriptcore
    pip install PySide6
"""
from scriptcore import parse_subfiles, launch_viewer
import sys


# Embedded HTML file using SCRIPTCORE block format
"""
SCRIPTCORE subfile
subfile{
    FileType=".html"
    FileID="index.html"
    is_main="true"
    {
        <html>
        <head>
            <title>External Content</title>
            <style>
                body { margin: 0; }
                iframe { border: none; width: 100%; height: 100vh; }
            </style>
        </head>
        <body>
            <iframe src="https://example.com"></iframe>
        </body>
        </html>
    }
}
"""


def main():
    # Read this file and parse SCRIPTCORE blocks
    with open(__file__, 'r', encoding='utf-8') as f:
        text = f.read()
    
    subfiles = parse_subfiles(text)
    if not subfiles:
        print('No SCRIPTCORE blocks found in this file')
        return 1
    
    # Launch the viewer with the embedded files
    launch_viewer(subfiles)
    return 0


if __name__ == '__main__':
    sys.exit(main())

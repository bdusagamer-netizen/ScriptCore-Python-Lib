#!/usr/bin/env python3
import re

# ScriptCore main script that loads HTML from an external source
# Replace the src value with your URL or path.

SCRIPTCORE subfile
subfile{
    FileType=".html"
    FileID="index.html"
    is_main="true"
    {
        <iframe src="html_path_here" width="100%" height="100%"></iframe>
    }
}


#!/usr/bin/env python3
import re

# simple ScriptCore main script with embedded hello world HTML

SCRIPTCORE subfile
subfile{
    FileType=".html"
    FileID="index.html"
    is_main="true"
    {
        <h1>Hello World</h1>
    }
}

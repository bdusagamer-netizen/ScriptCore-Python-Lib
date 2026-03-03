"""Core parsing utilities for ScriptCore."""
from dataclasses import dataclass
import re
from typing import List

@dataclass
class Subfile:
    FileType: str
    FileID: str
    is_main: bool
    code: str

def parse_subfiles(text: str) -> List[Subfile]:
    """Parse SCRIPTCORE subfile blocks from the given text and return Subfile objects."""
    entries = []
    pos = 0
    while True:
        m = re.search(r"SCRIPTCORE\s+subfile", text[pos:])
        if not m:
            break
        start = pos + m.end()
        brace_pos = text.find("subfile{", start)
        if brace_pos == -1:
            pos = start
            continue
        i = brace_pos + len("subfile{")
        inner_start = text.find("{", i)
        if inner_start == -1:
            pos = i
            continue
        depth = 0
        j = inner_start
        while j < len(text):
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
                if depth == 0:
                    inner_end = j
                    break
            j += 1
        else:
            break
        attrs_text = text[i:inner_start]
        code = text[inner_start+1:inner_end]
        outer_close = text.find('}', inner_end+1)
        pos = outer_close + 1 if outer_close != -1 else inner_end + 1
        filetype = re.search(r'FileType\s*=\s*"([^"]+)"', attrs_text)
        fileid = re.search(r'FileID\s*=\s*"([^"]+)"', attrs_text)
        is_main = re.search(r'is_main\s*=\s*"([^"]+)"', attrs_text)
        sf = Subfile(
            FileType=filetype.group(1).strip() if filetype else '',
            FileID=fileid.group(1).strip() if fileid else '',
            is_main=is_main.group(1).strip().lower() == 'true' if is_main else False,
            code=code.strip(),
        )
        entries.append(sf)
    return entries

def write_subfiles_to_dir(subfiles: List[Subfile], path: str) -> None:
    """Write given subfiles to `path` using their FileID as filenames."""
    import os
    os.makedirs(path, exist_ok=True)
    for sf in subfiles:
        name = sf.FileID or ('untitled' + (sf.FileType or ''))
        dst = os.path.join(path, name)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(sf.code)
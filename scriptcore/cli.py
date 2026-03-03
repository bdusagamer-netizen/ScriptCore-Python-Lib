"""Command-line interface for ScriptCore."""
import argparse
import sys
import os
from .core import parse_subfiles, write_subfiles_to_dir
from .viewer import launch_viewer

def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    p = argparse.ArgumentParser(prog='scriptcore', description='ScriptCore CLI')
    p.add_argument('--source', '-s', help='Source file to parse (default: main.py)', default='main.py')
    p.add_argument('--extract', '-e', help='Directory to extract subfiles to')
    p.add_argument('--open', action='store_true', help='Open viewer UI')
    args = p.parse_args(argv)

    if not os.path.exists(args.source):
        print('Source file not found:', args.source)
        return 2

    with open(args.source, 'r', encoding='utf-8') as f:
        content = f.read()

    subfiles = parse_subfiles(content)
    if not subfiles:
        print('No SCRIPTCORE subfile blocks found in', args.source)
        return 1

    if args.extract:
        write_subfiles_to_dir(subfiles, args.extract)
        print('Wrote', len(subfiles), 'files to', args.extract)

    if args.open or (not args.extract and not args.open):
        # default action when no flags: open viewer
        launch_viewer(subfiles)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
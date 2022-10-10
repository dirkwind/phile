from __future__ import annotations

import os
import sys


def get_indent_level(string: str, *, indent: int=4) -> int:
    space_count = 0
    for c in string:
        if c == ' ':
            space_count += 1
        else:
            break
    return space_count // indent


def execute(lines: list(str), path: list(str) | None = None, prev_level: int = -1, pos: int = 0) -> None:
    if path is None:
        path = ['.']

    if pos >= len(lines):
        return

    line  = lines[pos]
    level = get_indent_level(line)

    print(line, level, prev_level)

    if level < prev_level:
        for _ in range(prev_level - level):
            path.pop()
    
    line = line.strip()

    if line != '':
        if not line.startswith("f "):
            

            path.append(line)

            print("Creating dir ", "/".join(path))
            os.makedirs("/".join(path), exist_ok=True)
        else:
            print("Creating file ", "/".join(path) + "/" + line[2:])
            with open("/".join(path) + "/" + line[2:], 'w'):
                pass
    
    execute(lines, path, level, pos + 1)
    



if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) <= 1:
        print("ERROR: file not provided")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as source_file:
        source_code = source_file.read().strip()
    
    execute(source_code.splitlines())
    
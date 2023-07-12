#!/usr/bin/python3
"""Append to text"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='utf-8') as f:
        read = f.read()
        f.seek(0)
        n = 0
        lines = []
        for line in f:
            n += len(line)
            if search_string in line:
                lines.append(n)
    with open(filename, 'w', encoding='utf-8') as f:
        lines_added = 0
        for n in lines:
            n += (len(new_string) * lines_added)
            read = read[:n] + new_string + read[n:]
            lines_added += 1
        f.write(read)

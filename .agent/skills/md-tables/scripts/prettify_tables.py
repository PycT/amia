#!/usr/bin/env python3
"""Align pipe-delimited markdown tables to consistent column widths.

Usage:
    python3 prettify_tables.py <file.md> [--dry-run]

Rewrites every markdown table in the file in place: pads cells so columns
line up, resizes the separator row to match, and preserves each column's
original alignment marker (left/right/center). Everything outside of
tables — including lines inside fenced code blocks that merely contain a
"|" — is left untouched.
"""
import re
import sys

FENCE_RE = re.compile(r'^\s*(```|~~~)')
SEP_CELL_RE = re.compile(r'^:?-+:?$')
SPLIT_RE = re.compile(r'(?<!\\)\|')


def is_table_line(line):
    s = line.strip()
    return s.startswith('|') and len(SPLIT_RE.split(s)) >= 3


def split_row(line):
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    return [c.strip() for c in SPLIT_RE.split(s)]


def is_separator_row(cells):
    return len(cells) > 0 and all(SEP_CELL_RE.match(c) for c in cells)


def cell_align(sep_cell):
    left = sep_cell.startswith(':')
    right = sep_cell.endswith(':')
    if left and right:
        return 'center'
    if right:
        return 'right'
    if left:
        return 'left-explicit'
    return 'left'


def pad(text, width, align):
    gap = width - len(text)
    if gap <= 0:
        return text
    if align == 'right':
        return ' ' * gap + text
    if align == 'center':
        left = gap // 2
        return ' ' * left + text + ' ' * (gap - left)
    return text + ' ' * gap


def build_separator(aligns, widths):
    cells = []
    for align, width in zip(aligns, widths):
        if align == 'center':
            cells.append(':' + '-' * (width - 2) + ':')
        elif align == 'right':
            cells.append('-' * (width - 1) + ':')
        elif align == 'left-explicit':
            cells.append(':' + '-' * (width - 1))
        else:
            cells.append('-' * width)
    return '| ' + ' | '.join(cells) + ' |\n'


def format_table(block_lines):
    """block_lines: list of raw table-row strings (header, sep, data...).
    Returns the reformatted lines, or the original lines unchanged if the
    second row isn't a valid separator (so it wasn't really a table)."""
    rows = [split_row(l) for l in block_lines]
    if len(rows) < 2 or not is_separator_row(rows[1]):
        return block_lines

    header, sep, data = rows[0], rows[1], rows[2:]
    ncols = len(header)
    aligns = [cell_align(c) for c in sep] + ['left'] * max(0, ncols - len(sep))
    aligns = aligns[:ncols]

    widths = [len(header[c]) for c in range(ncols)]
    for row in data:
        for c in range(ncols):
            if c < len(row):
                widths[c] = max(widths[c], len(row[c]))
    min_widths = {'center': 3, 'right': 2, 'left-explicit': 2}
    widths = [max(w, min_widths.get(a, 1)) for w, a in zip(widths, aligns)]

    def build_row(cells):
        padded = [pad(cells[c] if c < len(cells) else '', widths[c], aligns[c])
                  for c in range(ncols)]
        return '| ' + ' | '.join(padded) + ' |\n'

    out = [build_row(header), build_separator(aligns, widths)]
    out.extend(build_row(row) for row in data)
    return out


def prettify(text):
    lines = text.splitlines(keepends=True)
    out = []
    i, n = 0, len(lines)
    in_fence = False
    tables_found = 0
    while i < n:
        if FENCE_RE.match(lines[i]):
            in_fence = not in_fence
            out.append(lines[i])
            i += 1
            continue
        if not in_fence and is_table_line(lines[i]):
            j = i
            while j < n and not FENCE_RE.match(lines[j]) and is_table_line(lines[j]):
                j += 1
            block = lines[i:j]
            formatted = format_table(block)
            if formatted != block:
                tables_found += 1
            out.extend(formatted)
            i = j
        else:
            out.append(lines[i])
            i += 1
    return ''.join(out), tables_found


def main():
    args = sys.argv[1:]
    dry_run = '--dry-run' in args
    args = [a for a in args if a != '--dry-run']
    if len(args) != 1:
        print('Usage: prettify_tables.py <file.md> [--dry-run]', file=sys.stderr)
        sys.exit(1)

    path = args[0]
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    updated, changed = prettify(original)

    if updated == original:
        print(f'No changes: tables already aligned in {path}')
        return

    if dry_run:
        print(f'Would update {changed} table(s) in {path} (dry run, no write)')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f'Updated {changed} table(s) in {path}')


if __name__ == '__main__':
    main()

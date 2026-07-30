---
name: md-tables
description: Prettifies pipe-delimited markdown tables in a file by aligning every column to a consistent width, padding cells, and resizing the separator row — while preserving each column's left/right/center alignment markers. Use this whenever the user runs "/md_tables", asks to "prettify", "align", "clean up", or "fix the formatting" of markdown tables, or points out that a table's columns are ragged/misaligned/hard to read in a .md file. Applies to the file open in the user's editor unless another path is given.
---

# Markdown table prettifier

Aligns markdown tables the way a human would by hand, but reliably: every
cell in a column padded to the same width, the separator row (`---`)
resized to match, and each column's original alignment (left / right /
center, from `:---`, `---:`, `:---:`) kept exactly as it was. Only the
tables change — every other line in the file, including anything inside
fenced code blocks, is left byte-for-byte alone.

Column widths and left/right/center padding are easy to get wrong by
counting characters manually, especially with multiple tables of different
shapes in the same file. Always use the bundled script — don't hand-align
tables by eye.

## Running it

```
python3 scripts/prettify_tables.py <path-to-file.md>
```

- If the user invoked this via `/md_tables` (or otherwise didn't name a
  file), use the file currently open in their editor.
- If they named a file or pasted a path, use that instead.
- Add `--dry-run` first if you want to confirm how many tables would change
  before writing (it reports a count and makes no edits).
- The script rewrites the file in place and prints how many tables it
  changed. Report that count back to the user rather than re-describing
  every table.

## What counts as a table

A block of consecutive lines starting with `|` where the second line is a
valid separator row (only `-`, and optional leading/trailing `:`, per
cell). Blocks that don't have a real separator row are left untouched —
that catches lines that merely contain pipes (e.g. inline code with `|` in
it) without misformatting them. Pipes escaped as `\|` inside a cell are not
treated as column boundaries.

## Notes

- The script assumes one character = one column of display width. It
  doesn't special-case wide (e.g. CJK) characters — mention this if a file
  full of those tables looks off after running it.
- If a table has rows with fewer or more cells than the header, the script
  pads short rows with empty cells rather than erroring out.

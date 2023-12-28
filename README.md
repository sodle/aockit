# AoCKit
A set of common utilities for completing the [Advent of Code](https://adventofcode.com/).

## Input Parsing (`aockit.inputs`)
Utility functions for reading puzzle input from a file.

- `read_lines(path: Path, parser: Callable[[str], T], include_blank_lines: bool = False, strip: bool = True) -> Iterator[T]`
  - Reads each line from the file at `path`. Uses `parser` to process the line and yield it.
  - If `include_blank_lines` is True, blank lines from the file will be included. If False (the default), they will be omitted.
  - If `strip` is False, leading and trailing spaces and newlines will be included. If True (the default), they will be stripped.
  - `parser` should be a lambda or function that accepts a string. `read_lines` will yield the value of `parser(line)` for each line.
- `read_strings(path: Path, include_blank_lines: bool = False, strip: bool = True) -> Iterator[str]`
  - Reads each line from the file at `path` and yields it.
  - If `include_blank_lines` is True, blank lines from the file will be included. If False (the default), they will be omitted.
  - If `strip` is False, leading and trailing spaces and newlines will be included. If True (the default), they will be stripped.
- `read_ints(path: Path) -> Iterator[int]`
  - Reads each line from the file at `path` and yields it as an integer.
- `read_string_groups(path: Path) -> Iterator[list[str]]`
  - Reads each line from the file at `path`.
  - Lines are organized into groups, separated by blank lines in the file.
  - Each group is yielded as a list of strings.
- `read_int_groups(path: Path) -> Iterator[list[int]]`
  - Reads each line from the file at `path` and parses it as an integer.
  - Lines are organized into groups, separated by blank lines in the file.
  - Each group is yielded as a list of integers.

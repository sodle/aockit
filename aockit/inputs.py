from pathlib import Path
from collections.abc import Iterator

from typing import TypeVar, Callable


T = TypeVar("T")


def read_lines(path: Path, parser: Callable[[str], T],
               include_blank_lines: bool = False, strip: bool = True) -> Iterator[T]:
    with path.open() as f:
        line = f.readline()
        while len(line) > 0:
            if line == '\n':
                if include_blank_lines:
                    if strip:
                        line = line.strip()
                    yield parser(line)
            else:
                if strip:
                    line = line.strip()
                yield parser(line)

            line = f.readline()


def read_strings(path: Path, include_blank_lines: bool = False, strip: bool = True) -> Iterator[str]:
    return read_lines(path, lambda line: line, include_blank_lines=include_blank_lines, strip=strip)


def read_ints(path: Path) -> Iterator[int]:
    return read_lines(path, lambda line: int(line))


def read_string_groups(path: Path) -> Iterator[list[str]]:
    group = []

    for line in read_strings(path, include_blank_lines=True):
        if len(line) == 0:
            if len(group) > 0:
                yield group
            group = []
        else:
            group.append(line)

    if len(group) > 0:
        yield group


def read_int_groups(path: Path) -> Iterator[list[int]]:
    group = []

    for line in read_strings(path, include_blank_lines=True):
        if len(line) == 0:
            if len(group) > 0:
                yield group
            group = []
        else:
            group.append(int(line))

    if len(group) > 0:
        yield group

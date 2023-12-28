from collections.abc import Iterator

from typing import TypeVar, Generic

T = TypeVar('T')


class Grid(Generic[T]):
    def __init__(self, height: int, width: int, content: list[T]):
        self.height = height
        self.width = width
        self._content = content

    def _calculate_index(self, row: int, col: int) -> int:
        if col >= self.width:
            raise IndexError(f'Column {col} out of range for grid width {self.width}')
        if row >= self.height:
            raise IndexError(f'Row {row} out of range for grid height {self.height}')

        while row < 0:
            row = self.height + row
        while col < 0:
            col = self.width + col

        return (self.width * row) + col

    def get(self, row: int, col: int) -> T:
        index = self._calculate_index(row, col)
        return self._content[index]

    def __getitem__(self, key: tuple[int, int]) -> T:
        return self.get(*key)

    def set(self, row: int, col: int, value: T):
        index = self._calculate_index(row, col)
        self._content[index] = value

    def __setitem__(self, key: tuple[int, int], value: T):
        return self.set(*key, value)

    def col(self, col: int) -> Iterator[T]:
        row = 0
        while row < self.height:
            index = self._calculate_index(row, col)
            yield self._content[index]
            row += 1

    def col_indexed(self, col: int) -> Iterator[tuple[int, int, T]]:
        row = 0
        while row < self.height:
            index = self._calculate_index(row, col)
            yield row, col, self._content[index]
            row += 1

    def row(self, row: int) -> Iterator[T]:
        col = 0
        while col < self.width:
            index = self._calculate_index(row, col)
            yield self._content[index]
            col += 1

    def row_indexed(self, row: int) -> Iterator[tuple[int, int, T]]:
        col = 0
        while col < self.width:
            index = self._calculate_index(row, col)
            yield row, col, self._content[index]
            col += 1

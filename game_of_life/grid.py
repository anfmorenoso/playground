from numpy.random import choice
from typing import List, Tuple
from .cell import Cell


class UnevenGridException(Exception):
    pass


class EmptyGridException(Exception):
    pass


class Grid:
    def __init__(self, initial_state: List[List[int]]):
        self.n_generation = 0
        self.initial_state = initial_state
        self.n_lines = self._ensure_lines()
        self.n_cols = self._ensure_cols()
        self.lines_of_cells = []
        for x in range(self.n_lines):
            line = [Cell(x, y, initial_state[x][y]) for y in range(self.n_cols)]
            self.lines_of_cells.append(line)
        # this is a bit weird :p
        for line in self.lines_of_cells:
            for cell in line:
                cell.calculate_neighbors(n_lines=self.n_lines, n_cols=self.n_cols)

    @classmethod
    def from_random_start(cls, n_lines: int, n_columns: int):
        initial_state = []
        for i in range(n_lines):
            initial_state.append(list(choice([1, 0], size=n_columns)))
        return cls(initial_state)

    def _ensure_lines(self) -> int:
        n_lines = len(self.initial_state)
        if n_lines == 0:
            raise EmptyGridException
        else:
            return n_lines

    def _ensure_cols(self) -> int:
        if self.n_lines != 0:
            n_cols = len(self.initial_state[0])
            for line in self.initial_state:
                if len(line) != n_cols:
                    raise UnevenGridException
        return n_cols

    def __str__(self):
        laconcha = []
        for line in self.lines_of_cells:
            str_line = " ".join(str(cell) for cell in line)
            laconcha.append(str_line)
        return "\n".join(laconcha)

    def __eq__(self, other):
        if self.n_cols == other.n_cols:
            if self.n_lines == self.n_lines:
                for x in range(self.n_lines):
                    for y in range(self.n_cols):
                        if self.lines_of_cells[x][y] != other.lines_of_cells[x][y]:
                            return False
                return True
        return False

    def calculate_cells_next_state(self):
        for line in self.lines_of_cells:
            for cell in line:
                cell_neighbors = cell.get_neighbors()
                count_alive = 0
                for (x, y) in cell_neighbors:
                    if self.lines_of_cells[x][y].is_alive:
                        count_alive += 1
                cell.calculate_next_generation_state(count_alive)

    def next_generation(self):
        self.n_generation += 1
        self.calculate_cells_next_state()

        for line in self.lines_of_cells:
            for cell in line:
                cell.pass_generation()

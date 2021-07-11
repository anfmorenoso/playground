from typing import List, Tuple, Optional


class Cell:
    # status 1 = Cell Alive
    def __init__(self, x: int, y: int, initial_status: int) -> None:
        self.x = x
        self.y = y

        self.next_generation_is_alive = None
        self.neighbors = None

        if initial_status == 1:
            self.is_alive = True
        else:
            self.is_alive = False

    def pass_generation(self, verbose: Optional[bool] = False):
        if self.next_generation_is_alive is None:
            if verbose:
                print(f"my status didnt change, im ({self.x}, {self.y})")
        else:
            self.is_alive = self.next_generation_is_alive
            self.next_generation_is_alive = None

    def get_neighbors(self):
        return self.neighbors

    def calculate_neighbors(
        self, n_lines: int, n_cols: int, verbose: Optional[bool] = False
    ) -> List[Tuple[int, int]]:
        base_neighbors = [
            (self.x - 1, self.y),  # 6
            (self.x - 1, self.y + 1),  # 7
            (self.x, self.y + 1),  # 1
            (self.x + 1, self.y + 1),  # 4
            (self.x + 1, self.y),  # 3
            (self.x + 1, self.y - 1),  # 5
            (self.x, self.y - 1),  # 2
            (self.x - 1, self.y - 1),  # 8
        ]
        neighbors = []
        for (x, y) in base_neighbors:
            if verbose:
                print(
                    f"[{x}],[{y}]: x>lines {x > (n_lines - 1)}, x>cols {y > (n_cols - 1)}, {x<0}, {y<0}"
                )
            # -1 => index, n_cols = len
            if (x > (n_lines - 1)) or (y > (n_cols - 1)) or (x < 0) or (y < 0):
                pass
            else:
                neighbors.append((x, y))
                if verbose:
                    print((self.x, self.y), neighbors)
        self.neighbors = neighbors

    def calculate_next_generation_state(self, n_alive_neighbors):
        self.n_alive_neighbors = n_alive_neighbors
        if self.is_alive:
            if self.check_underpopulation():
                self.next_generation_is_alive = False
            if self.check_overpopulation():
                self.next_generation_is_alive = False
            # if self.check_lives_on():
            #     self.is_alive = True
        else:
            if self.check_reproduction():
                self.next_generation_is_alive = True

    def check_underpopulation(self):
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        return self.n_alive_neighbors < 2

    def check_lives_on(self):
        # Any live cell with two or three live neighbours lives on to the next generation.
        return self.n_alive_neighbors == 2 or self.n_alive_neighbors == 3

    def check_overpopulation(self):
        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        return self.n_alive_neighbors > 3

    def check_reproduction(self):
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        return self.n_alive_neighbors == 3

    def __str__(self):
        if self.is_alive == True:
            return "*"
        else:
            return " "

    def __eq__(self, other):
        return (
            self.is_alive == other.is_alive and self.x == other.x and self.y == other.y
        )

    def __ne__(self, other):
        return self.is_alive != other.is_alive or self.x != other.x or self.y != other.y

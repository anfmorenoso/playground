import pytest
from game_of_life.cell import Cell


@pytest.mark.parametrize(
    ("x", "y", "status", "x2", "y2", "status2", "expected_result"),
    [
        (0, 0, 1, 0, 0, 1, True),
        (0, 1, 0, 0, 1, 0, True),
        (1, 0, 0, 0, 0, 0, False),
    ],
)
def test_cell_equals(x, y, status, x2, y2, status2, expected_result):
    # Given
    cell_1 = Cell(x, y, status)
    cell_2 = Cell(x2, y2, status2)
    # When
    result = cell_1 == cell_2
    # Then
    assert result == expected_result


@pytest.mark.parametrize(
    ("x", "y", "status", "x2", "y2", "status2", "expected_result"),
    [
        (0, 0, 1, 0, 0, 0, True),
        (0, 1, 0, 0, 1, 0, False),
        (1, 0, 0, 1, 0, 0, False),
    ],
)
def test_cell_not_equals(x, y, status, x2, y2, status2, expected_result):
    # Given
    cell_1 = Cell(x, y, status)
    cell_2 = Cell(x2, y2, status2)
    # When
    result = cell_1 != cell_2
    # Then
    a = 10
    assert result == expected_result


@pytest.mark.parametrize(
    ("n_lines", "n_cols", "input_cell", "expected_neighbors"),
    [
        (4, 5, Cell(0, 0, 0), [(0, 1), (1, 1), (1, 0)]),  # origin
        (4, 5, Cell(3, 4, 0), [(2, 4), (3, 3), (2, 3)]),  # bottom right edge
        (4, 5, Cell(3, 2, 0), [(2, 2), (2, 3), (3, 3), (3, 1), (2, 1)]),  # bottom edge
        (4, 5, Cell(2, 4, 0), [(1, 4), (3, 4), (3, 3), (2, 3), (1, 3)]),  # right edge
        (4, 5, Cell(0, 2, 0), [(0, 3), (1, 3), (1, 2), (1, 1), (0, 1)]),  # top edge
        (4, 5, Cell(2, 0, 0), [(1, 0), (1, 1), (2, 1), (3, 1), (3, 0)]),  # left edge
    ],
)
def test_calculate_neighbors_origin(n_lines, n_cols, input_cell, expected_neighbors):
    # Given
    # When
    input_cell.calculate_neighbors(n_lines, n_cols)
    # Then
    assert input_cell.get_neighbors() == expected_neighbors


# TODO : this one is fundamentally false as the origin cell can have maximum 3 neighbors
@pytest.mark.parametrize(
    ("cell", "n_alive_neighbors", "expected_next_state"),
    [
        (Cell(0, 0, 1), 1, False),
        (Cell(0, 0, 1), 4, False),
        (Cell(0, 0, 1), 2, True),
        (Cell(0, 0, 1), 3, True),
        (Cell(0, 0, 0), 3, True),
    ],
)
def calculate_next_generation_state(
    cell: Cell, n_alive_neighbors: int, expected_next_state: bool
):
    # Given
    # When
    cell.calculate_next_generation_state()
    # Then
    assert cell.next_generation_is_alive == expected_next_state

import pytest
import copy
from game_of_life.grid import Grid, UnevenGridException, EmptyGridException


def test_uneven_grid():
    # Given
    grid_array = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    # When
    with pytest.raises(UnevenGridException):
        Grid(grid_array)
    # Then


def test_empty_grid():
    # Given
    grid_array = []
    # When
    with pytest.raises(EmptyGridException):
        Grid(grid_array)
    # Then


def test_equals():
    # Given
    initial_grid = Grid(
        [
            [0, 0, 0],
            [0, 0, 0],
        ]
    )
    other_grid = Grid(
        [
            [0, 0, 0],
            [0, 0, 0],
        ]
    )
    expected = True
    # When
    result = initial_grid == other_grid
    # Then
    assert result == expected


def test_equals_false():
    # Given
    initial_grid = Grid(
        [
            [0, 0, 0],
            [0, 0, 0],
        ]
    )
    other_grid = Grid(
        [
            [0, 1, 0],
            [0, 0, 0],
        ]
    )
    expected = False
    # When
    result = initial_grid == other_grid
    # Then
    assert result == expected


def test_next_generation():
    # Given
    initial_grid = Grid(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    expected_next_grid = Grid(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )

    # When
    initial_grid.next_generation()
    # Then
    assert initial_grid == expected_next_grid


def test_oscillator_blinker():
    # Given
    initial_grid = Grid(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    test_grid = copy.deepcopy(initial_grid)
    expected_next_grid = Grid(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    # When
    test_grid.next_generation()
    # Then
    assert test_grid == expected_next_grid
    # This configuration is supposed to the initial_state (generation 0) in the second generation
    test_grid.next_generation()
    assert test_grid == initial_grid


def test_oscillator_beacon():
    # Given
    initial_grid = Grid(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    test_grid = copy.deepcopy(initial_grid)
    expected_next_grid = Grid(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    # When
    test_grid.next_generation()
    # Then
    assert test_grid == expected_next_grid
    # This configuration is supposed to the initial_state (generation 0) in the second generation
    test_grid.next_generation()
    assert test_grid == initial_grid


def test_still_life_block():
    # Given
    initial_grid = Grid(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
    )
    expected_next_grid = Grid(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
    )
    # When
    initial_grid.next_generation()
    # Then
    assert initial_grid == expected_next_grid

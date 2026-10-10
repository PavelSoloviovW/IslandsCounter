import pytest

from number_of_islands.islands_counter import IslandsCounter

STR_AND_INT = [
    pytest.param("1", "0", id="str"),
    pytest.param(1, 0, id="int"),
]


@pytest.fixture
def islands_counter() -> IslandsCounter:
    return IslandsCounter()


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_two_islands(islands_counter, land, water):
    grid = [
        [land, land, water, water],
        [land, water, water, land],
        [water, water, land, land],
    ]
    assert islands_counter.numIslands(grid) == 2


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_diagonal_cells_are_not_connected(islands_counter, land, water):
    grid = [
        [land, water],
        [water, land],
    ]
    assert islands_counter.numIslands(grid) == 2


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_ring_around_lake_is_one_island(islands_counter, land, water):
    grid = [
        [land, land, land],
        [land, water, land],
        [land, land, land],
    ]
    assert islands_counter.numIslands(grid) == 1


@pytest.mark.parametrize("grid", [[], [[]]])
def test_empty_grid(islands_counter, grid):
    assert islands_counter.numIslands(grid) == 0


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_all_water(islands_counter, land, water):
    assert islands_counter.numIslands([[water] * 5 for _ in range(5)]) == 0


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_single_row_all_land(islands_counter, land, water):
    assert islands_counter.numIslands([[land] * 100]) == 1


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_single_row_alternating(islands_counter, land, water):
    assert islands_counter.numIslands([[land, water] * 50]) == 50


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_single_column_all_land(islands_counter, land, water):
    assert islands_counter.numIslands([[land] for _ in range(100)]) == 1


@pytest.mark.parametrize("land, water", STR_AND_INT)
def test_full_50x50_grid(islands_counter, land, water):
    assert islands_counter.numIslands([[land] * 50 for _ in range(50)]) == 1

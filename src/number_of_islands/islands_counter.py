from collections.abc import Iterator
from itertools import product

LAND_TO_WATER = {"1": "0", 1: 0}
LAND_VALUES = frozenset(LAND_TO_WATER)
WATER_VALUES = frozenset(LAND_TO_WATER.values())
ALLOWED_VALUES = LAND_VALUES | WATER_VALUES
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

Grid = list[list[str]] | list[list[int]]
Cell = tuple[int, int]


class IslandsCounter:
    def numIslands(self, grid: Grid) -> int:
        if not grid or not grid[0]:
            return 0

        _validate_grid(grid)
        working_grid = _copy_grid(grid)
        island_count = 0

        for cell in _all_cells(working_grid):
            if _is_land(working_grid, cell):
                island_count += 1
                _sink_island(working_grid, start=cell)

        return island_count


def _validate_grid(grid: Grid) -> None:
    unexpected = {value for row in grid for value in row} - ALLOWED_VALUES
    if unexpected:
        raise ValueError(f"Unexpected cell values: {unexpected}")


def _copy_grid(grid: Grid) -> Grid:
    return [row[:] for row in grid]


def _all_cells(grid: Grid) -> Iterator[Cell]:
    return product(range(len(grid)), range(len(grid[0])))


def _is_land(grid: Grid, cell: Cell) -> bool:
    row, col = cell
    in_bounds = 0 <= row < len(grid) and 0 <= col < len(grid[0])
    return in_bounds and grid[row][col] in LAND_VALUES


def _land_neighbors(grid: Grid, cell: Cell) -> Iterator[Cell]:
    row, col = cell
    for d_row, d_col in DIRECTIONS:
        neighbor = (row + d_row, col + d_col)
        if _is_land(grid, neighbor):
            yield neighbor


def _mark_water(grid: Grid, cell: Cell) -> None:
    row, col = cell
    grid[row][col] = LAND_TO_WATER[grid[row][col]]


def _sink_island(grid: Grid, start: Cell) -> None:
    _mark_water(grid, start)
    pending = [start]

    while pending:
        current = pending.pop()
        for neighbor in _land_neighbors(grid, current):
            _mark_water(grid, neighbor)
            pending.append(neighbor)

# Number of Islands

Counts the number of islands in a grid.

## What it does

The input is a grid of `1` (land) and `0` (water). An island is a group of land cells connected horizontally or vertically. Diagonal cells are not connected.

```python
from number_of_islands.islands_counter import IslandsCounter

grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
]

print(IslandsCounter().numIslands(grid))  # 2
```

Details:

- the traversal is iterative (explicit stack), so large islands never cause a `RecursionError`
- the input grid is not modified
- cells can be strings (`"1"`, `"0"`) or integers (`1`, `0`)
- an unexpected cell value (for example `"2"` or `None`) raises `ValueError`
- an empty grid (`[]` or `[[]]`) returns `0`

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

## Running

```bash
uv run number-of-islands
```

This runs the `number_of_islands.main:main` entry point defined in `pyproject.toml`.

## Tests

```bash
uv run pytest -v
```

## Project structure

```
.
├── pyproject.toml
├── README.md
├── uv.lock
├── src/
│   └── number_of_islands/
│       ├── __init__.py
│       ├── islands_counter.py   # the solution
│       └── main.py              # entry point
└── tests/
    ├── __init__.py
    └── test_number_of_islands.py
```
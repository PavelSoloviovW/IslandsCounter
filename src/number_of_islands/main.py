from number_of_islands.islands_counter import IslandsCounter

test_1 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 1],
]

test_2 = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
]

test_3 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
]


def main() -> None:
    islands_counter = IslandsCounter()

    tests_result = True
    tests_result = tests_result & (islands_counter.numIslands(test_1) == 2)
    tests_result = tests_result & (islands_counter.numIslands(test_2) == 3)
    tests_result = tests_result & (islands_counter.numIslands(test_3) == 2)
    if not tests_result:
        raise ValueError("Failed")
    print("Done")

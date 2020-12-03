import math
from typing import Generator, Tuple


def read_file() -> Generator[str, None, None]:
    with open("input.txt") as text:
        yield from text.readlines()


def cnt_trees(rows: Tuple[str], step: int, num: int) -> int:
    index, trees = 0, 0
    length: int = len(rows[0])
    for row in (row for row_index, row in enumerate(rows) if row_index % num == 0):
        trees += 1 if row[index] == "#" else 0
        index += step + (0 if index + step + 1 < length else 1 - length)
    return trees


data: Tuple[str] = tuple(read_file())
print(f"Part 1: {cnt_trees(data, 3, 1)}")
print(f"Part 2: {math.prod((*(cnt_trees(data, st, 1) for st in range(1, 8, 2)), cnt_trees(data, 1, 2)))}")

import itertools
import math
from typing import Generator


def read_file() -> Generator[int, None, None]:
    with open("input.txt") as text:
        for line in text.readlines():
            yield int(line.strip())


def find_x_numbers_mul(data: Generator[int, None, None], equals: int, x: int) -> int:
    filtered: filter = filter(lambda nums: sum(nums) == equals, itertools.combinations(data, x))
    return math.prod(*filtered)


print(f"Part 1: {find_x_numbers_mul(read_file(), 2020, 2)}")
print(f"Part 2: {find_x_numbers_mul(read_file(), 2020, 3)}")

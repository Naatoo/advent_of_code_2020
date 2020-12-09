import collections
import itertools
from typing import Generator, Tuple


def parse_file() -> Generator[int, None, None]:
    with open("input.txt") as file:
        yield from map(int, file.readlines())


def part_1(preamble: int = 25) -> int:
    program: Generator[int, None, None] = parse_file()
    current_values: collections.deque = collections.deque((next(program) for _ in range(preamble)), maxlen=preamble)
    while (num := next(program)) in set(map(sum, itertools.combinations(current_values, 2))):
        current_values.append(num)
    return num


def part_2(val: int) -> int:
    program: Tuple[int] = tuple(parse_file())
    for basic_index in itertools.count():
        for index in itertools.count(basic_index):
            zxc = sum(program[basic_index: index])
            if zxc > val:
                break
            elif zxc == val:
                vbn = program[basic_index: index]
                return min(vbn) + max(vbn)


part_1_res: int = part_1()
print("Part 1:", part_1_res)
print("Part 2:", part_2(part_1_res))

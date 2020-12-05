import itertools
from typing import Generator


def read_file() -> Generator[str, None, None]:
    with open("input.txt") as file:
        for line in file.readlines():
            yield line.strip()


def get_place(signs: str, possible_places: range, higher: str) -> int:
    for sign in signs:
        half_length: int = len(possible_places) // 2
        possible_places = possible_places[half_length:] if sign == higher else possible_places[:half_length]
    return next(iter(possible_places))


seats: set = set((get_place(line[:7], range(128), "B"), get_place(line[7:], range(8), "R")) for line in read_file())
print(f"Part 1: {max(indexes[0] * 8 + indexes[1] for indexes in seats)}")

prev: int = 0
for place in sorted(set(itertools.product(range(128), range(8))).difference(seats), key=lambda x: x[0]):
    if place[0] in range(prev + 1):
        prev += 1 if place[0] == prev else 0
    else:
        break

print(f"Part 2: {place[0] * 8 + place[1]}")

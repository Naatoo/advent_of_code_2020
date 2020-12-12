import itertools

from typing import Dict, List


def parse_file() -> Dict[tuple, str]:
    data: dict = {}
    with open("input.txt") as file:
        for row_index, line in enumerate(file.readlines()):
            data.update({(row_index, column_index): sign for column_index, sign in enumerate(line.strip())})
    return data


data: Dict[tuple, str] = parse_file()
common_adjacents: List[tuple] = [pair for pair in itertools.product((-1, 0, 1), repeat=2) if pair != (0, 0)]
to_be_taken = ...
while to_be_taken:
    for old_sign, new_sign, func in (("L", "#", lambda occ: sum(occ) == 0), ("#", "L", lambda occ: sum(occ) > 3)):
        to_be_taken: list = []
        for coords, sign in data.items():
            if sign == old_sign and func(data.get(tuple(map(sum, zip(coords, pair))), "L") == "#"
                                         for pair in common_adjacents):
                to_be_taken.append(coords)
        for coords in to_be_taken:
            data[coords] = new_sign

print("Part 1:", tuple(data.values()).count("#"))

data: Dict[tuple, str] = parse_file()
length = len(set(map(lambda coords: coords[1], tuple(data.keys()))))
updated = ...
while updated:
    for skip_sign, new_sign, func in (("#", "L", lambda nums: None not in nums and 0 not in nums),
                                      ("L", "#", lambda nums: sum(x for x in nums if x is not None) > 4)):
        updated: list = []
        for coords, sign in data.items():
            if sign in (".", skip_sign):
                continue
            adjacents: List[tuple] = [pair for pair in itertools.product((-1, 0, 1), repeat=2) if pair != (0, 0)]
            free: dict = {adj: None for adj in common_adjacents}
            for val in range(1, length - 1):
                tbr: list = []
                for pair in adjacents:
                    seat = data.get(tuple(map(sum, zip(coords, (c * val for c in pair)))), "L")
                    if seat == ".":
                        continue
                    else:
                        free[pair] = 1 if seat == new_sign else 0
                        tbr.append(pair)
                for pair in tbr:
                    adjacents.remove(pair)
                if func(free.values()):
                    updated.append(coords)
                    break
        for coords in updated:
            data[coords] = skip_sign

print("Part 2:", tuple(data.values()).count("#"))

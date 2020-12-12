import collections
from typing import Dict, List


def parse_file() -> Dict[tuple, str]:
    with open("input.txt") as file:
        for line in file.readlines():
            yield line[0], int(line[1:])


coords = [0, 0]
directions: dict = {"E": (0, -1), "W": (0, 1), "N": (1, -1), "S": (1, 1)}
current_dir = collections.deque(("E", "S", "W", "N"))

for sign, val in parse_file():
    if sign in (*current_dir, "F"):
        index, basic_val = directions[sign if sign != "F" else current_dir[0]]
        coords[index] += val * basic_val
    else:
        current_dir.rotate(val // 90 * (1 if sign == "L" else -1))

print("Part 1:", sum(abs(c) for c in coords))


ship: tuple = 0, 0
waypoint: List = [10, 1]

for sign, val in parse_file():
    if sign in directions.keys():
        index, basic_val = directions[sign]
        waypoint[index] += - val * basic_val
    elif sign in ("L", "R"):
        for _ in range(val // 90):
            waypoint[1 if sign == "L" else 0] *= -1
            waypoint.reverse()
    else:
        ship = tuple(map(sum, zip(ship, (w * val for w in waypoint))))


print("Part 2:", sum(abs(c) for c in ship))

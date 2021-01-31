from typing import Dict, Tuple


def parse_file() -> tuple:
    with open("input.txt") as file:
        return int(file.readline()), file.readline().split(",")


timestamp, lines = parse_file()
vals: Tuple[int] = tuple(int(val) for val in lines if val != "x")
over_ts: Tuple[int] = tuple(range(0, timestamp + li, li)[-1] for li in vals)
print("Part 1:", vals[over_ts.index(min(over_ts))] * (min(over_ts) - timestamp))

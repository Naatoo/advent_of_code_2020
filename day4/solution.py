from typing import Tuple, Generator, Dict


def read_file() -> Generator[str, None, None]:
    with open("input.txt") as file:
        for line in file.readlines():
            yield line.strip()


def part_1(data: Generator[str, None, None]):
    valid, cnt, cid = 0, 0, 0
    data: Tuple[str, ...] = tuple(data)
    for index, line in enumerate(data):
        cid += line.count("cid")
        cnt += line.count(":")
        if not line or index + 1 == len(data):
            if cnt == 8 or (cnt == 7 and cid == 0):
                valid += 1
            cid, cnt = 0, 0
            continue
    return valid


def part_2(data: Generator[str, None, None]) -> int:
    validators: Dict[str, callable] = {
        'byr': lambda val: 1920 <= int(val) <= 2002,
        'iyr': lambda val: 2010 <= int(val) <= 2020,
        'eyr': lambda val: 2020 <= int(val) <= 2030,
        'hgt': lambda val: 150 <= int(val.split("cm")[0]) <= 193 if 'cm' in val else 59 <= int(val.split("in")[0]) <= 76,
        'hcl': lambda val: val[0] == "#" and len(val) == 7 and all(sign in '0123456789abcdef' for sign in val[1:]),
        'ecl': lambda val: val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda val: val.isdigit() and len(val) == 9
    }
    quantity: int = 0
    for pas in parse_data(data):
        for field, func in validators.items():
            if field not in pas or not func(pas[field]):
                break
        else:
            quantity += 1
    return quantity


def parse_data(data: Generator[str, None, None]) -> Generator[Dict[str, callable], None, None]:
    pas: dict = {}
    for line in data:
        if not line:
            yield pas
            pas: dict = {}
            continue
        for (key, value) in (field.split(":") for field in line.split(" ")):
            pas[key] = value
    yield pas


print(f"Part 1: {part_1(read_file())}")
print(f"Part 2: {part_2(read_file())}")
import copy
from typing import List


def parse_file():
    with open("input.txt") as file:
        return [(line.split()[0], int(line.split()[1])) for line in file.readlines()]


def execute_until_repeat(data: list):
    used_indexes: set = set()
    index, accumulator = 0, 0
    try:
        while index not in used_indexes:
            used_indexes.add(index)
            action, val = data[index]
            if action == "acc":
                accumulator += val
                index += 1
            elif action == "nop":
                index += 1
            else:
                index += val
    except IndexError:
        raise StopIteration(accumulator)
    return accumulator


data: List[tuple] = parse_file()
print("Part 1:", execute_until_repeat(data))

for index, (action, val) in enumerate(data):
    if action == "acc":
        continue
    data_updated = copy.deepcopy(data)
    data_updated[index] = 'jmp' if action == "nop" else 'nop', val
    try:
        execute_until_repeat(data_updated)
    except StopIteration as e:
        print("Part 2:", e.value)

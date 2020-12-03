import collections
import re
from typing import Generator


def read_file() -> Generator[int, None, None]:
    with open("input.txt") as text:
        for row in text.readlines():
            yield re.search(r'(\d+)-(\d+)\s(\w):\s(\w+)', row).groups()


print("Part 1: " + str(sum(1 for min_occur, max_occur, sign, password in read_file()
                           if collections.Counter(password)[sign] in range(int(min_occur), int(max_occur) + 1))))

print("Part 2: " + str(sum(1 for *indexes, sign, password in read_file()
                           if sum(map(lambda index: int(password[int(index) - 1] == sign), indexes)) == 1)))

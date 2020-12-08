def parse_file():
    with open("input.txt") as file:
        for line in file.readlines():
            (*name_parts, _), content = (part.split() for part in line.split(" contain "))
            single_bag_contains = {" ".join(content[index + 1: index + 3]): int(content[index])
                                   for index in range(len(content)) if index % 4 == 0 and len(content) > 3}
            yield " ".join(name_parts), single_bag_contains


my_bag: str = "shiny gold"
data: dict = {name: content for name, content in parse_file()}


def find_bag(demanded_name: str) -> set:
    bags_container: set = set()
    for bag_name, content in data.items():
        if demanded_name in content:
            bags_container.update({bag_name, *find_bag(bag_name)})
    return bags_container


print("Part 1:", len(find_bag(my_bag)))


def find_content(demanded_name: str, demanded_bag_quantity: int) -> int:
    content: dict = data[demanded_name]
    nested_quantity = sum(demanded_bag_quantity * find_content(nested_bag_name, num)
                          for nested_bag_name, num in content.items())
    quantity = sum(map(lambda x: x * demanded_bag_quantity, content.values()))
    return quantity + nested_quantity


print("Part 2:", find_content(my_bag, 1))

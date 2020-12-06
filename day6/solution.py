import collections


with open("input.txt") as file:
    lines = file.read().split("\n\n")
    print(sum(len(collections.Counter("".join(questions.split()))) for questions in lines))
    print(sum(tuple(collections.Counter("".join(questions.split())).values()).count(questions.count("\n") + 1)
              for questions in lines))

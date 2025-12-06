import math
import numpy as np
from typing import Callable

INPUT_FILE = 'day-6 input.txt'

function_map: dict[str, Callable[[list[int]], int | float]] = {
    '*': math.prod,
    '+': math.fsum
}

def re_position(fields: list[str]) -> int:
    output = 0
    for char in fields:
        if char == ' ':
            continue
        output *= 10
        output += int(char)
    return output

with open(INPUT_FILE) as f:
    content = f.read()

all_stuff = np.array([list(row) for row in content.split("\n")]).transpose()

group_function: Callable[[list[int]], int | float] | None = None
group_arguments: list[int] = []
running_total: int = 0
for row in all_stuff:
    argument = re_position(row[:-1])

    if argument == 0 and row[-1] == ' ' and group_function is not None: # an empty row but also satisfy linter
        result = group_function(group_arguments)
        running_total += int(result)
        group_function = None
        group_arguments: list[int] = []
        continue

    group_arguments.append(argument)
    if row[-1] in function_map:
        group_function = function_map[row[-1]]

if group_function is not None: # for the linter
    result = group_function(group_arguments)
    running_total += int(result)

print(f"\n{running_total}")
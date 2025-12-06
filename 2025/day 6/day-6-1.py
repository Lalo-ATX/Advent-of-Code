import re
import math
import numpy as np
from typing import Callable

INPUT_FILE = 'day-6 input.txt'

function_map: dict[str, Callable[[list[int]], int | float]] = {
    '*': math.prod,
    '+': math.fsum
}

with open(INPUT_FILE) as f:
    content = f.read()

all_inputs = np.array([ re.split(r" +", line.strip()) for line in content.split("\n")])

output_sum: int = 0
for col_idx in range(np.size(all_inputs, 1)):
    column = all_inputs[:, col_idx]
    current_value = function_map[column[-1]]([int(x) for x in column[:-1]])
    output_sum += int(current_value)

print(output_sum)
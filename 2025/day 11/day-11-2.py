import time
from math import fsum, prod

INPUT_FILE = 'day-11 input.txt'

start_wall_time = time.time()
start_cpu_time = time.process_time()

def count_paths(hops: dict[str, list[str]], position: str, target: str, memo: dict[str, int]) -> int:
    if position in memo:
        return memo[position]
    if position == target:
        return 1
    if position not in hops:
        return 0

    # else, recurse
    memo[position] = int(fsum( count_paths(hops, next_hop, target, memo) for next_hop in hops[position] ))
    return memo[position]

with open(INPUT_FILE) as f:
    lines_fields = [ x.split(': ') for x in f.read().splitlines() ]

path_hop: dict[str, list[str]] = {
    line[0]: line[1].split(' ') for line in lines_fields
}

# since there's no loops, we can count on one of these being zero
central_order = [ 'dac', 'fft' ]
central_section = count_paths(path_hop, central_order[0], central_order[1], {})
if not central_section:
    central_order.reverse()
    central_section = count_paths(path_hop, central_order[0], central_order[1], {})

nav_path = [('svr', central_order[0]), (central_order[1], 'out')]
print(prod( [central_section] + [ count_paths(path_hop, from_node, to_node, {}) for from_node, to_node in nav_path ] ))


elapsed_wall_time = time.time() - start_wall_time
elapsed_cpu_time = time.process_time() - start_cpu_time
print(f"took {elapsed_wall_time:.3f} seconds / {elapsed_cpu_time:.3f} cpu seconds")
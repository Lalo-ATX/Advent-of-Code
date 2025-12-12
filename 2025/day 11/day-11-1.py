import time

INPUT_FILE = 'day-11 input.txt'

start_wall_time = time.time()
start_cpu_time = time.process_time()

# if this took too long, you could add memoization
# but this ran in 10ms on the production data, so there's no point
def count_paths(hops: dict[str, list[str]], position: str) -> int:
    if hops[position][0] == 'out':
        return 1
    
    # else, recurse
    return sum( [ count_paths(hops, next_hop) for next_hop in hops[position] ] )

with open(INPUT_FILE) as f:
    lines_fields = [ x.split(': ') for x in f.read().splitlines() ]

path_hop: dict[str, list[str]] = {}
for line in lines_fields:
    path_hop[line[0]] = line[1].split(' ')

print(count_paths(path_hop, 'you'))

elapsed_wall_time = time.time() - start_wall_time
elapsed_cpu_time = time.process_time() - start_cpu_time
print(f"took {elapsed_wall_time:.3f} seconds / {elapsed_cpu_time:.3f} cpu seconds")
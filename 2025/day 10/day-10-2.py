import time
import pulp # type: ignore missing stubs

INPUT_FILE = 'day-10 input.txt'

start_wall_time = time.time()
start_cpu_time = time.process_time()

def process_joltage(input_joltage: str) -> list[int]:
    return [ int(x) for x in input_joltage[1:-1].split(',') ]

def process_schematics(input_schematics: list[str], counters_count: int) -> list[list[int]]:
    result: list[list[int]] = []
    for schem in input_schematics:
        numbers = [ int(x) for x in schem[1:-1].split(',')]
        result.append( [ int(idx in numbers) for idx in range(counters_count) ] )
    return result        

with open(INPUT_FILE) as f:
    lines_fields = [ x.split(' ') for x in f.read().splitlines() ]

final_sum = 0
for line in lines_fields:
    light_diagram, input_schematics, input_joltage = line[0], line[1:-1], line[-1]
    joltages = process_joltage(input_joltage)
    schematics = process_schematics(input_schematics, len(joltages))
    upper_bound = max(joltages)

    variables = [ pulp.LpVariable(f"A_{idx}", 0, upper_bound, pulp.LpInteger) for idx in range(len(schematics)) ]

    # state the problem
    prob = pulp.LpProblem("Minimize button presses", pulp.LpMinimize)
    prob += pulp.lpSum(variables)

    # now let's add our constraints
    for col_idx, joltage in enumerate(joltages):
        prob += pulp.lpSum(
             [ variable * schematics[row_idx][col_idx] for row_idx, variable in enumerate(variables) ]  # type: ignore
            ) == joltage, f"constraint_{col_idx}"

    prob.solve(pulp.PULP_CBC_CMD(msg=False)) # type: ignore
    result = pulp.value(prob.objective) # type: ignore
    if isinstance(result, float):
        final_sum += int(result)
    else:
        print(f"unexpected result: {result}")

print(final_sum)

elapsed_wall_time = time.time() - start_wall_time
elapsed_cpu_time = time.process_time() - start_cpu_time
print(f"took {elapsed_wall_time:.3f} seconds / {elapsed_cpu_time:.3f} cpu seconds")
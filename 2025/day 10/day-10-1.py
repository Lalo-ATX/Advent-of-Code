import time

INPUT_FILE = 'day-10 input.txt'

start_wall_time = time.time()
start_cpu_time = time.process_time()

def light_diagram_int(diagram: str) -> int:
    light_value_string = ''.join( reversed([ str(int(char=='#')) for char in diagram[1:-1] ]) )
    return int(light_value_string, 2)

def process_schematics(input_schematics: list[str]) -> list[int]:
    result: list[int] = []
    for schem in input_schematics:
        numbers = [ int(x) for x in schem[1:-1].split(',')]
        val = int(0)
        for number in numbers:
            mask = 1 << number
            val |= mask
        result.append(val)
    return result        

def run_schematics(level: int, target: int, schematics: list[int], stats: dict[str, int]):
    level += 1
#    print(f"  starting level {level}, trying to match {target:08b}")
    # breadth-first search - helps make things a little faster
    for schematic in schematics:
#        print(f"    testing {schematic:08b}")
        if schematic == target:
            stats['best_solution'] = level
#            print(f"    found match {schematic:08b} = {target:08b} level {level}")
            return
    
    # it never matched. Should we go down a level? only if that level could
    # still be better than our current best solution
    if level + 1 >= stats['best_solution']:
        # the next level can't improve our current best soltion, so don't bother
        return

    # else... it might! give it a shot
    for idx, schematic in enumerate(schematics[:-1]):
        new_target = target ^ schematic
        run_schematics(level, new_target, schematics[idx+1:], stats)
    
    return

with open(INPUT_FILE) as f:
    lines_fields = [ x.split(' ') for x in f.read().splitlines() ]

final_output = 0
for line in lines_fields:
    light_diagram, input_schematics, joltage = line[0], line[1:-1], line[-1]
    light_value = light_diagram_int(light_diagram)
    schematics = process_schematics(input_schematics)
#    print(f"working {light_value:08b} / {light_value} against {len(schematics)} schematics")
    stats: dict[str, int] = {
        'best_solution': len(schematics) + 1
    }
    run_schematics(0, light_value, schematics, stats)
#    print(f"best we can do is {stats['best_solution']}")
    final_output += stats['best_solution']

print(f"final output: {final_output}")

elapsed_wall_time = time.time() - start_wall_time
elapsed_cpu_time = time.process_time() - start_cpu_time
print(f"took {elapsed_wall_time:.3f} seconds / {elapsed_cpu_time:.3f} cpu seconds")
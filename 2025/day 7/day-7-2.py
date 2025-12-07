from collections import defaultdict

INPUT_FILE = 'day-7 input.txt'

# global variables
beam_history: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))
cache_hits: dict[str, int] = {'count': 0}

# process_path does all the work
def process_path(beam_position: int, tach_manifold: list[str], manifold_row: int) -> int:
    total_left_paths: int = 0
    for row_idx, row in enumerate(tach_manifold):
        print(f"\r  {manifold_row:4d}, {beam_position:3d}: {total_left_paths:14d} / {cache_hits['count']:5d}", end="")
        if manifold_row in beam_history and beam_position in beam_history[manifold_row]:
            cache_hits['count'] += 1
            return beam_history[manifold_row][beam_position]

        # we're living in the future
        manifold_row += 1

        if row[beam_position] == '^':
            # branch of a test case to the left
            left_position = beam_position - 1
            left_paths = process_path(left_position, tach_manifold[row_idx+1:], manifold_row)
            beam_history[manifold_row][left_position] = left_paths
            total_left_paths += left_paths
            # and continue as normal to the right
            beam_position += 1

    # we've processed all the rows and all the others paths, let's give ourselves credit
    return total_left_paths + 1

with open(INPUT_FILE) as f:
    content = f.read()

# `not linenumber%2` filters out odd rows
tach_manifold = [line for linenumber, line in enumerate(content.splitlines()) if not linenumber%2]
first_row = tach_manifold.pop(0)
beam_position: int | None = None
for idx, column in enumerate(first_row):
    if column == 'S':
        beam_position = idx
        break

if beam_position is None: # for the linter
    exit(1)

path_count = process_path(beam_position, tach_manifold, 0)
print(f"\n{path_count}")
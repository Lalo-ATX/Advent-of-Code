INPUT_FILE = 'day-7 input.txt'

with open(INPUT_FILE) as f:
    content = f.read()

beams: set[int] = set()

# only need to keep even-numbered lines, cuts the processing down
tmanifold = [line for linenumber, line in enumerate(content.splitlines()) if not linenumber%2]
first_row = tmanifold.pop(0)
for idx, column in enumerate(first_row):
    if column == 'S':
        beams.add(idx)
        break

split_count = 0
for row in tmanifold:
    for beam_pos in list(beams):
        if row[beam_pos] == '^':
            beams.remove(beam_pos)
            beams.add(beam_pos - 1)
            beams.add(beam_pos + 1)
            split_count += 1

print(f"split {split_count} times")
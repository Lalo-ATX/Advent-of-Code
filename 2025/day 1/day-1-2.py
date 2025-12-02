INPUT_FILE = 'day-1 input.txt'
DIAL_SIZE = 100
DIRECTION_MAP = {'L': -1, 'R': 1}

dial_before = 50
dial_after = 50
zero_count = 0

with open(INPUT_FILE) as f:
    for line in f:
        direction_val = DIRECTION_MAP[line[0]]
        movement = direction_val * int(line[1:])

        dial_after = dial_before + movement

        # no need to check for a clockwise zero-cross because dial_before is always positive
        zero_cross = 1 if dial_before != 0 and dial_after <= 0 else 0

        wraps = abs(dial_after) // DIAL_SIZE
        zero_count += zero_cross + wraps

        print(f"m: {movement:4d} b: {dial_before:2d} a: {dial_after:3d} zc: {zero_cross} wr: {wraps:2d} c: {zero_count}")
        dial_before = dial_after % DIAL_SIZE
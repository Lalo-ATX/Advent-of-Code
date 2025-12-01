INPUT_FILE = 'day-1 input.txt'
DIAL_SIZE = 100

dial_pointer = 50
zero_count = 0

with open(INPUT_FILE) as f:
    for line in f:
        direction = line[0]
        multiplier = 1 if direction == 'R' else -1
        value = multiplier * int(line[1:])
        dial_pointer = (dial_pointer + value) % DIAL_SIZE
        if dial_pointer == 0:
            zero_count += 1
        print(f"line: {line} value: {value} dial: {dial_pointer} zeros: {zero_count}")
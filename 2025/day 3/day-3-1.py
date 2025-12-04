from typing import NamedTuple

INPUT_FILE = 'day-3 input.txt'

class ValPos(NamedTuple):
    value: int
    position: int

def de_position(input_number: int) -> list[int]:
    positions: list[int] = []
    while input_number:
        positions.append(input_number % 10)
        input_number = input_number // 10
    positions.reverse()
    return positions

def max_valpos(input_list: list[int]) -> ValPos:
    max_value = 0
    max_position = 0
    for idx, digit in enumerate(input_list):
        if digit > max_value:
            max_value = digit
            max_position = idx
    return ValPos(max_value, max_position)

result_sum: int = 0
with open(INPUT_FILE) as f:
    for line in f:
        in_number = int(line)
        positions = de_position(in_number)

        digit_1vp = max_valpos(positions[:-1])
        digit_2 = max(positions[digit_1vp.position+1:])

        result = digit_1vp.value * 10 + digit_2

        print(f"{in_number=} {result=}")
        result_sum += result

print(f"{result_sum=}")




# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
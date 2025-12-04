from typing import NamedTuple

INPUT_FILE = 'day-3 input.txt'
DIGITS_OUT = 12

class ValPos(NamedTuple):
    value: int
    position: int

def de_position(input_number: int) -> list[int]:
    positions: list[int] = []
    while input_number: # this is dumb and will break if the number ends in zero
        positions.append(input_number % 10)
        input_number = input_number // 10
    positions.reverse()
    return positions

def re_position(input_list: list[int]) -> int:
    output: int = 0
    for digit in input_list:
        output *= 10
        output += digit
    return output

def max_valpos(input_list: list[int]) -> ValPos:
    max_value = 0
    max_position = 0
    for idx, digit in enumerate(input_list):
        if digit > max_value:
            max_value = digit
            max_position = idx
            if max_value == 9:
                break
    return ValPos(max_value, max_position)

def process(positions: list[int], digit_count: int, result_digits: list[int]) -> None:
    if digit_count == 1:
        result_digits.append(max(positions))
        return
    
    # else
    my_digit_vp = max_valpos(positions[:-(digit_count-1)])
    result_digits.append(my_digit_vp.value)

    process(positions[my_digit_vp.position+1:], digit_count - 1, result_digits)


result_sum: int = 0
with open(INPUT_FILE) as f:
    for line in f:
        in_number = int(line) # this is wildly optimistic with a long input string - idk how python does it
        positions = de_position(in_number)

        result_digits: list[int] = []
        process(positions, DIGITS_OUT, result_digits)
        result = re_position(result_digits)
        result_sum += result

print(f"{result_sum=}")
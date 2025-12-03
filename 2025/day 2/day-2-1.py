import math
INPUT_FILE = 'day-2 input.txt'

with open(INPUT_FILE) as f:
    content = f.read()

output_sum = 0
for set in content.split(","):
    in_low, in_high = (int(x) for x in set.split("-"))
    digits_low = math.floor(math.log10(in_low))
    digits_high = math.floor(math.log10(in_high))

    if digits_low == digits_high and not digits_low % 2:
        print(f"skipping {in_low}-{in_high}: both odd length")
        continue

#    print(f"{in_low=} {digits_low=} {in_high=} {digits_high=}")
    if digits_high - digits_low > 1:
        print("WARNING: crossing some boundaries here bub")

    # default assume in_low is the starting point, and in_high is the ending point
    # if low is odd and high is even, then the low starting point is 1E+digits_high
    # if low is even and high is odd, then the high ending point is 1E+digits_low - 1
    if digits_low % 2:
        start_number = in_low
    else:
        start_number = 10**digits_high
        digits_low += 1
    
    if digits_high % 2:
        end_number = in_high
    else:
        end_number = 10**digits_high - 1

    print(f"going to test from {start_number=} to {end_number=}")

    half_length = (digits_low+1)/2
    start_number_left =  start_number // 10**half_length
    start_number_right = start_number % 10**half_length
    if start_number_right > start_number_left:
        start_number_left += 1

    test_number = start_number_left * 10**half_length + start_number_left
    print(f"starting from {test_number}")

    # next time the answer is the integral for y = (a + x) * 10**half_length + a + x for x=0 to (end_left - start_left)
    # with adjustment up if end_right > end_left and down if start_left > start_right
    while test_number <= end_number:
        output_sum += test_number
        print(f"found {test_number}")
        start_number_left += 1
        test_number = start_number_left * 10**half_length + start_number_left

print(f"output sum: {output_sum}")
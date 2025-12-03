import math
from typing import NamedTuple

INPUT_FILE = 'day-2 input.txt'

class TestRange(NamedTuple):
    start_number: int
    end_number: int
    digits: int

def factors(x: int) -> list[int]:
    return [i for i in range(1, x) if x % i == 0]

def de_position(whole_number: int, chunk_size: int) -> list[int]:
    chunks: list[int] = []
#    chunks = [ (whole_number // 10**(chunk_size*x)) % 10**chunk_size for x in range((int((math.log10(whole_number)+1)/chunk_size)))]
    for _ in range((int((math.log10(whole_number)+1)/chunk_size))):
        chunks.append(whole_number % 10**chunk_size)
        whole_number = whole_number // 10**chunk_size
    chunks.reverse()
    return chunks

def re_position(chunks: list[int]) -> int:
    chunk_size = math.floor(math.log10(chunks[0])) + 1
    whole_number = 0
    for chunk in chunks[::-1]: # [::-1] makes a reversed copy of the list, says Copilot
        whole_number = whole_number * 10**chunk_size
        whole_number += chunk
    return int(whole_number)

with open(INPUT_FILE) as f:
    content = f.read()

output_sum = 0
for id_range in content.split(","):
    in_low, in_high = (int(x) for x in id_range.split("-"))
    digits_low = math.floor(math.log10(in_low))
    digits_high = math.floor(math.log10(in_high))

    if digits_low == digits_high:
        test_ranges = [
            TestRange(in_low, in_high, digits_low)
        ]
    else:
        test_ranges = [
            TestRange(in_low, 10**digits_high - 1, digits_low),
            TestRange(10**digits_high, in_high, digits_high)
        ]

    seen_ids: set[int] = set()
    for test_range in test_ranges:
        subranges = factors(test_range.digits+1)
        for subrange in subranges:
            chunks_start = de_position(test_range.start_number, subrange)
            root_start = chunks_start[0]
            for chunk in chunks_start:
                if chunk > root_start:
                    root_start += 1
                    break
                if chunk < root_start:
                    break
            chunks_end = de_position(test_range.end_number, subrange)
            root_end = chunks_end[0]
            for chunk in chunks_end:
                if chunk < root_end:
                    root_end -= 1
                    break
                if chunk > root_end:
                    break
            test_number = re_position([root_start] * len(chunks_start))
            print(f"chunk len={len(chunks_start)} {chunks_start=} {chunks_end=} {root_start=} {root_end=} {test_number=}")
            while test_number <= test_range.end_number:
                if test_number not in seen_ids:
                    print(f" - {test_number=} works")
                    output_sum += test_number
                    seen_ids.add(test_number)
                root_start += 1
                test_number = re_position([root_start] * len(chunks_start))

print(f"output sum: {output_sum}")
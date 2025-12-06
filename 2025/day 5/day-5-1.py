from typing import NamedTuple

class Bookends(NamedTuple):
    low_end: int
    high_end: int

INPUT_FILE = 'day-5 input.txt'

# 1: below, below
# 2: below, between
# 3: below, above
# 4: between, between
# 5: between, above
# 6: above, above

def add_range_really(new_bookend: Bookends, range_db: list[Bookends]) -> None:
#    print(f"testing {new_bookend.low_end}-{new_bookend.high_end} against {range_db}")
    for idx, bookend in enumerate(range_db):
        if new_bookend.low_end < bookend.low_end:
            if new_bookend.high_end < bookend.low_end:
                # 1: below, below
                # insert ahead and return
                range_db.insert(idx, new_bookend)
                return

            # 2: below, between
            # 3: below: above
            # else, new_bookend.high_end must be >= bookend.low_end
            # delete the old bookend, expand it and re-add it
            range_db.pop(idx)
            add_range_really(Bookends(new_bookend.low_end, max([bookend.high_end, new_bookend.high_end])), range_db)
            return

        # new_bookend.low_end must be >= bookend.low_end
        if new_bookend.low_end <= bookend.high_end:
            # 4: between, between
            # 5: between, above
            range_db.pop(idx)
            add_range_really(Bookends(bookend.low_end, max([bookend.high_end, new_bookend.high_end])), range_db)
            return
        
        # else, continue
    
    # if we get here, that means we're #6, above, above
    range_db.append(new_bookend)


def add_range(id_range: str, range_db: list[Bookends]) -> None:
    id_low, id_high = id_range.split("-")
    new_bookend = Bookends(int(id_low), int(id_high))
    add_range_really(new_bookend, range_db)

def check_ranges(test_id: int, range_db: list[Bookends]) -> bool:
    for check_range in range_db:
        if check_range.low_end <= test_id <= check_range.high_end:
            return True
    return False

with open(INPUT_FILE) as f:
    content = f.read()

id_ranges, ids = content.split("\n\n")

range_db: list[Bookends] = []

for id_range in id_ranges.split("\n"):
    add_range(id_range, range_db)

#print(f"finished with {range_db}")

fresh_count = 0
for test_id in ids.split("\n"):
    if check_ranges(int(test_id), range_db):
        fresh_count += 1

print(f"fresh: {fresh_count}")